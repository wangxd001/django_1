# -*- coding:utf-8 -*-
"""
Author: wangxd
Date: 2022/7/21
"""
from django.urls import path
from book.views import shop, set_session
from django.urls.converters import register_converter


# 自定义转换器
class MobileConverter:
    # 验证没有问题的数据，给视图函数
    regex = '1[3-9]\d{9}'

    def to_python(self, value):
        return value


# 先注册转换器，才能在后面使用
register_converter(MobileConverter, 'phone')

urlpatterns = [
    # <转换器名字:变量名>
    # 转换器会对变量数据进行正则校验
    path('<int:city>/<phone:mobile>/', shop),
    path('set_session/<name>/', set_session),
]
