from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
import urllib.request as urllib2
from DevNewsAggregatorConfiguration.models import HtmlContent
from DevNewsAggregatorConfiguration.models import QuickSidebarItem


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


def feed(request):
    all_available_news_sources = __get_available_news_sources()
    my_news_sources = __get_my_news_sources(request)
    quick_sidebar_news_sources = __build_quick_sidebar_list(all_available_news_sources, my_news_sources)
    feed_body = __load_aggregated_news_feed()

    return render(request, "DevNewsAggregatorConfiguration/dev_news.html", {
        'available_news_sources': quick_sidebar_news_sources,
        'authenticated': request.user.is_authenticated(),
        'content_body': feed_body,
        'username': request.user.get_username() if request.user.is_authenticated() else 'Anonymous'
    })


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

        return login(request)
    else:
        return render(request, "DevNewsAggregatorConfiguration/register.html", {
            'email': request.GET.get('email'),
            'username': request.GET.get('username'),
            'username_error': __get_registration_error_message_for_username_field(request.GET.get('username_error'))
        })


def __build_quick_sidebar_list(all_news_sources, my_news_sources):
    # Execute the query now, so we don't hit the db every time we iterate over all_news_sources
    my_news_sources = my_news_sources.values()
    return [QuickSidebarItem(news_source.id, news_source.name, my_news_sources.filter(id=news_source.id).count() > 0) for news_source in all_news_sources]


def __get_available_news_sources():
    return HtmlContent.objects.filter(enabled=1).order_by('name')


def __get_my_news_sources(request):
    if request.user.is_authenticated():
        return HtmlContent.objects.filter(users=request.user)
    else:
        return HtmlContent.objects.all()


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


def __load_aggregated_news_feed():
    # TODO: Don't convert the whole thing to a string. Remove need to remove \r\n & \t ?
    html = str(urllib2.build_opener().open(urllib2.Request("http://127.0.0.1/DevNewsAggregator/index.php")).read())
    body = html.split('<body>')[1].split('</body>')[0].strip().replace('\\n', '').replace('\\r', '').replace('\\t', '')
    return body


def __redirect_to_news_feed(request):
    return HttpResponseRedirect("/DevNewsAggregatorConfiguration/")