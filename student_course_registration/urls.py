"""
URL configuration for student_course_registration project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from studentportal.views import (add_student, add_course, student_list, course_list, student_detail)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/add/', add_student, name='add_student'),
    path('course/add/', add_course, name='add_course'),
    path('students/', student_list, name='student_list'),
    path('courses/', course_list, name='course_list'),
    path('students/<int:student_id>/', student_detail, name='student_detail'),
]
