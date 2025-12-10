from django.db import models
from courses.models_courses.course import Course
from students.models import Student

class Lab(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="labs"
    )
    title = models.CharField(max_length=255)
    max_score = models.PositiveIntegerField(default=10)
    deadline = models.DateTimeField()

    def __str__(self):
        return f"{self.course.name} - {self.title}"

class LabSubmission(models.Model):
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE, related_name="submissions")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="lab_submissions")

    score = models.PositiveIntegerField(default=0)
    submitted_at = models.DateTimeField(null=True, blank=True)

    @property
    def is_late(self):
        if not self.submitted_at:
            return False
        return self.submitted_at > self.lab.deadline

    def __str__(self):
        return f"{self.student} - {self.lab} ({self.score})"
