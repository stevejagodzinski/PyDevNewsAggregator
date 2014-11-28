from django.http import HttpResponseRedirect


def __redirect_to_news_feed(request):
    return HttpResponseRedirect("/DevNewsAggregatorConfiguration/")