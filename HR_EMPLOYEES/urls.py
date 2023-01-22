from django.urls import path
from . import views

urlpatterns = [
    path('somedata/', views.SomEmpData),
    path('alldata/<pk>/', views.AllEmpData),
    path('departments/', views.available_department),
    path('add-job/', views.add_job),
    path('add-department/', views.add_department),
         
]
