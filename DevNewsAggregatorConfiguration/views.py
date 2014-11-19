from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        try:
            User.objects.create_user(username, email, password);
        except IntegrityError:
            return HttpResponseRedirect("/DevNewsAggregatorConfiguration/register/?username_error=duplicate&username=" + username + "&email=" + email);
        return HttpResponseRedirect("http://127.0.0.1/DevNewsAggregator/index.php")
    else:
        return render(request, "DevNewsAggregatorConfiguration/register.html", {
            'email': request.GET.get('email'),
            'username': request.GET.get('username'),
            'username_error': __get_error_message_for_username_field(request.GET.get('username_error'))
        })

def __get_error_message_for_username_field(username_error) :
    if username_error == 'duplicate':
        return "This username has already been chosen."