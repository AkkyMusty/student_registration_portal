from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    matric_number = models.CharField(max_length=255, unique=True)

    courses = models.ManyToManyField('Course', blank=True)

    def __str__(self):
        return f"{self.name} ({self.matric_number})"

class Course(models.Model):
    title = models.CharField(max_length=225)
    code = models.CharField(max_length=6)
    description = models.TextField()

    def __str__(self):
        return f"{self.code} - {self.title}"




