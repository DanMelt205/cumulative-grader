# from django.forms import ModelForm
from django import forms
from .models import KsuStudent, Course


class StudentForm(forms.ModelForm):
    # student_id = forms.IntegerField(required=True)

    class Meta:
        model = KsuStudent
        fields = ("student_id",)


class CourseForm(forms.ModelForm):
    # course_id = forms.IntegerField(required=True)
    grade = forms.IntegerField(min_value=0, max_value=100, required=True)

    class Meta:
        model = Course
        fields = ("course_id", "grade",)
