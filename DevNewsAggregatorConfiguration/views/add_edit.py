from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from DevNewsAggregatorConfiguration.models import ScrapingStrategy, HtmlContentForm, HtmlContent
from DevNewsAggregatorConfiguration.views.view_utils import render_metronic_navigation_template_extension


@login_required
def duplicate(request, html_content_id):
    if request.method == 'GET':
        instance = get_object_or_404(HtmlContent, id=html_content_id)
        instance.id = None
        instance.name = None
        form = HtmlContentForm(None, instance=instance)
        return __render_add_edit_form(request, form)
    else:
        return new_html_content(request)


@login_required
def new_html_content(request):
    if request.method == 'POST':
        form = HtmlContentForm(request.POST)
        if form.is_valid():
            instance = form.save()

            instance.users.add(request.user)
            instance.save()

            return __redirect_after_successful_save(instance)
    else:
        form = HtmlContentForm()
    return __render_add_edit_form(request, form)


@login_required
def get_or_update_html_content(request, html_content_id):
    instance = get_object_or_404(HtmlContent, id=html_content_id)
    form = HtmlContentForm(request.POST or None, instance=instance)
    if request.method == 'POST' and form.is_valid():
        instance = form.save()
        return __redirect_after_successful_save(instance)
    return __render_add_edit_form(request, form)


def __redirect_after_successful_save(html_content_instance):
    return HttpResponseRedirect("/DevNewsAggregatorConfiguration/html_content/%d/" % html_content_instance.id)


def __render_add_edit_form(request, form):
    return render_metronic_navigation_template_extension(request, "DevNewsAggregatorConfiguration/add_edit.html", form=form)
