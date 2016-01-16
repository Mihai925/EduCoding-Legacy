__author__ = 'Kriss'

from .models import Unit as UnitModel, Lesson as LessonModel
from .ClassStructure import Assignment, Lesson, Unit


def get_all_courses():
    units = []
    for unit in UnitModel.objects.all():
        lessons = []
        for l in unit.lessons.all():
            lessons.append(
                Lesson(title=l.title, description=l.description, briefing=l.briefing, introduction=l.introduction,
                       assignments=[], lesson_id=l.lesson_id))
        units.append(Unit(name=unit.title, lessons=lessons, unit_id=unit.unit_id))
    return units


def get_lesson(lesson_id):
    l = LessonModel.objects.get(lesson_id=lesson_id)
    if l is None:
        return None
    assignments = []
    for assignment in l.assignments.all():
        assignments.append(
            Assignment(title=assignment.title, description=assignment.description, content=assignment.content))
    return Lesson(title=l.title, description=l.description, briefing=l.briefing, introduction=l.introduction,
                  assignments=assignments, lesson_id=l.lesson_id)