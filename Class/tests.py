from django.test import TestCase

from .class_queries import *



class ClassQuerysTest(TestCase):
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

        self.class1 = Class(name="Algorithms", description="Sample")
        self.class2 = Class(name="Graphs", description="Stuff")
        self.class1.save()
        self.class2.save()

        self.class1.teacher.add(self.tch_1)
        self.class1.save()
        self.class1.students.add(self.std_1)
        self.class1.students.add(self.std_2)

        self.class2.teacher.add(self.tch_2)
        self.class2.save()
        self.class2.students.add(self.std_1)
        self.class2.students.add(self.std_3)

        self.class1.save()
        self.class2.save()

        self.class_id = self.class1.cls_id


    # Given a Teacher object (User), class name and class id
    def test_class_by_teacher(self):
        class_tuple = get_class_by_teacher(self.tch_1)
        self.assertEqual(1, len(class_tuple))
        (class_name, class_desc, _) = class_tuple[0]
        self.assertEqual("Algorithms", class_name)
        self.assertEqual("Sample", class_desc)

    # Given a class id, return a list of all the students in the class
    def test_get_students_by_class(self):
        students_in_class = [("Mark", "", "john"), ("Loo", "", "mark")]
        students = get_students_by_class_id(self.class_id)
        self.assertEqual(2, len(students))
        for student in students:
            self.assertIn(student, students_in_class)

    # Add a student to a class
    def test_add_student_to_class(self):
        new_student = User.objects.create_user('Johhan', 'johhan@gmail.com', 'johnpassword4')
        new_student.first_name = "Johan"
        new_student.last_name = "Phillips"
        new_student.save()

        add_student_to_class(self.class_id, new_student)
        a_class = Class.objects.get(students=new_student)
        self.assertEqual(self.class_id, a_class.cls_id)

    def test_remove_student_from_class(self):
        # Adding a student
        new_student = User.objects.create_user('Johhan2', 'johhan@gmail.com', 'johnpassword4')
        new_student.save()
        self.class1.students.add(new_student)
        remove_student_from_class(self.class1.cls_id, new_student)

        for student in self.class1.students.all():
            if new_student == student:
                self.fail()
        # ClassManagement.objects.get(cls_id=cls_id).students.add(student)
        pass



