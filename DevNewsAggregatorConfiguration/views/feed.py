from DevNewsAggregatorConfiguration.views.view_utils import render_metronic_navigation_template_extension


def feed(request):
    feed_body = '<div class="content"></div>'
    return render_metronic_navigation_template_extension(request, "DevNewsAggregatorConfiguration/dev_news.html", content_body=feed_body)
