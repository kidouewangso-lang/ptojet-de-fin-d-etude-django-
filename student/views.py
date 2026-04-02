from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

def is_admin_or_teacher(user):
    return user.is_authenticated and (getattr(user, 'is_admin', False) or getattr(user, 'is_teacher', False))

def is_admin(user):
    return user.is_authenticated and getattr(user, 'is_admin', False)

from .models import Student, Parent

@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/students.html', {'student_list': students})

@user_passes_test(is_admin_or_teacher)
def add_student(request):
    if request.method == 'POST':
        d = request.POST
        parent = Parent.objects.create(
            father_name=d.get('father_name', ''),
            father_occupation=d.get('father_occupation', ''),
            father_mobile=d.get('father_mobile', ''),
            father_email=d.get('father_email', ''),
            mother_name=d.get('mother_name', ''),
            mother_occupation=d.get('mother_occupation', ''),
            mother_mobile=d.get('mother_mobile', ''),
            mother_email=d.get('mother_email', ''),
            present_address=d.get('present_address', ''),
            permanent_address=d.get('permanent_address', '')
        )
        student = Student.objects.create(
            first_name=d.get('first_name', ''),
            last_name=d.get('last_name', ''),
            student_id=d.get('student_id', ''),
            gender=d.get('gender', ''),
            date_of_birth=d.get('date_of_birth', '2000-01-01'),
            student_class=d.get('student_class', ''),
            joining_date=d.get('joining_date', '2000-01-01'),
            mobile_number=d.get('mobile_number', ''),
            admission_number=d.get('admission_number', ''),
            section=d.get('section', ''),
            student_image=request.FILES.get('student_image'),
            parent=parent
        )
        messages.success(request, 'Student added Successfully')
        return redirect('student_list')
    return render(request, 'students/add-student.html')

@login_required
def view_student(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    return render(request, 'students/student-details.html', {'student': student})

@user_passes_test(is_admin_or_teacher)
def edit_student(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    if request.method == 'POST':
        messages.success(request, 'Student updated Successfully')
        return redirect('student_list')
    return render(request, 'students/edit-student.html', {'student': student})

@user_passes_test(is_admin)
def delete_student(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    student.parent.delete() # this will cascade and delete student as well
    messages.success(request, 'Student deleted Successfully')
    return redirect('student_list')

@user_passes_test(is_admin_or_teacher)
def export_students_json(request):
    students = Student.objects.all()
    data = []
    for s in students:
        data.append({
            'student_id': s.student_id,
            'first_name': s.first_name,
            'last_name': s.last_name,
            'class': s.student_class,
            'date_of_birth': str(s.date_of_birth),
            'mobile_number': s.mobile_number,
            'parent_name': f"{s.parent.father_name} / {s.parent.mother_name}" if s.parent else "",
        })
    response = JsonResponse({'students': data}, json_dumps_params={'ensure_ascii': False, 'indent': 4})
    response['Content-Disposition'] = 'attachment; filename="students_export.json"'
    return response
