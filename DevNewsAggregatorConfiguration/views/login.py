from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from DevNewsAggregatorConfiguration.views.view_utils import __redirect_to_news_feed


def app_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return __handle_login_success(request)
            else:
                return HttpResponseRedirect(
                    "/DevNewsAggregatorConfiguration/login/?authentication_failure=account_disabled&username=" + username)
        else:
            return HttpResponseRedirect(
                "/DevNewsAggregatorConfiguration/login/?authentication_failure=authentication_failure&username=" + username)
    else:
        return render(request, "DevNewsAggregatorConfiguration/login.html", {
            'username': request.GET.get('username'),
            'authentication_failure': __get_login_failure_error_message(request.GET.get('authentication_failure'))
        })


def app_logout(request):
    logout(request)
    return __redirect_to_news_feed(request)


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        try:
            User.objects.create_user(username, email, password)
        except IntegrityError:
            return HttpResponseRedirect(
                "/DevNewsAggregatorConfiguration/register/?username_error=duplicate&username=" + username + "&email=" + email)

        return app_login(request)
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


def __handle_login_success(request):
    return __redirect_to_news_feed(request)