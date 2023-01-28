from django.urls import path
from . import views

urlpatterns = [
    path('somedata/', views.SomEmpData.as_view()),


    path('emp-data/<pk>/', views.AllEmpData.as_view()),
    path('update-emp/<pk>/', views.EditEmpData.as_view()),
    path('delete-emp/<pk>/', views.DeleteEmpData.as_view()),
    path('add-emp/', views.AddEmp.as_view()),
         

    path('departments/', views.available_department.as_view()),
    path('add-department/', views.add_department.as_view()),
    path('delete-department/<pk>/', views.delete_department.as_view()),
    path('edit-department/<pk>/', views.edit_department.as_view()),
                                                         
    path('add-job/', views.add_job.as_view()),
    path('available-jobs/', views.available_jobs.as_view()),
    path('delete-job/<pk>/', views.delete_job.as_view()),
    path('edit-job/<pk>/', views.edit_job.as_view()),

    path('add-leave/', views.add_leave.as_view()),
    path('available-leaves/', views.available_leave.as_view()),
    path('delete-leave/<pk>/', views.delete_leave.as_view()),
    path('edit-leave/<pk>/', views.edit_leave.as_view()),

    path('available-managments/', views.available_managements.as_view()),


    
]
