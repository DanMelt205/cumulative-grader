from django.shortcuts import render
from .models import KsuStudent
from django.db.models import Avg
from django.contrib import messages


def home(request):

    #   Enter information for database
    s = KsuStudent()

    if request.method == 'POST':

        student_id = request.POST.get('student_id')
        course_id = request.POST.get('course_id')
        grade = request.POST.get('grade')

        s.student_id = student_id
        s.course_id = course_id
        s.grade = grade

        s.save()

    else:
        pass

    context = {
        's':  s,
    }

    return render(request, 'grader/home.html', context)


def grader(request):
    # Display information and average from database
    all = []
    x = 0
    # message = " "

    if request.method == 'POST':

        student_id = request.POST.get('student_id')

        u = KsuStudent.objects.filter(student_id=student_id)

        if u is not None:
            all = u.all()
            x = u.aggregate(average=Avg('grade'))
            x = x.get('average')
            print(x)
        else:
            pass
            # message = f"The student id {student_id} is not found."

    context = {
        'all': all,
        'avg': x,
        # 'message': message,
    }

    return render(request, 'grader/display.html', context)
