import time
import functools


def quadrado(numero: float) -> float:
    """Calcula o quadrado de um número."""
    return numero * numero


def cubo(numero: float) -> float:
    """Calcula o cubo de um número."""
    return numero**3


def potencia(base: float, expoente: float = 2) -> float:
    """Calcula a potência de um número."""
    return base**expoente


def aplicar_funcao(funcao, valores: list) -> list:
    """Aplica uma função a uma lista de valores."""
    return [funcao(x) for x in valores]


def medir_tempo(funcao):
    """Decorador para medir o tempo de execução apenas da chamada principal."""

    @functools.wraps(funcao)
    def wrapper(*args, **kwargs):
        if not hasattr(wrapper, "nivel") or wrapper.nivel == 0:
            wrapper.nivel = 0
            wrapper.nivel += 1
            inicio = time.time()
            try:
                resultado = funcao(*args, **kwargs)
                fim = time.time()
                print(f"{funcao.__name__} levou {fim - inicio:.6f} segundos")
                return resultado
            finally:
                wrapper.nivel -= 1
        else:
            return funcao(*args, **kwargs)

    return wrapper


@medir_tempo
def calcular_fatorial(n: int) -> int:
    """Calcula o fatorial de um número."""
    return 1 if n == 0 else n * calcular_fatorial(n - 1)


def fibonacci(n: int) -> int:
    """Calcula o n-ésimo número de Fibonacci recursivamente."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@functools.lru_cache(maxsize=None)
def fibonacci_cache(n: int) -> int:
    """Calcula Fibonacci com cache."""
    if n <= 1:
        return n
    return fibonacci_cache(n - 1) + fibonacci_cache(n - 2)


def fibonacci_iterativo(n: int) -> int:
    """Calcula Fibonacci iterativamente."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def listar_quadrados(n: int) -> list:
    """Lista os quadrados dos primeiros n números."""
    return [quadrado(i) for i in range(1, n + 1)]


def quadrados_pares(n: int) -> list:
    """Lista quadrados de números pares até n."""
    return [x**2 for x in range(2, n + 1, 2)]


def contar_ate(n: int) -> list:
    """Conta até n usando while."""
    resultado = []
    i = 1
    while i <= n:
        resultado.append(i)
        i += 1
    return resultado


def primeiros_impares(n: int) -> list:
    """Lista os primeiros n números ímpares."""
    resultado: list[int] = []
    i = 1
    while len(resultado) < n:
        if i % 2 == 0:
            i += 1
            continue
        resultado.append(i)
        i += 1
    return resultado


def combinar_listas(lista1: list, lista2: list) -> list:
    """Combina duas listas com zip e enumerate."""
    return [(i, x, y) for i, (x, y) in enumerate(zip(lista1, lista2))]


def gerar_quadrados(n: int):
    """Gera quadrados até n."""
    for i in range(1, n + 1):
        yield i**2
