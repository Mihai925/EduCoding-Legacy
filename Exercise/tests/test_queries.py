from django.test import TestCase
from django.contrib.auth.models import User

from Exercise.exercise_queries import *

# Create your tests here.

#TODO's
#Test: validate the data in the exercise
#Test: submit the exercise to the database
#Test: select an exercise based on exercise id


class ExercisesTestCase(TestCase):


    #TODO: most of it is a copy-paste, make it more reusable
    def setUp(self):
        self.std_1 = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        self.std_1.first_name = "Mark"
        self.std_2 = User.objects.create_user('mark', 'lennon2@thebeatles.com', 'johnpassword2')
        self.std_2.first_name = "Loo"
        self.std_3 = User.objects.create_user('loo', 'lennon3@thebeatles.com', 'johnpassword3')
        self.std_3.first_name = "Ogg"

        self.std_1.save()
        self.std_2.save()
        self.std_3.save()

        self.tch_1 = User.objects.create_user('sofia', 'lennon4@thebeatles.com', 'johnpassword4')
        self.tch_2 = User.objects.create_user('susan', 'lennon5@thebeatles.com', 'johnpassword5')

        self.tch_1.save()
        self.tch_2.save()

        class1 = Class(name="Algorithms", description="Sample")
        class2 = Class(name="Graphs", description="Stuff")

        class1.save()
        class1.teacher.add(self.tch_1)
        class1.save()
        class1.students.add(self.std_1)
        class1.students.add(self.std_2)

        class2.save()
        class2.teacher.add(self.tch_2)
        class2.save()
        class2.students.add(self.std_1)
        class2.students.add(self.std_3)

        class1.save()
        class2.save()

        self.class_id = class1.cls_id
        self.class_id_2 = class2.cls_id
        #end of copy-paste

        self.ex_1 = Exercise(title="Sorting exercise", description="Implement bubble-sort", content="whatever")
        self.ex_1.save()
        self.ex_1.classes_assigned_to.add(class1)
        self.ex_1.save()
        self.ex_2 = Exercise(title="Adding exercise", description="Add two numbers", content="whatever man!");

        self.ex_1.save()
        self.ex_2.save()

        self.ex_1_id = self.ex_1.ex_id
        self.ex_2_id = self.ex_2.ex_id

    def test_assign_exercise_to_class(self):
        assign_exercise_to_class(self.ex_2_id,self.class_id_2)
        self.assertEqual(1, len(self.ex_2.classes_assigned_to.all()))

    def test_get_assigned_exercise_for_students(self):
        exercises_stu2 = get_assigned_exercise_for_students(self.std_2)
        self.assertEqual(1, len(exercises_stu2))
        (class_name, exercise) = exercises_stu2[0]
        self.assertEqual("Sorting exercise" ,exercise[0].title)
        self.assertEqual("Implement bubble-sort" ,exercise[0].description)

    def test_get_assigned_exercise_for_class(self):
        exercises_cls1 = get_assigned_exercise_for_class(self.class_id)
        self.assertEqual(1, len(exercises_cls1))
        self.assertEqual("Sorting exercise" ,exercises_cls1[0].title)
        self.assertEqual("Implement bubble-sort" ,exercises_cls1[0].description)

