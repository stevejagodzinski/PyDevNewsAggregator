from django.shortcuts import render
from DevNewsAggregatorConfiguration.models import HtmlContent
from DevNewsAggregatorConfiguration.models import QuickSidebarItem
from DevNewsAggregatorConfiguration.views import view_utils


def feed(request):
    all_available_news_sources = __get_available_news_sources()
    my_news_sources = __get_my_news_sources(request)
    quick_sidebar_news_sources = __build_quick_sidebar_list(all_available_news_sources, my_news_sources)
    feed_body = __load_aggregated_news_feed(request)

    return render(request, "DevNewsAggregatorConfiguration/dev_news.html", {
        'available_news_sources': quick_sidebar_news_sources,
        'authenticated': request.user.is_authenticated(),
        'content_body': feed_body,
        'username': view_utils.get_username_for_top_nav_menu(request)
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


def __load_aggregated_news_feed(request):
    return view_utils.get_news_feed(request)
    # return "";