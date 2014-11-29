from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from DevNewsAggregatorConfiguration.models import ScrapingStrategy, HtmlContentForm, HtmlContent
from DevNewsAggregatorConfiguration.views import view_utils


def new_html_content(request):
    if request.method == 'POST':
        form = HtmlContentForm(request.POST)
        if form.is_valid():
            instance = form.save()
            return __redirect_after_successful_save(instance)
    else:
        form = HtmlContentForm()
    return __render_add_edit_form(request, form)


def get_or_update_html_content(request, html_content_id):
    instance = get_object_or_404(HtmlContent, id=html_content_id)
    form = HtmlContentForm(request.POST or None, instance=instance)
    if request.method == 'POST' and form.is_valid():
        instance = form.save()
        return __redirect_after_successful_save(instance)
    return __render_add_edit_form(request, form)


def __redirect_after_successful_save(html_content_instance):
    return HttpResponseRedirect("DevNewsAggregatorConfiguration/html_content/%d/" % html_content_instance.id)


def __render_add_edit_form(request, form):
    return render(request, "DevNewsAggregatorConfiguration/add_edit.html", {
        'authenticated': request.user.is_authenticated(),
        'form': form,
        'scraping_strategies': ScrapingStrategy.get_all_sorted_by_display_string(),
        'username': view_utils.get_username_for_top_nav_menu(request)
    })