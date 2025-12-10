from django.db import models
from django.utils import timezone

from exam_submission import ExamSubmission
from exams.models_exams.exam_task_variant import ExamTaskVariant


class ExamTaskSubmission(models.Model):
    """
    Stores a student's answer for a specific task within an exam submission.

    Each ExamSubmission will have multiple ExamTaskSubmission entries — one per task.
    """

    exam_submission = models.ForeignKey(
        ExamSubmission,
        on_delete=models.CASCADE,
        related_name="task_submissions"
    )

    task_variant = models.ForeignKey(
        ExamTaskVariant,
        on_delete=models.CASCADE,
        related_name="submissions"
    )

    # For advanced tasks this can be JSON or file upload.
    answer_text = models.TextField(null=True, blank=True)

    answer_file = models.FileField(
        upload_to="exam_answers/",
        null=True,
        blank=True
    )

    score = models.FloatField(default=0)
    is_checked = models.BooleanField(default=False)

    submitted_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"TaskSubmission: {self.exam_submission.id} – {self.task_variant.id}"
