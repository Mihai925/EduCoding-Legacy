from models import Exercise


class ExerciseTools():
    def __init__(self):
        pass

    def submit_exercise(self, title, description, content):
        exercise = Exercise(title=title, description=description, content=content)
        exercise.save()
        return True

    def get_exercise_by_id(self, ex_id):
        exercise = None
        try:
            exercise = Exercise.objects.get(ex_id=ex_id)
        except Exception as e:
            pass
        return exercise