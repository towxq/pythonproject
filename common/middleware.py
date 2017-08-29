import uuid
from django.core.cache import cache
from django.http import request, HttpResponseRedirect


try:
    from django.utils.deprecation import MiddlewareMixin  # Django 1.10.x
except ImportError:
    MiddlewareMixin = object  # Django 1.4.x - Django 1.9.x

class SimpleMiddleware(MiddlewareMixin):
    def process_request(self, request):
        sessionid = request.COOKIES.get('wxq_django_sessionid','')
        if sessionid != '' and request.path != "user/login":
            pass
            # if cache.get(sessionid) is None:
            #     return HttpResponseRedirect('/')
        return None

    def process_response(self, request, response):
        sessionid = request.COOKIES.get('wxq_django_sessionid','')
        if sessionid == '':
            response.set_cookie("wxq_django_sessionid",uuid.uuid4(),7200)
        return response