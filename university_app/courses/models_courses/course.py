from django.core.exceptions import ValidationError
from django.db import models
from accounts.models import User
from evaluation_formula import EvaluationFormula

class Course(models.Model):
    name = models.CharField(max_length=255,unique=True)
    description = models.TextField(blank=True)


    evaluation_formula = models.OneToOneField(
        # OneToOneField because each course has its own formula and each formula its own course

        EvaluationFormula,
        on_delete=models.CASCADE,
        related_name="course",
    )

    instructor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,      # Impossible to make course without instructor
        related_name="courses"
    )

    def __str__(self):
        return self.name

    def clean(self):
        """
        Ensures that the course cannot be created with duplicate names
        and that the linked evaluation formula is valid
        """
        if Course.objects.filter(name=self.name).exclude(pk=self.pk).exists():
            raise ValidationError("Course with this name already exists")

        if Course.objects.filter(evaluation_formula=self.evaluation_formula).exists():
            raise ValidationError("This formula is already used by another course")

        pass
