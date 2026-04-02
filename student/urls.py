from django.urls import path
from . import views

from django.shortcuts import redirect

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('teacher-dashboard.html', lambda req: redirect('dashboard')),
    path('add/', views.add_student, name='add_student'),
    path('students/<str:student_id>/', views.view_student, name='view_student'),
    path('edit/<str:student_id>/', views.edit_student, name='edit_student'),
    path('delete/<str:student_id>/', views.delete_student, name='delete_student'),
    path('export/json/', views.export_students_json, name='export_students_json'),
]
