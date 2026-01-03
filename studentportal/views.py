from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .forms import StudentForm, StudentCreationForm, CourseForm, StudentCourseForm
from .models import Student, Course

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
    query = request.GET.get('q', '')

    if query:
        students = Student.objects.filter(
            Q(name__icontains=query) |
            Q(email__icontains=query) |
            Q(matric_number__icontains=query)
        )
    else:
        students = Student.objects.all()

    return render(request, 'student/student_list.html', {
        'students': students,
        'query': query,
    })

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course/course_list.html', {'courses': courses})

def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        form = StudentCourseForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
    else:
        form = StudentCourseForm(instance=student)

    return render(request, 'student/student_detail.html', {
        'student': student,
        'form': form,
        'courses': student.courses.all(),
    })

def student_login(request):
    error = None
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('student_dashboard')
        else:
            error = "Invalid credentials"

    return render(request, 'auth/login.html', {'error': error})


@login_required
def student_dashboard(request):
    student = request.user.student
    return render(request, 'student/dashboard.html', {
        'student': student,
        'courses': student.courses.all()
    })

@staff_member_required
def admin_dashboard(request):
    return render(request, 'admin/dashboard.html', {
        'student_count': Student.objects.count(),
        'course_count': Course.objects.count(),
        'total_enrollments': Student.objects.filter(courses__isnull=False).count(),
    })

def create_student_account(request):
    if request.method == "POST":
        form = StudentCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentCreationForm()

    return render(request, 'student/create_student.html', {'form': form})


