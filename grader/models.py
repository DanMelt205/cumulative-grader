from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class KsuStudent(models.Model):
    student_id = models.PositiveIntegerField(null=True)
    course_id = models.PositiveIntegerField(null=True)
    grade = models.PositiveSmallIntegerField(
        null=True, validators=[MinValueValidator(0), MaxValueValidator(100)])

    class Meta:
        db_table = "ksu_student"


# class Course(models.Model):
#     course_id = models.PositiveIntegerField(primary_key=True)
#     grade = models.PositiveSmallIntegerField(
#         null=True, validators=[MinValueValidator(0), MaxValueValidator(100)])
#     # student = models.ForeignKey("KsuStudent", verbose_name=(
#     #     "Student_id"), on_delete=models.CASCADE)

#     class Meta:
#         db_table = "course"
