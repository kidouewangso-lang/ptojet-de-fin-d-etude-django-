from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from faculty.models import Subject, Teacher, Exam, ExamResult
from student.models import Student

def index(request):
    return redirect('login')

@login_required
def dashboard(request):
    context = {
        'total_subjects': Subject.objects.count(),
        'total_students': Student.objects.count(),
        'total_exams': Exam.objects.count(),
        'total_teachers': Teacher.objects.count(),
    }
    return render(request, 'students/student-dashboard.html', context)
