import os
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.utils.text import slugify
from .workers import pdf2text, txt2questions
from django.http import HttpResponse
from django.shortcuts import render
from django.http import StreamingHttpResponse
from urllib.parse import urlencode
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# Create your views here.
def genQuizHome(request):
    return render(request, "mcq_generator.html")


def quizGenPage(request):
    """ Handle upload and conversion of file + other stuff """
    quiz_data = {}

    # Make directory to store uploaded files, if not exists
    if not os.path.isdir(os.path.join(settings.MEDIA_ROOT, 'pdf')):
        os.mkdir(os.path.join(settings.MEDIA_ROOT, 'pdf'))

    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        if not request.POST.get("numPages"):
            numPages = 10
        else:
            numPages = int(request.POST.get("numPages"))
        file_path = os.path.join(
            settings.MEDIA_ROOT,
            'pdf',
            slugify(uploaded_file.name))
        file_exten = uploaded_file.name.rsplit('.', 1)[1].lower()

        # Save uploaded file
        fs = FileSystemStorage()
        fs.save(file_path, uploaded_file)
        # Get contents of file
        uploaded_content = pdf2text(file_path, file_exten)
        quiz_data = txt2questions(uploaded_content, numPages)
        # File upload + convert success
        if uploaded_content is not None:
            pdf_path = os.path.join(
            settings.MEDIA_ROOT,
            'pdf',
            'quiz_data.pdf'
            )
            
            makePDFfile(quiz_data, pdf_path)
        
            # pdf is streamed in chunks, rather than loading entire file
            def file_iterator():
                with open(pdf_path, 'rb') as f:
                    for chunk in iter(lambda: f.read(8192), b''):
                        yield chunk

            # use StreamingHttpResponse to load pdf content
            response = StreamingHttpResponse(
                file_iterator(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="mcqFile"'
            return response
        
        else:
            return HttpResponse("No pdf uploaded")
    else:
        return HttpResponse("No pdf uploaded")


def makePDFfile(quiz_data, pdf_path):
    doc = SimpleDocTemplate(pdf_path, pagesize=letter)
            
    # Define the styles for the document
    styles = getSampleStyleSheet()

    # List to hold the content of the PDF
    content = []

    # Loop through each question and add its content to the PDF
    for question_number, question_data in quiz_data.items():
        question = question_data['question']
        answer = question_data['answer']
        options = question_data['options']

        # Define the content for the question
        question_text = f"Question {question_number}: {question}<br/>" \
                        f"Answer: {answer}<br/>" \
                        "Options:<br/>" + "<br/>".join(f"- {option}" for option in options)

        # Create a Paragraph element with the defined style
        question_paragraph = Paragraph(question_text, styles['Normal'])

        # Add the paragraph to the content
        content.append(question_paragraph)
        content.append(Spacer(1, 12))  # Add a space between questions
    
    doc.build(content)