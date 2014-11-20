from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                return __handle_login_success()
            else:
                return HttpResponseRedirect("/DevNewsAggregatorConfiguration/login/?authentication_failure=account_disabled&username=" + username)
        else:
            return HttpResponseRedirect("/DevNewsAggregatorConfiguration/login/?authentication_failure=authentication_failure&username=" + username)
    else:
        return render(request, "DevNewsAggregatorConfiguration/login.html", {
            'username': request.GET.get('username'),
            'authentication_failure': __get_login_failure_error_message(request.GET.get('authentication_failure'))
        })


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        try:
            User.objects.create_user(username, email, password)
        except IntegrityError:
            return HttpResponseRedirect("/DevNewsAggregatorConfiguration/register/?username_error=duplicate&username=" + username + "&email=" + email)

        return login(request)
    else:
        return render(request, "DevNewsAggregatorConfiguration/register.html", {
            'email': request.GET.get('email'),
            'username': request.GET.get('username'),
            'username_error': __get_registration_error_message_for_username_field(request.GET.get('username_error'))
        })


def __get_registration_error_message_for_username_field(username_error):
    if username_error == 'duplicate':
        return "This username has already been chosen."


def __get_login_failure_error_message(authentication_failure):
    if authentication_failure == 'account_disabled':
        return "Your account has been disabled!"
    elif authentication_failure == 'authentication_failure':
        return "The username and password were incorrect."


def __handle_login_success():
    return __redirect_to_news_feed()


def __redirect_to_news_feed():
    # TODO: Redirect to content surrounded by top/side nav
    return HttpResponseRedirect("http://127.0.0.1/DevNewsAggregator/index.php")