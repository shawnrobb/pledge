from django.conf import settings
from django.db import models

from django_extensions.db.models import TitleSlugDescriptionModel, TimeStampedModel


class Action(TimeStampedModel, TitleSlugDescriptionModel):
    """Model to define an Action that a user can make a pledge against."""

    def __str__(self):
        return self.title


class Pledge(TimeStampedModel):
    """Model to define a user's pledge towards a specific action."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    action = models.ForeignKey(Action, on_delete=models.CASCADE)
    message = models.CharField(max_length=255, blank=True)

    class Meta:
        unique_together = ("user", "action")

    def __str__(self):
        return f"{self.user} ({self.action})"


class Question(TimeStampedModel):
    """Model to define a specific identifier (e.g. veggie_meals) and corresponding type (e.g. select)
    for an Action."""

    SELECT = "select"
    NUMBER = "number"
    TYPE_CHOICES = ((NUMBER, NUMBER), (SELECT, SELECT))

    action = models.ForeignKey(Action, on_delete=models.CASCADE)
    identifier = models.CharField(
        max_length=64
    )  # Todo: add validator to constrain values to specific characters (e.g. a-z and underscores)
    question_type = models.CharField(max_length=6, choices=TYPE_CHOICES, default=NUMBER)

    class Meta:
        unique_together = ("action", "identifier")

    def __str__(self):
        return f"{self.action} ({self.identifier})"


class SelectOption(TimeStampedModel):
    """Model to define select options for a specific question."""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    display_text = models.CharField(max_length=64)
    value = models.FloatField(default=0)

    class Meta:
        unique_together = ("question", "display_text")

    def __str__(self):
        return f"{self.question} ({self.display_text})"


class Answer(TimeStampedModel):
    """Model to hold the user's answer for a specific question (e.g. veggie meals) on a Pledge

    Utilizes EAV (Entity - Attribute - Value) pattern.
    """

    pledge = models.ForeignKey(Pledge, on_delete=models.CASCADE, related_name="answers")
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    value = models.FloatField()

    class Meta:
        unique_together = ("pledge", "question")

    def __str__(self):
        return f"{self.pledge.user} - {self.question}"


class Metric(TimeStampedModel, TitleSlugDescriptionModel):
    """Model to define a Metric (e.g. co2, h2o, waste, etc.)."""

    def __str__(self):
        return self.title


class Formula(TimeStampedModel):
    """Model that holds the formula (eval_string) to be evaluated for a specific (e.g Veg Out) action and metric (e.g. co2).

    Note that versioning has not yet been implemented."""

    action = models.ForeignKey(Action, on_delete=models.CASCADE)
    metric = models.ForeignKey(Metric, on_delete=models.CASCADE)
    version = models.PositiveSmallIntegerField(default=1)
    eval_string = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.action} ({self.metric}) v{self.version}"

    class Meta:
        unique_together = ("action", "metric", "version")
