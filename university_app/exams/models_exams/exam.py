from django.db import models
from courses.models_courses.course import Course


class Exam(models.Model):
    class ExamType(models.TextChoices):
        MIDTERM = "midterm", "Midterm Exam"
        FINAL = "final", "Final Exam"
        QUIZ = "quiz", "Quiz Test"
        OTHER = "other", "Other"

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="exams"
    )

    title = models.CharField(max_length=255)

    type = models.CharField(
        max_length=20,
        choices=ExamType.choices,
        default=ExamType.OTHER,
    )

    max_score = models.PositiveIntegerField()

    is_published = models.BooleanField(default=False)
    deadline = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.course.name} – {self.title}"

    @property
    def has_deadline(self):
        return self.deadline is not None

    @property
    def total_tasks(self):
        return self.tasks.count()

    @property
    def total_variants(self):
        return self.variants.count()
