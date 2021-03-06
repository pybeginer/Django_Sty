import json

from django.shortcuts import render
from django.http import HttpResponse


def say(request):

    return HttpResponse("hello world")


def talk(req):

    return HttpResponse("oh on")


# 获取路径参数,包括:位置参数和关键字参数
def test(request, year, city):

    print(year, city)
    return HttpResponse("天气")


# 获取查询参数的方法
def string_query(req):
    a = req.GET.get("a")
    # a1 = req.GET.getlist("a")
    b = req.GET.get("b")
    a2 = req.GET.getlist("a")

    return HttpResponse("")


# 获取请求体中的表单数据
def req_body(req):

    hobby = req.POST.get('hobby')
    hobby_list = req.POST.getlist('hobby')
    name = req.POST.get('name')

    return HttpResponse('req_body')


# 获取请求体中的非表单数据
def body_json(req):
    data_bit = req.body
    data_str = data_bit.decode()
    data_json = json.loads(data_str)

    return HttpResponse("body_json")


def request_head(req):

    content_type = req.META.get('CONTENT_TYPE')
    print(content_type)
    print(req.user, req.method)
    return HttpResponse("req_head")