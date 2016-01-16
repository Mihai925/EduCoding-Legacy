from django.http import HttpResponse
from django.template import RequestContext
from django.template.loader import get_template
from Autotester.models import ExerciseTests
from Exercise.models import Exercise
from Exercise.exercise_queries import get_assigned_exercise_for_students
from .forms import ExerciseForm, NewExerciseForm
from uuid import uuid4
from Compiler.compiler import *
from authentication.authenticate import group_required

@group_required('Student')
def submit_exercise(request):
    return


@group_required('Student')
def add_new_exercise(request):
    return

@group_required('Student')
def student_single_exercise_editor(request, ex_id):
    exercise = Exercise.objects.get(ex_id=ex_id)
    context = RequestContext(request,
                       {'form': ExerciseForm(initial={'code': exercise.content}, auto_id="id_%s_" + ex_id),
                       'ex_description': exercise.description,
                       'ex_id': ex_id,
                       'name': request.user.first_name})
    return HttpResponse(get_template('Exercise/student_single_exercise.html').render(context))



@group_required('Student')
def get_exercise_for_student(request):
    # TODO: Need to change this to use the server query which currently this does not use.
    exercises = get_assigned_exercise_for_students(request.user)
    context = RequestContext(request,
    {
        'name': request.user.first_name,
        'exercises': exercises
    })
    return HttpResponse(get_template("Exercise/student_all_exercises.html").render(context))


@group_required('Student')
def submit_code(request):

    code = request.POST["code"]

    compiler = Compiler(code, str(uuid4().get_hex().upper()[0:6]))
    output = compiler.compile()
    return HttpResponse(output)

@group_required('Teacher')
def manage_exercise(request):
    errors = []
    if request.method == 'POST':
        tests = [ExerciseTests.objects.create(input=input, expected_output=output) for (input, output) in zip(request.POST.getlist("input_test"), request.POST.getlist("output_test"))]
        title = request.POST["inputTitle"]
        code = request.POST["code"]
        if not title:
            errors += ['Title field cannot be empty']
        description = request.POST["inputDescription"]
        if not description:
            errors += ['Description field cannot be empty']

        if not errors:

            new_exercise = Exercise.objects.create(title=title, description=description, content=code)
            new_exercise.tests = tests

    context = RequestContext(request, {'form': NewExerciseForm(initial={'code': ''}, auto_id='new_ex'), 'errors': errors})
    return HttpResponse(get_template("Exercise/manage_exercises.html").render(context))
