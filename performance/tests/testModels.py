from django.test import TestCase
from django.contrib.auth import get_user_model
from performance.models import Subject, Marks

class StudentModelTest(TestCase):

    def setUp(self):
        self.student = get_user_model().objects.create_user(
            username='testuser',
            password='pass1234',
            roll_number='123456',
            department='Computer Science'
        )

    def test_student_creation(self):
        self.assertEqual(self.student.username, 'testuser')
        self.assertEqual(self.student.roll_number, '123456')
        self.assertEqual(self.student.department, 'Computer Science')

class SubjectModelTest(TestCase):

    def setUp(self):
        self.subject = Subject.objects.create(name='Mathematics - 2', code='014')

    def test_subject_creation(self):
        self.assertEqual(self.subject.name, 'Mathematics - 2')
        self.assertEqual(self.subject.code, '014')

class MarksModelTest(TestCase):

    def setUp(self):
        self.student = get_user_model().objects.create_user(
            username='testuser',
            password='pass1234',
            roll_number='123456',
            department='Computer Science'
        )
        self.subject = Subject.objects.create(name='Mathematics - 2', code='014')
        self.marks = Marks.objects.create(student=self.student, subject=self.subject, marks_obtained=85)

    def test_marks_creation(self):
        self.assertEqual(self.marks.student.username, 'testuser')
        self.assertEqual(self.marks.subject.name, 'Mathematics - 2')
        self.assertEqual(self.marks.marks_obtained, 85)
