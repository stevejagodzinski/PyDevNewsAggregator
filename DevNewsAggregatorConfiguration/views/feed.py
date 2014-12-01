from django.shortcuts import render
from DevNewsAggregatorConfiguration.models import HtmlContent
from DevNewsAggregatorConfiguration.models import QuickSidebarItem
from DevNewsAggregatorConfiguration.views import view_utils


def feed(request):

    feed_body = __load_aggregated_news_feed(request)

    return render(request, "DevNewsAggregatorConfiguration/dev_news.html", {
        'available_news_sources': view_utils.get_quick_sidebar_list(request),
        'authenticated': request.user.is_authenticated(),
        'content_body': feed_body,
        'username': view_utils.get_username_for_top_nav_menu(request)
    })


def __load_aggregated_news_feed(request):
    return view_utils.get_news_feed(request)