import pytest
from lab0X import *

modulus = 8683317618811886495518194401279999999


@pytest.mark.task1
@pytest.mark.parametrize("polynomial, value, result", [
    ([1], 1000, 1),
    ([1, 2], 10, 12),
    ([5, 8, 1], 1000, 5008001),
    ([1, 1, 1, 1, 1, 1, 1, 1], 10000000000, 4431880142436212121547786588067757615),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 868331761881188649551819440127999999, 916413297382920010623284147230794061),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8683317618811886495518194401279999999, 10),
])
def test_polynomial_evaluation(polynomial, value, result):
    assert polynomial_evaluation(polynomial, value, modulus) == result


@pytest.mark.task2
@pytest.mark.parametrize("P_1, P_2, result", [
    ([1], [1], [2]),
    ([10, 0, 7, 8], [2, 0, 1], [10, 2, 7, 9]),
    ([1, 1, 1, 1, 1, 1, 1, 1], [modulus, modulus], [1, 1, 1, 1, 1, 1, 1, 1])
])
def test_polynomial_addition(P_1, P_2, result):
    assert polynomial_addition(P_1, P_2, modulus) == result


@pytest.mark.task3
@pytest.mark.parametrize("P_1, P_2, result", [
    ([1], [1], [1]),
    ([1, 1, 1], [2], [2, 2, 2]),
    ([1, 1, 1], [1, 1], [1, 2, 2, 1]),
    ([1, 2], [2, 3], [2, 7, 6]),
    ([10, 0, 7, 8], [2, 0, 1], [20, 0, 24, 16, 7, 8]),
    ([1, 2, 3, 4, 5, 6, 7, 8], [modulus - 1],
     [modulus - 1, modulus - 2, modulus - 3, modulus - 4, modulus - 5, modulus - 6, modulus - 7, modulus - 8])
])
def test_polynomial_multiplication(P_1, P_2, result):
    assert polynomial_multiplication(P_1, P_2, modulus) == result


@pytest.mark.task4
@pytest.mark.parametrize("S, result", [
    ({1}, [1, modulus - 1]),
    ({2, 3}, [1, modulus - 5, 6]),
    ({1, 2, 3, 4, 5}, [1, 8683317618811886495518194401279999984, 85, 8683317618811886495518194401279999774, 274,
                       8683317618811886495518194401279999879]),
])
def test_polynomial_representation(S, result):
    assert polynomial_representation(S, modulus) == result


@pytest.mark.task5
@pytest.mark.parametrize("A, B", [
    ({1}, {1}),
    ({1, 19, 10}, {1, 2}),
    ({1, 19, 10}, {19, 1, 10}),
    ({1, 19, 10, 4}, {19, 1, 10, 80}),
    ({9, 8, 2, 1, 100, 3, 44, 4, 234, 21, 45, 33},  {4, 10, 55, 23, 8, 12, 30, 89, 6, 102}),
    ({9, 8, 2, 1, 100, 3, 44, 4, 234, 21, 45, 33},  {9, 8, 2, 1, 100, 3, 44, 4, 234, 21, 45, 33})
])
def test_comp_intersection(A, B):
    assert set(comp_intersection(A, B, modulus)) == A.intersection(B)
