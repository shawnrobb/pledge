import pytest

from pledge.actions.factories import (
    ActionFactory,
    PledgeFactory,
    MetricFactory,
    QuestionFactory,
    AnswerFactory,
    FormulaFactory,
)
from pledge.actions.helpers import calculate_metric_for_pledge
from pledge.users.models import User
from pledge.users.tests.factories import UserFactory


class TestCalculationHelperFunctions:
    """Tests for ensuring correctness of metric calculation functions."""

    # TODO: Parametrize these tests to test a variety of formula types (e.g. multiple questions)

    @pytest.mark.django_db
    def test_calculate_metric_for_pledge_function_single_question(self, user: User):
        """Check function returns correct result for metric with single user question."""
        pledge = PledgeFactory()
        # identifiers in question must match those in Formula
        question1_identifier = "veggie_meals"
        question1 = QuestionFactory(
            action=pledge.action, identifier=question1_identifier
        )
        answer1_value = 2.5
        answer1 = AnswerFactory(pledge=pledge, question=question1, value=answer1_value)

        const1 = 0.884
        const2 = 8.7

        eval_string = f"{const1} * {question1_identifier} * {const2}"
        formula = FormulaFactory(action=pledge.action, eval_string=eval_string)

        expected_result = const1 * answer1_value * const2

        assert calculate_metric_for_pledge(formula.metric, pledge) == expected_result
