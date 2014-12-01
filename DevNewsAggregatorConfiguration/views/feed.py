from django.shortcuts import render
from DevNewsAggregatorConfiguration.views.view_utils import render_metronic_navigation_template_extension, get_news_feed


def feed(request):
    feed_body = __load_aggregated_news_feed(request)
    return render_metronic_navigation_template_extension(request, "DevNewsAggregatorConfiguration/dev_news.html", content_body=feed_body)


def __load_aggregated_news_feed(request):
    return get_news_feed(request)