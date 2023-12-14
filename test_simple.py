import pytest

from simple import calculate


@pytest.mark.parametrize(
    "order, result",
    [
        (1, {250: 1, 500: 0, 1000: 0, 2500: 0}),
        (251, {250: 2, 500: 0, 1000: 0, 2500: 0}),
        (1000, {250: 0, 500: 0, 1000: 1, 2500: 0}),
        (2501, {250: 1, 500: 0, 1000: 0, 2500: 1}),
        (3001, {250: 1, 500: 1, 1000: 0, 2500: 1}),
    ]
)
def test_simple_calculate(order, result):
    options = [250, 500, 1000, 2500]
    assert calculate(options, order) == result
