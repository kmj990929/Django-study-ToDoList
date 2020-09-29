# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 08:48:00 2020

@author: kmj99
"""

from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('createTodo/', views.createTodo)
]