import factory

from django.contrib.auth import get_user_model
from factory import Faker, post_generation
from factory.django import DjangoModelFactory

from pledge.actions.models import Action, Pledge, Question, Answer, Metric, Formula


class ActionFactory(DjangoModelFactory):
    title = factory.Faker(
        "word", ext_word_list=["VegOut", "Stairs", "Flights", "Energy"]
    )

    class Meta:
        model = Action


class MetricFactory(DjangoModelFactory):
    title = factory.Faker("word", ext_word_list=["CO2", "H2O", "Waste"])

    class Meta:
        model = Metric


class PledgeFactory(DjangoModelFactory):
    class Meta:
        model = Pledge

    action = factory.SubFactory(ActionFactory)
    user = factory.SubFactory("pledge.users.tests.factories.UserFactory")


class QuestionFactory(DjangoModelFactory):
    class Meta:
        model = Question


class AnswerFactory(DjangoModelFactory):
    class Meta:
        model = Answer


class FormulaFactory(DjangoModelFactory):
    class Meta:
        model = Formula

    metric = factory.SubFactory(MetricFactory)
