from django.db import models
from exam import Exam


class ExamTask(models.Model):

    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE,
        related_name="tasks"
    )


    order = models.PositiveIntegerField()
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField()

    # Maximum score for this task
    max_score = models.PositiveIntegerField()

    class Meta:
        # Tasks must appear in a consistent order
        ordering = ["order"]

        # A single exam cannot have two tasks with the same order number
        unique_together = ("exam", "order")

    def __str__(self):
        return f"{self.exam.title} – Task {self.order}"
