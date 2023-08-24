# from PyPDF2 import PdfFileReader
from .question_generation_main import QuestionGeneration
from pdfrw import PdfReader
import fitz  # PyMuPDF

def pdf2text(file_path: str, file_exten: str) -> str:
    """Converts a given file to text content"""
    _content = ''

    if file_exten == 'pdf':
        try:
            pdf_document = fitz.open(file_path)
            num_pages = pdf_document.page_count
            for page_num in range(num_pages):
                page = pdf_document[page_num]
                _content += page.get_text()
            pdf_document.close()
            print('PDF operation done!')
        except Exception as e:
            print('Error:', e)

    elif file_exten == 'txt':
        try:
            with open(file_path, 'r') as txt_file:
                _content = txt_file.read()
                print('TXT operation done!')
        except Exception as e:
            print('Error:', e)

    return _content

def txt2questions(doc: str, n: int, o=4) -> dict:
    """ Get all questions and options """

    qGen = QuestionGeneration(n, o)
    q = qGen.generate_questions_dict(doc)
    for i in range(len(q)):
        temp = []
        for j in range(len(q[i + 1]['options'])):
            temp.append(q[i + 1]['options'][j + 1])
        # print(temp)
        q[i + 1]['options'] = temp
    return q