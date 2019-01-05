# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import hashlib
from io import BytesIO
import json
import uuid
from django.core.cache import cache
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render

# Create your views here.

from userdemo.models import User
from userdemo.util import FeedbackMessage
from userdemo.smscodeutil import create_validate_code


def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        user = User.objects.get(username=username)
        md5 = hashlib.md5()
        # md5.update(password)
        md5password = md5.hexdigest()
        if user.password != md5password:
            return_json = FeedbackMessage(True,"77779", "密码错误",)
        else:
            cache.set(request.COOKIES.get('wxq_django_sessionid',''),json.dumps(user.username))
            return_json = FeedbackMessage(True,"11111", "登陆成功",)
    except Exception:
        return_json = FeedbackMessage(True,"77779", "用户名不存在",)
    return HttpResponse(json.dumps(return_json.dict()), content_type='application/json')


def check_code(request):
    stream = BytesIO()
    img, code = create_validate_code()
    img.save(stream,'GIF')
    request.session['smscode'] = code
    return HttpResponse(stream.getvalue())

    # mstream = StringIO.StringIO()
    # validate_code = create_validate_code()
    # img = validate_code[0]
    # img.save(mstream, "GIF")
    # return HttpResponse(mstream.getvalue())



def userlist(request,page,pagesize):
     page = int(page)
     pagesize = int(pagesize)
     if page==1:
         began = 0
         end = pagesize
     else:
         began = (page-1)*pagesize
         end =  began+pagesize
     user = User.objects.all()[began:end]
     total = User.objects.count()
     if total%pagesize==0:
         counts = total/pagesize
     else:
         counts = total/pagesize+1
     return render(request,'userlist.html',
                   {'users':user,'counts':counts,'page':page,'pagesize':pagesize}
     )

def adduser(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    md5 = hashlib.md5()
    md5.update(password)
    password = md5.hexdigest()
    telnumber = request.POST.get('telnumber')
    userrole = request.POST.get('userrole')
    id = uuid.uuid4()
    try:
        User.objects.create(id=id,username=username,password=password,telnumber=telnumber,userrole=userrole)
        return_json = FeedbackMessage(True,"11111", "添加成功",)
    except Exception:
        return_json = FeedbackMessage(True,"77779", "添加失败",)
    return HttpResponse(json.dumps(return_json.dict()), content_type='application/json')

def deluser(request):
    userid = request.POST.get('userid')
    try:
        User.objects.get(id=userid).delete()
        return_json = FeedbackMessage(True,"11111", "删除成功",)
    except Exception:
        return_json = FeedbackMessage(True,"77779", "删除失败",)
    return HttpResponse(json.dumps(return_json.dict()), content_type='application/json')

def updateuser(request):
    password = request.POST.get('password')
    username = request.POST.get('username')
    try:
         User.objects.filter(username=username).update(password=password)
         return_json = FeedbackMessage(True,"11111", "修改成功",)
    except Exception:
         return_json = FeedbackMessage(True,"77779", "修改失败",)
    return HttpResponse(json.dumps(return_json.dict()), content_type='application/json')