from django.db import models
from courses.models_courses.course import Course

class Lab(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="labs",
    )

    number = models.PositiveIntegerField()
    title = models.CharField(max_length=255)

    max_score = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.course.name} – Lab {self.number}"
