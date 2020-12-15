from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]# -*- coding: utf-8 -*-

