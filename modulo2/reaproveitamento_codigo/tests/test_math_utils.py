from utils.math_utils import quadrado, cubo, potencia


def test_quadrado():
    assert quadrado(3) == 9


def test_cubo():
    assert cubo(2) == 8


def test_potencia():
    assert potencia(2, 3) == 8
