from django.http import HttpResponse
from django.template import RequestContext
from django.template.loader import get_template
from .queries import get_all_courses, get_lesson
from authentication.authenticate import group_required
from django.contrib.auth.decorators import login_required
from Utils.UserGroups import TEACHER as TEACHER_GROUP


@login_required
@group_required(TEACHER_GROUP)
def lessons_home_page(request):
    context = RequestContext(request, {
        'name': request.user.first_name,
        'units': get_all_courses()
    })
    return HttpResponse(get_template("Lessons/lessons_home_page.html").render(context))


@login_required
@group_required(TEACHER_GROUP)
def get_lesson_plan(request, lesson_id):
    context = RequestContext(request, {
        'lesson': get_lesson(lesson_id)
    })
    return HttpResponse(get_template("Lessons/lesson_plan.html").render(context))


@login_required
@group_required(TEACHER_GROUP)
def get_create_new_lesson_page(request):
    context = RequestContext(request, {
        'name': request.user.first_name,
    })
    return HttpResponse(get_template('Lessons/create_new_lesson.html').render(context))