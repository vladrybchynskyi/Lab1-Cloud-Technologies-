from django.db import models
from accounts.models import User
from courses.models_courses.course import Course

class Student(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="student_profile"
    )

    courses = models.ManyToManyField(Course, related_name="students", blank=True)

    def __str__(self):
        return self.user.username

