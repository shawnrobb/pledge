from django.db.models import Count
from django.contrib.auth import get_user_model

from .models import Answer, Action, Formula, Pledge

User = get_user_model()


def get_total_impact(metric):
    # get all actions that have this metric applied
    relevant_actions = _get_actions_with_metric(metric)
    total = 0
    for action in relevant_actions:
        pledges = Pledge.objects.filter(action=action)
        for pledge in pledges:
            # get formula for this action and metric (e.g. Veg Out and co2)
            formula = Formula.objects.get(metric=metric, action=action)
            eval_data = {}
            for answer in pledge.answers.all():
                eval_data[answer.question.identifier] = answer.value
            total += eval(formula.eval_string, eval_data)
    return total


def _get_actions_with_metric(metric):
    return Action.objects.filter(formula__metric=metric)
