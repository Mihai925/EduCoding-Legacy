from django.http import HttpResponse
from Autotester.models import ExerciseTests
from Exercise.models import Exercise
from Exercise.exercise_queries import get_assigned_exercise_for_students
from .forms import ExerciseForm, NewExerciseForm
from uuid import uuid4
from Compiler.compiler import *
from authentication.authenticate import group_required
from django.views.generic import TemplateView, View
from django.utils.decorators import method_decorator
from django.shortcuts import render


class SingleExerciseEditorView(TemplateView):
    template_name = 'Exercise/student_single_exercise.html'

    @method_decorator(group_required('Student'))
    def get(self, request, *args, **kwargs):
        ex_id = args[0]
        exercise = Exercise.objects.get(ex_id=ex_id)
        template_pars = {
            'form': ExerciseForm(initial={'code': exercise.content}, auto_id="id_%s_" + ex_id),
            'ex_description': exercise.description,
            'ex_id': ex_id,
            'name': request.user.first_name}
        return render(request, self.template_name, template_pars)


class AllExercisesView(TemplateView):
    template_name = "Exercise/student_all_exercises.html"

    @method_decorator(group_required('Student'))
    def get(self, request, *args, **kwargs):
        # TODO: Need to change this to use the server query which currently this does not use.
        exercises = get_assigned_exercise_for_students(request.user)
        template_pars = {
            'name': request.user.first_name,
            'exercises': exercises
        }
        return render(request, self.template_name, template_pars)


@group_required('Student')
def submit_code(request):
    code = request.POST["code"]

    compiler = Compiler(code)
    output = compiler.compile()
    return HttpResponse(output)


class ManageExercisesView(View):
    template_name = "Exercise/manage_exercises.html"

    @method_decorator(group_required('Teacher'))
    def get(self, request, *args, **kwargs):
        template_pars = {
            'form': NewExerciseForm(initial={'code': ''}, auto_id='new_ex'),
            'errors': []
        }
        return render(request, self.template_name, template_pars)

    @method_decorator(group_required('Teacher'))
    def post(self, request, *args, **kwargs):
        errors = []
        tests = [ExerciseTests.objects.create(input=input, expected_output=output) for (input, output) in
                 zip(request.POST.getlist("input_test"), request.POST.getlist("output_test"))]
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
        template_pars = {
            'form': NewExerciseForm(initial={'code': ''}, auto_id='new_ex'),
            'errors': errors
        }
        return render(request, self.template_name, template_pars)
