from urllib.parse import urlencode
from django.http import HttpResponseRedirect
import urllib.request as urllib2


def redirect_to_news_feed(request):
    return HttpResponseRedirect("/DevNewsAggregatorConfiguration/")


def get_username_for_top_nav_menu(request):
    return request.user.get_username() if request.user.is_authenticated() else 'Anonymous'


def get_news_feed(request, name=None):
    url = "http://127.0.0.1/DevNewsAggregator/index.php?%s" % __build_query_params({'name': name, 'userid': request.user.id})
    html = str(urllib2.build_opener().open(urllib2.Request(url)).read())
    body = html.split('<body>')[1].split('</body>')[0].strip().replace('\\n', '').replace('\\r', '').replace('\\t', '')
    return body


def __build_query_params(parameter_map):
    nulls_removed = dict((k, v) for k, v in parameter_map.items() if v is not None)
    return urlencode(nulls_removed)