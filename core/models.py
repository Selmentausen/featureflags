# Create your models here.
from uuid import uuid4

from django.conf import settings
from django.db import models


class TimeStampedModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Organisation(TimeStampedModel):
    name = models.CharField(max_length=120)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="organisations", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Project(TimeStampedModel):
    organisation = models.ForeignKey(
        Organisation, related_name="projects", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=120)
    api_key = models.CharField(max_length=64, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.api_key:
            self.api_key = uuid4().hex
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.organisation} / {self.name}"


class Environment(TimeStampedModel):
    project = models.ForeignKey(
        Project, related_name="environments", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=60)

    class Meta:
        unique_together = ("project", "name")

    def __str__(self):
        return f"{self.project} : {self.name}"


class FeatureFlag(TimeStampedModel):
    environment = models.ForeignKey(
        Environment, related_name="flags", on_delete=models.CASCADE
    )
    key = models.CharField(max_length=120)
    enabled = models.BooleanField(default=False)
    percentage = models.PositiveSmallIntegerField(default=0)

    class Meta:
        unique_together = ("environment", "key")
        indexes = [models.Index(fields=["environment", "key"])]

    def __str__(self):
        return f"{self.environment} / {self.key}"


class Evaluation(TimeStampedModel):
    flag = models.ForeignKey(
        FeatureFlag, related_name="evaluations", on_delete=models.CASCADE
    )
    user_identifier = models.CharField(max_length=120)
    result = models.BooleanField()

    class Meta:
        indexes = [
            models.Index(fields=["flag", "created_at"]),
        ]
