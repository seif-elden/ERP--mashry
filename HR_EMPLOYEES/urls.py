from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.login.as_view()),



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
    
    path('list-weakly-leave/', views.List_Weakly_leave.as_view()),
    path('add-weakly-leave/', views.AddWeakly_leave.as_view()),
    path('delete-weakly-leave/<pk>/', views.DeleteWeakly_leave.as_view()),


    path('list-yearly-leave/', views.List_yearly_leave.as_view()),
    path('add-yearly-leave/', views.Add_yearly_leave.as_view()),
    path('delete-yearly-leave/<pk>/', views.Delete_yearly_leave.as_view()),
    path('edit-yearly-leave/<pk>/', views.Edit_yearly_leave.as_view()),

    path('add-leave-request/', views.add_leave_request.as_view()),
    path('list-avuser-leave/', views.list_avfruser_leave_request.as_view()),
    path('list-leave-request-user/', views.list_leave_request_user.as_view()),
    path('delete-leave-request-user/<pk>/', views.delete_leave_request_user.as_view()),
    path('list-leave-request-managment/', views.list_leave_request_managment.as_view()),
    path('response-to-leave-request-managment/<pk>/', views.response_to_leave_request_managment.as_view()),


    path('user-attendance/', views.user_attendance.as_view()),
    path('list-user-attendance-days/<pk>/', views.list_user_attendance_days.as_view()),




    path('available-managments/', views.available_managements.as_view()),


    path('available-equipment/', views.AllEquipment.as_view()),
    path('user-equipment/<pk>/', views.user_equipment.as_view()),

    path('add-equipment/', views.AddEquipment.as_view()),

    path('edit-equipment/<pk>/', views.edit_equipment.as_view()),
    path('add-user-to-equipment/', views.add_user_to_equipment.as_view()),
    path('delete-user-from-equipment/', views.delete_user_from_equipment.as_view()),

    path('delete-equipment/<pk>/', views.delete_equipment.as_view()),





    
]
