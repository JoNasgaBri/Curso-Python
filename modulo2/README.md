# Reaproveitamento de Código

Um projeto desenvolvido para o Módulo 2 do Curso de Python, focado no reaproveitamento de código em Python. Este projeto implementa funções matemáticas reutilizáveis, testes unitários e documentação gerada com Sphinx, demonstrando boas práticas de programação, como modularização, tipagem estática e formatação de código.

## Descrição do Projeto

Este projeto foi criado como parte da Atividade Prática do Módulo 2, com o objetivo de aprender a organizar código em módulos, reutilizar funções e aplicar ferramentas como `pytest`, `flake8`, `mypy` e Sphinx. Inclui funções como `cubo`, `quadrado`, `calcular_fatorial` e outras operações matemáticas, todas otimizadas com anotações de tipo e decoradores para medir desempenho.

## Funcionalidades

- Cálculo de operações matemáticas (quadrado, cubo, potência, fatorial, Fibonacci).
- Reutilização de código através de um módulo `utils/math_utils.py`.
- Testes unitários automatizados com `pytest`.
- Geração de documentação estática com Sphinx.
- Registro de logs em `app.log` para monitoramento.
- Verificação de estilo e tipos com `flake8` e `mypy`.

## Pré-requisitos

- **Python 3.7 ou superior**.
- Ferramentas recomendadas:
  - `pip` para instalar dependências.
  - `git` (opcional, para controle de versão).
  - VS Code ou outro editor com suporte a Python.

## Como Usar

1. **Clone o repositório** (se aplicável):
   ```bash
   git clone https://github.com/JoNasgaBri/Curso-Python.git
   cd reaproveitamento_codigo