# Install pytest using pip
# pip install pytest

import pytest


def test_addition():
    """
    Test the addition of two numbers
    """
    assert 1 + 1 == 2


class TestMathOperations:
    """
    Test math operations
    """
    def test_addition(self):
        """
        Test addition of two numbers
        """
        assert 1 + 1 == 2

    def test_subtraction(self):
        """
        Test subtraction of two numbers
        """
        assert 3 - 2 == 1


@pytest.mark.parametrize("test_input,expected", [(1, 2), (3, 4), (5, 6)])
def test_addition_with_parameters(test_input, expected):
    """
    Test addition of two numbers with parameters
    """
    assert test_input + 1 == expected


@pytest.fixture
def example_data():
    """
    Fixture to return example data
    """
    return {'foo': 'bar'}


def test_example(example_data):
    """
    Test example data
    """
    assert example_data['foo'] == 'bar'