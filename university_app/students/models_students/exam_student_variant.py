from django.db import models
from accounts.models import User
from exams.models_exams.exam import Exam
from exams.models_exams.exam_variant import ExamVariant


class ExamStudentVariant(models.Model):
    """
    Stores which exam variant was assigned to a particular student.

    Why we need it:
    - When a student starts the exam, we randomly pick a variant

    - We must guarantee that the student receives the SAME variant
      throughout the whole attempt

    - We must prevent assignment of multiple variants to the same student

    This table is basically a "journal" of variant distribution.
    """

    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="assigned_exam_variants",
    )

    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE,
        related_name="student_variants",
    )

    variant = models.ForeignKey(
        ExamVariant,
        on_delete=models.CASCADE,
        related_name="student_assignments",
    )

    assigned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        A student can have only ONE variant per exam.
        """
        unique_together = ("student", "exam")

    def __str__(self):
        return f"{self.student} – {self.exam.title} – {self.variant.label}"
