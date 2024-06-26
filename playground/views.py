import requests
from django.core.cache import cache
from django.core.mail import (BadHeaderError, EmailMessage, mail_admins,
                              send_mail)
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
from templated_mail.mail import BaseEmailMessage

from .tasks import notify_customers


class HelloView(APIView):
    @method_decorator(cache_page(5*60))
    def get(self, request):
        response = requests.get('https://httpbin.org/delay/2')
        data = response.json()
        # notify_customers.delay("Hello")
        return render(request, 'hello.html', {'name': data})




# @cache_page(5*60)
# def say_hello(request):
#     # try:
#         # send_mail('subject', 'message', 'd.blakaj1108@gmail.com', ['d.blakaj1108@gmail.com'])
#         #mail_admins('subject', 'message', html_message='message')
#         # message = EmailMessage('subject', 'message', 'from@testbuy.com',['d.blakaj1108@gmail.com'])
#         # message.attach_file('playground/static/images/dog.png')
#         # message.send()
#     #     message = BaseEmailMessage(template_name='emails/hello.html', context={'name': 'Test'})
#     #     message.send(['test@gmail.com'])
#     # except BadHeaderError:
#     #     pass
#     # key = 'httpbin_resultt'
#     # if cache.get(key) is None:
#     #     print("Entered in if")
#     response = requests.get('https://httpbin.org/delay/2')
#     data = response.json()
#     # notify_customers.delay("Hello")
#     return render(request, 'hello.html', {'name': data})

