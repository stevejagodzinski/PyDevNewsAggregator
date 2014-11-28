from django.shortcuts import render


def new_html_content(request):
    return render(request, "DevNewsAggregatorConfiguration/add_edit.html", {
        'authenticated': request.user.is_authenticated(),
        'username': request.user.get_username() if request.user.is_authenticated() else 'Anonymous'
    })