from django.db import models
from lab import Lab

class LabDeadline(models.Model):
    """
    Each deadline belongs to exactly one lab, but a lab can have multiple deadlines.

    The reason deadlines are split into a separate table is because:
    - every deadline has its own due date
    - every deadline has its own penalty
    - and we need to store them independently
    This allows flexible configurations with multiply deadlines
    """

    lab = models.ForeignKey(
        Lab,
        on_delete=models.CASCADE,
        related_name="deadlines",
    )

    due_date = models.DateTimeField()

    penalty = models.PositiveIntegerField(
        default=0,
        help_text="Points subtracted if submitted after this deadline.",
    )

    class Meta:
        ordering = ["due_date"]  # deadlines always appear in chronological order

    def __str__(self):
        return f"{self.lab} – deadline {self.due_date.date()} (penalty {self.penalty})"
