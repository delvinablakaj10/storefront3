from django.core.mail import (BadHeaderError, EmailMessage, mail_admins,
                              send_mail)
from django.shortcuts import render
from templated_mail.mail import BaseEmailMessage
from .tasks import notify_customers


def say_hello(request):
    # try:
        # send_mail('subject', 'message', 'd.blakaj1108@gmail.com', ['d.blakaj1108@gmail.com'])
        #mail_admins('subject', 'message', html_message='message')
        # message = EmailMessage('subject', 'message', 'from@testbuy.com',['d.blakaj1108@gmail.com'])
        # message.attach_file('playground/static/images/dog.png')
        # message.send()
    #     message = BaseEmailMessage(template_name='emails/hello.html', context={'name': 'Test'})
    #     message.send(['test@gmail.com'])
    # except BadHeaderError:
    #     pass

    notify_customers.delay("Hello")
    return render(request, 'hello.html', {'name': 'Test'})

