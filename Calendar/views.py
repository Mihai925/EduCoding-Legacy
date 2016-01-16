from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template


def teacher_home_calender_page(request):
    return HttpResponse(get_template("Calendar/teacher_calendar.html").render(
        Context({
            'name': request.user.first_name
        })
    ))