# -*- coding:utf-8 -*-
"""
Author: wangxd
Date: 2022/7/30
"""
from django.utils.deprecation import MiddlewareMixin


class MyMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        print('每次请求前 都会调用')
        username = request.COOKIES.get('username')
        if username is None:
            print('没有用户信息')
        else:
            print('有用户信息')

    def process_response(self, request, response):
        print('每次响应前 都会调用')
        return response
