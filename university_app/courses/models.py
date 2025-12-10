from django.db import models

class EvaluationFormula(models.Model):
    lab_count = models.PositiveIntegerField()
    lab_max_score = models.PositiveIntegerField()
    exam_max_score = models.PositiveIntegerField()
    penalty_per_missed = models.PositiveIntegerField(default=0)

    def __str__(self):

        return f"Formula: {self.lab_count} labs, exam {self.exam_max_score}"  # Better view for admin


    @property
    def total_score(self):
        return (
            self.lab_count * self.lab_max_score + self.exam_max_score
        )

    def calculate_score(self, lab_scores, exam_score, missed_deadlines=0):

        labs_total = sum(lab_scores)

        raw_total = labs_total + exam_score

        penalty = missed_deadlines * int(self.penalty_per_missed) #type: ignore

        final_score = raw_total - penalty
        return max(final_score, 0) # Student score cannot be lower than 0

