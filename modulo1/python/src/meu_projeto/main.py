
import logging
from meu_projeto.utils.calculadora import multiplicar

logging.basicConfig(filename="app.log", level=logging.INFO)

def main() -> None:
    """Função principal do programa."""
    logging.info("Iniciando cálculo")
    resultado = multiplicar(4, 5)
    logging.info(f"Resultado: {resultado}")
    print(f"4 x 5 = {resultado}")

if __name__ == "__main__":
    main()