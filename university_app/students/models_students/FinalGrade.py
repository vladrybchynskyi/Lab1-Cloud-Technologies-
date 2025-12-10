from django.db import models
from students.models import Student
from courses.models_courses.course import Course
from courses.models_courses.evaluation_formula import EvaluationFormula

class FinalGrade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    final_score = models.FloatField(default=0)

    def __str__(self):
        return f"{self.student} - {self.course}: {self.final_score}"
