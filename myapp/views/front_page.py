from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    return render(request, "frontPage/home.html")

def about(request):
    return render(request, "frontPage/about.html")

def contact(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        country = request.POST.get('country')
        from_message = request.POST.get('message')
        
        send_mail(
            subject="New Message from Contact Form",
            message=f'Name: {first_name} {last_name}\nEmail: {email}\nCountry: {country}\n\nMessage: {from_message}',
            from_email=settings.EMAIL_FROM_USER,
            recipient_list=[settings.EMAIL_FROM_USER],
            fail_silently=False,
        )
        messages.add_message(request, messages.SUCCESS,
                                         'We sent you an email to verify your account')  
        return redirect('contact') 
            
    context = {
        'page': 'contact'
    }
    return render(request, "frontPage/contact.html", context)