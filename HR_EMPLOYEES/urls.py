from django.urls import path
from . import views

urlpatterns = [
    path('', views.hr_emp_home),
]
