from django.db import models
from django.utils import timezone

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    matric_number = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.name} ({self.matric_number})"

class Course(models.Model):
    title = models.CharField(max_length=225)
    code = models.CharField(max_length=6)
    description = models.TextField()

    def __str__(self):
        return f"{self.code} - {self.title}"

class Registration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student} registered for {self.course}"



