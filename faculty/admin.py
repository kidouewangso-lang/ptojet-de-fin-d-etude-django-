from django.contrib import admin
from .models import Department, Teacher, Subject

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'head_of_department', 'started_date', 'student_capacity')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'teacher_id', 'department', 'mobile_number')

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject_id', 'department', 'teacher')

from .models import Holiday, TimeTable, Exam, ExamResult

@admin.register(Holiday)
class HolidayAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date')

@admin.register(TimeTable)
class TimeTableAdmin(admin.ModelAdmin):
    list_display = ('subject', 'teacher', 'day_of_week', 'start_time', 'end_time', 'room_no')
    list_filter = ('department', 'day_of_week')

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'date', 'start_time')

@admin.register(ExamResult)
class ExamResultAdmin(admin.ModelAdmin):
    list_display = ('exam', 'student', 'marks', 'grade')
