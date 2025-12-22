from django import forms
from .models import Student, Course, Registration

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'name',
            'email',
            'matric_number',
        ]

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'title',
            'code',
            'description',
        ]

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = [
            'student',
            'course'
        ]

    def clean(self):
        cleaned_data = super().clean()
        student = cleaned_data.get('student')
        course = cleaned_data.get('course')

        if student and course:
            exists = Registration.objects.filter(student=student, course=course).exists()
            if exists:
                raise forms.ValidationError(f"{student.name} is already registered for {course.code}.")

        return cleaned_data


