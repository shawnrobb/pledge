from django.conf import settings
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
    metric = models.ForeignKey(Metric, on_delete=models.CASCADE)
    version = models.PositiveSmallIntegerField(default=1)
    identifier = models.CharField(
        max_length=64
    )  # Todo: add validator to constrain to specific characters (e.g. a-z and underscores)
    value = models.FloatField()

    class Meta:
        unique_together = ("action", "metric", "version", "identifier")

    def __str__(self):
        return f"{self.action} ({self.identifier}) v{self.version}"


class Pledge(TimeStampedModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    action = models.ForeignKey(Action, on_delete=models.CASCADE)
    attribute = models.CharField(
        max_length=64
    )  # Todo: add validator to constrain to specific characters (e.g. a-z and underscores)
    value = models.FloatField()

    class Meta:
        unique_together = ("user", "action", "attribute")

    def __str__(self):
        return f"{self.user} - ({self.action}) ({self.attribute})"


class Question(TimeStampedModel):
    SELECT = "select"
    NUMBER = "number"
    TYPE_CHOICES = ((NUMBER, NUMBER), (SELECT, SELECT))

    action = models.ForeignKey(Action, on_delete=models.CASCADE)
    identifier = models.CharField(
        max_length=64
    )  # Todo: add validator to constrain to specific characters (e.g. a-z and underscores)
    question_type = models.CharField(max_length=6, choices=TYPE_CHOICES, default=NUMBER)

    class Meta:
        unique_together = ("action", "identifier")

    def __str__(self):
        return f"{self.action} ({self.identifier})"


class SelectOption(TimeStampedModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    display_text = models.CharField(max_length=64)
    value = models.FloatField(default=0)

    class Meta:
        unique_together = ("question", "display_text")

    def __str__(self):
        return f"{self.question} ({self.display_text})"


class Formula(TimeStampedModel):
    action = models.ForeignKey(Action, on_delete=models.CASCADE)
    metric = models.ForeignKey(Metric, on_delete=models.CASCADE)
    version = models.PositiveSmallIntegerField(default=1)
    eval_string = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.action} ({self.metric}) v{self.version}"

    class Meta:
        unique_together = ("action", "metric", "version")
