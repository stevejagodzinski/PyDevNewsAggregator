from urllib.parse import urlencode
from django.http import HttpResponseRedirect
import urllib.request as urllib2
from DevNewsAggregatorConfiguration.models import HtmlContent
from DevNewsAggregatorConfiguration.models import QuickSidebarItem


def redirect_to_news_feed(request):
    return HttpResponseRedirect("/DevNewsAggregatorConfiguration/")


def get_username_for_top_nav_menu(request):
    return request.user.get_username() if request.user.is_authenticated() else 'Anonymous'


def get_news_feed(request, name=None):
    url = "http://127.0.0.1/DevNewsAggregator/index.php?%s" % __build_query_params({'name': name, 'userid': request.user.id})
    http_response = urllib2.build_opener().open(urllib2.Request(url))
    response_bytes = http_response.read()
    html = response_bytes.decode('utf-8')
    body = html.split('<body>')[1].split('</body>')[0].strip().replace('\\n', '').replace('\\r', '').replace('\\t', '')
    return body


def get_quick_sidebar_list(request):
    all_available_news_sources = __get_available_news_sources()
    my_news_sources = __get_my_news_sources(request)
    return __build_quick_sidebar_list(all_available_news_sources, my_news_sources)


def __build_quick_sidebar_list(all_news_sources, my_news_sources):
    # Execute the query now, so we don't hit the db every time we iterate over all_news_sources
    my_news_sources = my_news_sources.values()
    return [QuickSidebarItem(news_source.id, news_source.name, my_news_sources.filter(id=news_source.id).count() > 0) for news_source in all_news_sources]


def __build_query_params(parameter_map):
    nulls_removed = dict((k, v) for k, v in parameter_map.items() if v is not None)
    return urlencode(nulls_removed)


def __get_available_news_sources():
    return HtmlContent.objects.filter(enabled=1).order_by('name')


def __get_my_news_sources(request):
    if request.user.is_authenticated():
        return HtmlContent.objects.filter(users=request.user)
    else:
        return HtmlContent.objects.all()
