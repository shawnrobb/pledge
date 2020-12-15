from django.db import models

from django_extensions.db.models import TitleSlugDescriptionModel, TimeStampedModel


class Action(TimeStampedModel, TitleSlugDescriptionModel):
    def __str__(self):
        return self.title


class Metric(TimeStampedModel, TitleSlugDescriptionModel):
    def __str__(self):
        return self.title


class Constant(TimeStampedModel):
    action = models.ForeignKey(Action, on_delete=models.CASCADE)
    version = models.PositiveSmallIntegerField(default=1)
    identifier = models.CharField(
        max_length=64
    )  # Todo: add validator to constrain to specific characters (e.g. a-z and underscores)
    value = models.FloatField()

    class Meta:
        unique_together = ("action", "version", "identifier")

    def __str__(self):
        return f"{self.action} ({self.identifier}) v{self.version}"
