from django.urls import path
from . import views

urlpatterns = [
    path('', views.hr_atend_home),
]
