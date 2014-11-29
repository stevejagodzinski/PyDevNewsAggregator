from django.shortcuts import render
from DevNewsAggregatorConfiguration.models import ScrapingStrategy, HtmlContentForm
from DevNewsAggregatorConfiguration.views import view_utils


def new_html_content(request):
    if request.method == 'POST':
        form = HtmlContentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = HtmlContentForm()

    return render(request, "DevNewsAggregatorConfiguration/add_edit.html", {
            'authenticated': request.user.is_authenticated(),
            'form': form,
            'scraping_strategies': ScrapingStrategy.get_all_sorted_by_display_string(),
            'username': view_utils.get_username_for_top_nav_menu(request)
        })