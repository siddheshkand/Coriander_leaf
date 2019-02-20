from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def home(request):
    if request.method == "POST":
        print(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        find_us = request.POST.get('find-us')
        message = request.POST.get('message')
        subject = "Mail from the website www.thecorianderleaf.in by {}".format(name)

        html_msg = "<h1>{}</h1>".format(message)
        html_msg += "<br>"
        html_msg += "<b>They came to know us by {}</b>".format(find_us)
        html_msg += "<br>"
        html_msg += "<b>Their email address {}</b>".format(email)
        html_msg += "<br>"
        html_msg += "<b>Their name {}</b>".format(name)

        from_email = settings.EMAIL_HOST_USER
        to_list = [
            # 'siddkand@gmail.com',
            'hrishitcl@gmail.com',
            'amruttcl@gmail.com',
            'hemantchavantcl@gmail.com',
            'ashishcoriander@gmail.com',
        ]
        # send_mail(subject,message,from_email,to_list,fail_silently=true)
        send_mail(subject=subject, message="", from_email=from_email, recipient_list=to_list, fail_silently=True,
                  html_message=html_msg)
        mail_send_msg = "mail sent successfully"
        return render(request, 'copy.html', {"mail_send_msg": mail_send_msg})
    
    return render(request, "copy.html")
