from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    add more fields later (avatar, bio, student_id)
    quickly check permissions in views/templates
    """
    is_student = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)

    student_id = models.CharField(max_length=50, blank=True, null=True, unique=True)

    bio = models.TextField(blank=True)
    avatar = models.URLField(blank=True)

    def __str__(self):
        return self.get_username()
