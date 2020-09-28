from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def sighnupuser(request):
    if request.mathod == 'GET':
        return render (request, 'todo/sighnupuser.html', {'form':UserCreationForm()})
    else:
        User.objects.create_user()
