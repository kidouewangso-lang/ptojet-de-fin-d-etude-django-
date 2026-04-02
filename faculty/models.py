from django.db import models
from django.conf import settings

class Department(models.Model):
    name = models.CharField(max_length=100)
    head_of_department = models.CharField(max_length=100, blank=True)
    started_date = models.DateField(null=True, blank=True)
    student_capacity = models.IntegerField(default=50)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    teacher_id = models.CharField(max_length=20, unique=True)
    gender = models.CharField(max_length=10, choices=[('Male','Male'), ('Female','Female')])
    date_of_birth = models.DateField(null=True, blank=True)
    mobile_number = models.CharField(max_length=15)
    joining_date = models.DateField(null=True, blank=True)
    qualification = models.CharField(max_length=100, blank=True)
    experience = models.CharField(max_length=100, blank=True)
    address = models.TextField(blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username} ({self.teacher_id})"

class Subject(models.Model):
    subject_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.name

class Holiday(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class TimeTable(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=20, choices=[('Monday','Monday'), ('Tuesday','Tuesday'), ('Wednesday','Wednesday'), ('Thursday','Thursday'), ('Friday','Friday'), ('Saturday','Saturday')])
    start_time = models.TimeField()
    end_time = models.TimeField()
    room_no = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.subject} - {self.day_of_week}"

class Exam(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    room_no = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} - {self.subject}"

class ExamResult(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    student = models.ForeignKey('student.Student', on_delete=models.CASCADE)
    marks = models.DecimalField(max_digits=5, decimal_places=2)
    grade = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return f"{self.student} - {self.exam}"
