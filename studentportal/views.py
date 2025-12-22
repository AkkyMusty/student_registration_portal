from django.shortcuts import render, redirect

from .forms import StudentForm, CourseForm, RegistrationForm
from .models import Student, Course, Registration

# Create your views here.

def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student/add_student.html', {'form': form})

def add_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'course/add_course.html', {'form': form})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student/student_list.html', {'students': students})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course/course_list.html', {'courses': courses})

def register_student(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_list')
    else:
        form = RegistrationForm()

    return render(request, 'registration/register_student.html', {'form': form})

def registration_list(request):
    registrations = Registration.objects.select_related('student', 'course')
    return render(
        request,
        'registration/registration_list.html',
        {'registrations': registrations}
    )
