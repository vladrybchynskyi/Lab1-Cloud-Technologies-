from django.db import models
from exam import Exam


class ExamVariant(models.Model):

    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE,
        related_name="variants"
    )

    # Variant number or letter ("1", "2", "A")
    label = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # Forbid duplicates: no repeat labels in same exam
        unique_together = ("exam", "label")

    def __str__(self):
        return f"{self.exam.title} – Variant {self.label}"

    @property
    def task_count(self):
        """How many tasks does this variant contain?"""
        return self.tasks.count()
