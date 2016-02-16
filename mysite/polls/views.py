from django.http import HttpResponse


def index(request):
    response = HttpResponse("Hello, world. You're at the polls index.")
    response.set_cookie("x-server-name", "django-dev-webserver")
    return response