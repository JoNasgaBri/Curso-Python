from meu_projeto.utils.calculadora import multiplicar

def test_multiplicar() -> None:
    """Testa a função multiplicar."""
    assert multiplicar(4, 5) == 20