from django.http import HttpResponseRedirect


def redirect_to_news_feed(request):
    return HttpResponseRedirect("/DevNewsAggregatorConfiguration/")


def get_username_for_top_nav_menu(request):
    return request.user.get_username() if request.user.is_authenticated() else 'Anonymous'