from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            # TODO: Redirect properly once servers are integrated
            return HttpResponseRedirect("http://127.0.0.1/DevNewsAggregator/index.php")
    else:
        form = UserCreationForm()
    return render(request, "DevNewsAggregatorConfiguration/register.html", {
        'form': form,
    })