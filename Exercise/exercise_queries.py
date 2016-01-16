from Class.models import Class
from Exercise.models import Exercise


def assign_exercise_to_class(ex_id, cls_id):
    a_class = Class.objects.get(cls_id=cls_id)
    exercise = Exercise.objects.get(ex_id=ex_id)
    exercise.classes_assigned_to.add(a_class)


def get_assigned_exercise_for_class(cls_id):
    a_class = Class.objects.get(cls_id=cls_id)
    exercises = Exercise.objects.filter(classes_assigned_to=a_class)
    return exercises
    #return [(exercise.title.encode("ascii", "ignore"), exercise.description.encode("ascii","ignore")) for exercise in exercises]


def get_assigned_exercise_for_students(student):
    student_classes = Class.objects.filter(students=student)
    ret = []
    for student_class in student_classes:
        class_name = Class.objects.get(cls_id=student_class.cls_id)
        exercises = get_assigned_exercise_for_class(student_class.cls_id)
        ret+= [(class_name.name, exercises)]
    #for exercise_tuples in [get_assigned_exercise_for_class(student_class.cls_id) for student_class in student_classes]:

    #    ret += exercise_tuples
    return ret


