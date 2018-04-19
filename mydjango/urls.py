"""mydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from common import views as common_views
from mydjango.index import index
from projectdemo.views import indexpage, projectlist, addproject, delproject
from userdemo.views import login, userlist, adduser, deluser

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^user/login',login),
    url(r'^user/index',indexpage),
    url(r'^user/addprojrct',addproject),
    url(r'^user/deluser',deluser),
    url(r'^user/delproject',delproject),
    url(r'^user/adduser',adduser),
    url(r'^user/projectlist/(\d+)/(\d+)/$',projectlist),
    url(r'^user/userlist/(\d+)/(\d+)/$',userlist),
    # url(r'^index/', common_views.index),
    # url(r'^index2/', common_views.index2),
    # url(r'^add/$', common_views.add, name='add'),
    # url(r'^add/(\d+)/(\d+)/$', common_views.add2, name='add2'),
]
