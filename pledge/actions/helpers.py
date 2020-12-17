from django.db.models import Count
from django.contrib.auth import get_user_model

from .models import Answer, Action, Formula, Pledge

User = get_user_model()


def get_total_impact(metric):
    """Return the combined total for all Pledges where this metric is applicable."""
    # get all actions that have this metric applied
    relevant_actions = _get_actions_with_metric(metric)
    total = 0
    for action in relevant_actions:
        # get all pledges for this action
        pledges = Pledge.objects.filter(action=action)
        for pledge in pledges:
            # calculate the result using the given formula and inputs and add to total
            total += calculate_metric_for_pledge(metric, pledge)
    return total


def _get_actions_with_metric(metric):
    """Return a set of actions that have a formula defined for this metric."""
    return Action.objects.filter(formula__metric=metric)


def calculate_metric_for_pledge(metric, pledge):
    """"Return result from calculating metric for the given pledge"""
    # get formula for this action and metric (e.g. Veg Out and co2)
    formula = Formula.objects.get(metric=metric, action=pledge.action)

    # build up a dictionary of identifiers and corresponding user answers to be plugged into the formula
    # e.g. {'heating_source': 5.0, 'number_of_people': 2.0, 'energy_supplier': 0.5}
    eval_data = {}
    for answer in pledge.answers.all():
        eval_data[answer.question.identifier] = answer.value

    # return the result using the given formula and inputs
    return eval(formula.eval_string, eval_data)
