from django.shortcuts import render, redirect

from .forms import StudentForm, CourseForm
from .models import Student

# Create your views here.

def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
    else:
        form = StudentForm()
    return render(request, 'student/add_student.html', {'form': form})

def add_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save()
    else:
        form = CourseForm()
    return render(request, 'course/add_course.html', {'form': form})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student/student_list.html', {'students': students})