import logging
from utils.math_utils import (
    quadrado,
    potencia,
    aplicar_funcao,
    calcular_fatorial,
    fibonacci,
    fibonacci_cache,
    fibonacci_iterativo,
    listar_quadrados,
    quadrados_pares,
    contar_ate,
    primeiros_impares,
    combinar_listas,
    gerar_quadrados,
    cubo,
    medir_tempo,
)

logging.basicConfig(filename="app.log", level=logging.INFO)


@medir_tempo
def calcular_cubo(n: float) -> float:
    logging.info(f"Calculando cubo de {n}")
    return cubo(n)


# Testes das funções
print(f"Quadrado de 5: {quadrado(5)}")
print(f"5 ao quadrado: {potencia(5)}")
print(f"5 ao cubo: {potencia(5, 3)}")
valores = [1, 2, 3, 4]
print(f"Quadrados: {aplicar_funcao(quadrado, valores)}")
print(f"Fatorial de 5: {calcular_fatorial(5)}")
print(f"Fibonacci de 6: {fibonacci(6)}")
print(f"Fibonacci com cache de 30: {fibonacci_cache(30)}")
print(f"Fibonacci iterativo de 6: {fibonacci_iterativo(6)}")
print(f"Quadrados de 1 a 5: {listar_quadrados(5)}")
print(f"Quadrados pares até 10: {quadrados_pares(10)}")
print(f"Contar até 5: {contar_ate(5)}")
print(f"Primeiros 5 ímpares: {primeiros_impares(5)}")
print(f"Combinar listas: {combinar_listas([1, 2], ['a', 'b'])}")
print(f"Gerador de quadrados até 5: {list(gerar_quadrados(5))}")

# Atividade prática
resultado = calcular_cubo(3)
logging.info(f"Resultado: {resultado}")
print(f"Cubo de 3: {resultado}")
