from django.contrib import admin

# Register your models here.
from .models import Student, Course

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'matric_number')
    search_fields = ('name', 'email', 'matric_number')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'code')
    search_fields = ('title', 'code')

# @admin.register(Registration)
# class RegistrationAdmin(admin.ModelAdmin):
#     list_display = ('student', 'course', 'date_created')
#     search_fields = ('student',)