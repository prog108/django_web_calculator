# moja_app/urls.py
from django.urls import path, re_path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.index, name='index'),
    path('converter/', views.konverter, name='konverter'),
    path('sample/', TemplateView.as_view(template_name='new_app/sample.html'), name='sample'), #NOTICE FOLDER_NAME IN TEMPLATE_NAME
    #path('sample/', views.sample_view, name='sample'),

    #WE USE TemplateView.as_view() WHEN THE PAGE IS TOTALLY STATIC. NO NEED TO CHANGE view.py NEITHER.
]
