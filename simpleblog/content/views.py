from django.shortcuts import render


def index(request):
    # TODO: generic view?
    return render(request, "content/index.html")
