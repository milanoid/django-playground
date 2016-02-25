from django.http import HttpResponse


def index(request):
    response = HttpResponse("Hello, world. You're at the polls index.")
    response.set_cookie("x-server-name", "django-dev-webserver")
    return response


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def result(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)