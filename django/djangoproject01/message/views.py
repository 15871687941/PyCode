from django.shortcuts import render
from .models import UserMessage

# Create your views here.


def get_form(request):
    message = UserMessage.objects.filter(name='赵永康', address='湖北襄阳')[0]
    return render(request, 'message_form.html', {'my_message': message})

