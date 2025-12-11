from django.db import models
from django.utils import timezone

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    matric_number = models.CharField(max_length=255)

class Course(models.Model):
    title = models.CharField(max_length=225)
    code = models.CharField(max_length=6)
    description = models.TextField()

class Registration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)

