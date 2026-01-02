from django import forms
from .models import Student, Course
from django.contrib.auth.models import User

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

class StudentCourseForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['courses']

        widgets = {
            'courses': forms.CheckboxSelectMultiple()
        }

class StudentCreationForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Student
        fields = ['name', 'email', 'matric_number']

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            email=self.cleaned_data['email']
        )
        student = super().save(commit=False)
        student.user = user
        if commit:
            student.save()
        return student



