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

        # TODO: Catch unique constraint violation and report on the UI
        try:
            User.objects.create_user(username, email, password);
        except IntegrityError:
            return HttpResponseRedirect("/DevNewsAggregatorConfiguration/register/");
        return HttpResponseRedirect("http://127.0.0.1/DevNewsAggregator/index.php")
    else:
        return render(request, "DevNewsAggregatorConfiguration/register.html")