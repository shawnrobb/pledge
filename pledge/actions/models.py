from django.db import models

from django_extensions.db.models import TitleSlugDescriptionModel, TimeStampedModel


class Action(TimeStampedModel, TitleSlugDescriptionModel):
    def __str__(self):
        return self.title
