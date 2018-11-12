from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def say(request):

    return HttpResponse("hello world")


def talk(req):

    return HttpResponse("oh on")


def test(request, year, city):

    print(year, city)
    return HttpResponse("天气")


