# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 07:24:26 2020

@author: kmj99
"""

from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('createTodo/', views.createTodo, name = 'createTodo'),
    path('deleteTodo/', views.deleteTodo, name = 'deleteTodo')
]