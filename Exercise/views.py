from django.http import HttpResponse
from Exercise.exercise_queries import get_assigned_exercise_for_students
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
        template_pars = {

        }
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
        }
        return render(request, self.template_name, template_pars)




