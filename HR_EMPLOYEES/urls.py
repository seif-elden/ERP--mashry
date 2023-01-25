from django.urls import path
from . import views

urlpatterns = [
    path('somedata/', views.SomEmpData),
    path('alldata/<pk>/', views.AllEmpData),
    path('departments/', views.available_department),
    path('add-job/', views.add_job.as_view()),
    path('add-department/', views.add_department.as_view()),
    path('available-jobs/', views.available_jobs),

]
