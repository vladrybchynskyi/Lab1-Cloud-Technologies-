from django.db import models
from students.models import Student
from courses.models_courses.course import Course

class ExamResult(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="exam_results")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="exam_results")

    score = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.student} — {self.course} exam: {self.score}"
