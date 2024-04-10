from django.urls import path

from . import views


app_name = "quotes"

urlpatterns = [
    path('', views.main, name="root"),
    path('<int:page>/', views.main, name="root_paginate"),
    path('add_author/', views.add_author, name='add_author'), 
    path('authors/<int:author_id>/', views.author_details, name="author_details"), #было  name="root"
    path('add_quote/', views.add_quote, name='add_quote'), 
    path('quotes/', views.main, name='quotes'),    
]