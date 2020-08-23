from django.contrib import admin
from django.urls import path

from . import views

app_name = 'mainview'
urlpatterns = [
    path('', views.IndexView.as_view(),name="index"),
    path('test/', views.test_module,name="test_module"),
]
