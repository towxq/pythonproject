# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from common import models
# Create your views here.

def index(request):
    # return HttpResponse("hello world!")
    # string = "你好！"
    # list = ["微信","腾讯","百度","阿里"]
    # dict = {"微信":"30000","腾讯":"35000","阿里":"40000"}
    # dict1 = {"a": string, "b": list,"c": dict}
    # # user = User.object.get(id='1234edser56rte345678')
    temp = models.UserInfo.objects.all()
    return render(request, 'home.html',{"data":temp})


def index2(request):
    # return HttpResponse("hello world!")
    # string = "你好！"
    # list = ["微信","腾讯","百度","阿里"]
    # dict = {"微信":"30000","腾讯":"35000","阿里":"40000"}
    # dict1 = {"a": string, "b": list,"c": dict}
    # # user = User.object.get(id='1234edser56rte345678')
    if request.method =="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        temp = {"username":username,"password":password}
    return render(request, 'home2.html',{"data":temp})

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))

def add2(request, a, b):
    c = int(a)+int(b)
    return HttpResponse(str(c))