# 🐍 Curso: Boas Práticas de Desenvolvimento em Python

Um repositório completo para aprender **reutilização de código** e **boas práticas** em Python, baseado no curso ministrado pelo **Professor Maxwell Gomes**.

## 📚 Sobre o Curso

Este repositório organiza os exercícios e projetos dos **3 módulos** do curso:

### 📖 Módulo 1 - Boas Práticas de Desenvolvimento
- **Carga Horária:** 2h teoria + 1h prática
- **Foco:** Organização de projetos, PEP 8, documentação e estrutura avançada
- **Tópicos:** Módulos, testes unitários, logging

### 🔄 Módulo 2 - Reaproveitamento de Código
- **Carga Horária:** 3h teoria + 1h prática  
- **Foco:** Técnicas de reaproveitamento e modularização
- **Tópicos:** Funções modulares, recursividade, decoradores, geradores, list comprehensions

### 📊 Módulo 3 - Manipulação de Dados com Pandas
- **Carga Horária:** 5h teoria + 1h prática
- **Foco:** Análise e transformação de dados profissional
- **Pré-requisitos:** Python básico e conhecimento de bibliotecas
- **Tópicos:** 
  - Limpeza de dados (valores nulos, duplicatas, strings)
  - Formatação e conversão de tipos
  - Cálculos e estatísticas em colunas
  - Condicionais simples e complexas

## 📁 Estrutura do Repositório
Siga este exemplo para modularização  de seu projeto
```
├── modulo1/                     # Organização e boas práticas
├── modulo2/                     # Reaproveitamento de código
├── modulo3/                     # Manipulação de dados
│   ├── limpeza_dados/
│   ├── formatos_dados/
│   ├── conversao_formatos/
│   ├── calculo_colunas/
│   ├── condicionais_colunas/
│   ├── condicionais_varias_colunas/
│   └── analise_risco_credito/   # 🎯 Projeto final
├── src/                         # Código-fonte
├── tests/                       # Testes unitários
├── docs/                        # Documentação
├── requirements.txt             # Dependências
├── .gitignore                   # Arquivos ignorados
└── README.md                    # Este arquivo
```

## 🚀 Como Usar

### 1️⃣ Instalação

```bash
# Clone o repositório
git clone https://github.com/JoNasgaBri/Curso-Python.git
cd boas-praticas-python

# Crie um ambiente virtual
python -m venv .venv

# Ative o ambiente virtual
# Windows
.venv\Scripts\activate
# Mac/Linux
source .venv/bin/activate

# Instale as dependências
pip install -r requirements.txt
```

### 2️⃣ Executando os Projetos

```bash
# Execute qualquer módulo
python modulo2/src/main.py

# Execute testes
pytest tests/
```

### 3️⃣ Documentação

```bash
# Gere a documentação
cd docs
make html

# Abra no navegador
# docs/_build/html/index.html
```

### 4️⃣ Verificação de Código

```bash
# Formate o código
black .

# Verifique qualidade
flake8 .
mypy .
```

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**
- **Pandas** - Manipulação de dados
- **Pytest** - Testes unitários
- **Black** - Formatação de código
- **Flake8** - Linting
- **MyPy** - Verificação de tipos
- **Sphinx** - Documentação

## 📋 Pré-requisitos

- Python 3.8 ou superior
- Conhecimentos básicos de Python (variáveis, funções, listas)
- Familiaridade com bibliotecas Python (para Módulo 3)

## 🎯 Projetos Destacados

### 📈 Análise de Risco de Crédito
Projeto final que aplica todos os conceitos aprendidos:
- Limpeza e transformação de dados
- Aplicação de condicionais complexas
- Cálculos estatísticos
- Boas práticas de código

## 🤝 Contribuição

Este é um repositório educacional pessoal. Sinta-se à vontade para:

- 📝 Adicionar novos exercícios
- 🐛 Corrigir bugs ou melhorar documentação
- 💡 Sugerir melhorias

## 👨‍🏫 Professor

**Maxwell Gomes** - Instrutor do curso

## 📄 Licença

Este projeto é destinado para uso **educacional e pessoal**. Consulte o professor para detalhes sobre licenciamento.

## 💡 Dicas Importantes

- 🔍 **Sempre leia** as mensagens de erro no terminal
- 📝 **Mantenha** o `.gitignore` atualizado
- 💻 **Use** VS Code para melhor experiência
- 🧪 **Execute** os testes regularmente
- 📚 **Documente** seu código seguindo as boas práticas

---

⭐ **Se este repositório te ajudou, deixe uma estrela!**
