# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import uuid
from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
from projectdemo.models import Project
from userdemo.util import FeedbackMessage


def indexpage(request):
    project = Project.objects.all()
    return render(request,'indexpage.html',{'projects':project})

def projectlist(request,page,pagesize):
     page = int(page)
     pagesize = int(pagesize)
     if page==1:
         began = 0
         end = pagesize
     else:
         began = (page-1)*pagesize
         end =  began+pagesize
     project = Project.objects.all()[began:end]
     total = Project.objects.count()
     if total%pagesize==0:
         counts = total/pagesize
     else:
         counts = total/pagesize+1
     return render(request,'projectlist.html',
                   {'projects':project,'counts':counts,'page':page,'pagesize':pagesize}
     )

def addproject(request):
    projectname = request.POST.get('projectname')
    projecturl = request.POST.get('projecturl')
    projectdesc = request.POST.get('projectdesc')
    id = uuid.uuid4()
    try:
        Project.objects.create(id=id,projectname=projectname,projecturl=projecturl,projectdesc=projectdesc)
        return_json = FeedbackMessage(True,"11111", "添加成功",)
    except Exception:
        return_json = FeedbackMessage(True,"77779", "添加失败",)
    return HttpResponse(json.dumps(return_json.dict()), content_type='application/json')

def delproject(request):
    projectid = request.POST.get('projectid')
    try:
        Project.objects.get(id=projectid).delete()
        return_json =  return_json = FeedbackMessage(True,"11111", "删除成功",)
    except Exception:
        return_json =  return_json = FeedbackMessage(True,"77779", "删除失败",)
    return HttpResponse(json.dumps(return_json.dict()), content_type='application/json')