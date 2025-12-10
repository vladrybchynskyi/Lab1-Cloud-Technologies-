from django.db import models
from exam_task import ExamTask
from exam_variant import ExamVariant


class ExamTaskVariant(models.Model):     #Represents a specific version of a task inside a specific variant.

    task = models.ForeignKey(
        ExamTask,
        on_delete=models.CASCADE,
        related_name="variants",
    )

    variant = models.ForeignKey(
        ExamVariant,
        on_delete=models.CASCADE,
        related_name="tasks",
    )

    # Concrete wording for this variant
    text = models.TextField()

    max_score = models.PositiveIntegerField()

    class Meta:
        """
        A given task can have only ONE version per variant.
        """
        unique_together = ("task", "variant")

    def __str__(self):
        return f"{self.variant.label} – Task {self.task.order}"
