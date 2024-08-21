from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

class StudentManager(UserManager):
    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('roll_number', None)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        # Create a user with the default fields
        return self._create_user(username, email, password, **extra_fields)

class Student(AbstractUser):
    roll_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    department = models.CharField(max_length=50)

    objects = StudentManager()
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='student_set',
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='student_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return f"{self.username} ({self.roll_number})"


class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name

class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        indexes = [
            models.Index(fields=['student', 'subject']),
            models.Index(fields=['marks_obtained']),
        ]
        unique_together = ('student', 'subject')
