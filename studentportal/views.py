from django.shortcuts import render, redirect

from .forms import StudentForm


# Create your views here.

def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
    else:
        form = StudentForm()
    return render(request, 'student/add_student.html', {'form': form})
