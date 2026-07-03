from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_employee, name='register'),
    path('id-card/<int:id>/', views.id_card, name='id_card'),
    path('mark-attendance/', views.mark_attendance_page, name='mark_attendance'),
    path('process-attendance/<str:emp_id>/', views.process_attendance, name='process_attendance'),
    path('att-mang/', views.home, name='home'),
    path('attendance/', views.attendance_list, name='attendance_list'),
    path('attendance/export/', views.export_attendance_excel, name='export_attendance'),
    path('view-employees/', views.view_employees, name='view_employees'),

]
