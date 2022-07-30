from django.shortcuts import render, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

# Create your views here.


def shop(request, city, mobile):
    # print(request.META)
    response = HttpResponse('OK')
    response['city'] = city
    response['mobile'] = mobile
    return response


def set_cookie(request, name):
    response = HttpResponse(f'Hello, {name}')
    response.set_cookie('username', name)
    return response


def get_cookie(request):
    username = request.COOKIES.get('username')
    return HttpResponse(username)


def set_session(request, name):
    u_id = 1
    request.session['u_id'] = u_id
    request.session['username'] = name
    return HttpResponse('Set session success.')


class OrderView(LoginRequiredMixin, View):
    def get(self, request):
        return HttpResponse('GET 订单页面')

    def post(self, request):
        return HttpResponse('POST 订单页面')
