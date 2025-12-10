from django.db import models
from django.utils import timezone

from .exam_student_variant import ExamStudentVariant


class ExamSubmission(models.Model):

    student_variant = models.OneToOneField(
        ExamStudentVariant,
        on_delete=models.CASCADE,
        related_name="submission"
    )

    started_at = models.DateTimeField(default=timezone.now)
    submitted_at = models.DateTimeField(null=True, blank=True)

    total_score = models.FloatField(default=0)

    is_submitted = models.BooleanField(default=False)

    def submit(self):
        """Mark the exam as submitted."""
        if not self.is_submitted:
            self.submitted_at = timezone.now()
            self.is_submitted = True
            self.save()

    def __str__(self):
        return f"Submission: {self.student_variant.student.username} – {self.student_variant.exam_variant}"
