# pip install pytest
import pytest as pytest


def test_addition():
    assert 1 + 1 == 2


class TestMathOperations:
    def test_addition(self):
        assert 1 + 1 == 2

    def test_subtraction(self):
        assert 3 - 2 == 1


@pytest.mark.parametrize("test_input,expected", [(1, 2), (3, 4), (5, 6)])
def test_addition(test_input, expected):
    assert test_input + 1 == expected


@pytest.fixture
def example_data():
    return {'foo': 'bar'}

def test_example(example_data):
    assert example_data['foo'] == 'bar'