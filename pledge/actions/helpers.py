from django.db.models import Count

from .models import Answer


def get_total_pledges():
    return len(
        Answer.objects.values("question__action").annotate(
            action_count=Count("question__action")
        )
    )
