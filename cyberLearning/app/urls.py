from django.urls import path
from .views import render_module, home

urlpatterns = [
    path('', home, name="home"),
    path('module/', render_module, name="render_module"),
]
