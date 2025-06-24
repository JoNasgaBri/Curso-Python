#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np

# Criar DataFrames simulando application_record.csv e credit_record.csv
application_data = pd.DataFrame(
    {
        "ID": [5001711, 5001712, 5001713, 5001719, 5001720],
        "CODE_GENDER": ["M", "F", "F", "M", "F"],
        "AMT_INCOME_TOTAL": [270000.0, 135000.0, 180000.0, 112500.0, 157500.0],
        "NAME_EDUCATION_TYPE": [
            "Higher education",
            "Secondary / secondary special",
            "Higher education",
            "Secondary / secondary special",
            "Incomplete higher",
        ],
    }
)

credit_data = pd.DataFrame(
    {
        "ID": [
            5001711,
            5001711,
            5001711,
            5001712,
            5001712,
            5001713,
            5001719,
            5001719,
            5001720,
            5001720,
            5001720,
        ],
        "MONTHS_BALANCE": [0, -1, -2, 0, -1, 0, 0, -1, 0, -1, -2],
        "STATUS": ["X", "0", "0", "C", "C", "0", "0", "1", "0", "1", "0"],
    }
)


# In[4]:


# Junção dos datasets
df = pd.merge(application_data, credit_data, on="ID", how="inner")
print("DataFrame após junção:")
df.head()


# In[5]:


# Limpeza de Dados
# a) Remover valores nulos
df = df.dropna(subset=["AMT_INCOME_TOTAL", "STATUS"])

# b) Remover duplicatas
df = df.drop_duplicates()

# c) Renomear colunas para snake_case
df = df.rename(
    columns={
        "ID": "id",
        "CODE_GENDER": "genero",
        "AMT_INCOME_TOTAL": "renda_total",
        "NAME_EDUCATION_TYPE": "nivel_educacao",
        "MONTHS_BALANCE": "meses_saldo",
        "STATUS": "status",
    }
)

# d) Limpeza de strings
df["genero"] = df["genero"].str.lower().str.strip()
df["nivel_educacao"] = df["nivel_educacao"].str.lower().str.strip()

print("DataFrame após limpeza:")
df.head()


# In[6]:


# Formatos de Dados
# a) Verificar tipos antes da conversão
print("Tipos antes da conversão:")
print(df.dtypes)

# b) Corrigir tipos
df["renda_total"] = pd.to_numeric(df["renda_total"], errors="coerce")
df["meses_saldo"] = df["meses_saldo"].astype(int)

# c) Verificar tipos após conversão
print("Tipos após a conversão:")
print(df.dtypes)


# In[7]:


# Conversão de Formatos
# a) Criar coluna status_texto
status_map = {
    "0": "pagamento_no_prazo",
    "1": "atraso_30_59_dias",
    "2": "atraso_60_89_dias",
    "3": "atraso_90_119_dias",
    "4": "atraso_120_149_dias",
    "5": "atraso_150_dias_ou_mais",
    "C": "conta_paga",
    "X": "sem_emprestimo",
}
df["status_texto"] = df["status"].map(status_map)
print("DataFrame com status_texto:")
df.head()


# In[8]:


# Cálculo em Colunas
# a) Total de registros por ID
registros_por_id = df.groupby("id").size().reset_index(name="total_registros")

# b) Proporção de registros com atraso
atrasos = (
    df[df["status"].isin(["1", "2", "3", "4", "5"])]
    .groupby("id")
    .size()
    .reset_index(name="registros_atraso")
)
atrasos = atrasos.merge(registros_por_id, on="id", how="right").fillna(0)
atrasos["proporcao_atraso"] = atrasos["registros_atraso"] / atrasos["total_registros"]

# c) Juntar cálculos ao DataFrame principal
df = df.merge(
    atrasos[["id", "total_registros", "proporcao_atraso"]], on="id", how="left"
)

# d) Estatísticas descritivas
print("Estatísticas de renda_total:")
print(df["renda_total"].describe())


# In[9]:


# Condicionais em Colunas
# a) Criar risco_credito
def calcular_risco_credito(status_list):
    if any(s in ["1", "2", "3", "4", "5"] for s in status_list):
        return 1  # Mau pagador
    return 0  # Bom pagador


risco = df.groupby("id")["status"].apply(list).reset_index(name="status_list")
risco["risco_credito"] = risco["status_list"].apply(calcular_risco_credito)
df = df.merge(risco[["id", "risco_credito"]], on="id", how="left")

# b) Categorizar renda
condicoes_renda = [
    (df["renda_total"] < 100000),
    (df["renda_total"].between(100000, 200000)),
    (df["renda_total"] > 200000),
]
valores_renda = ["baixa", "media", "alta"]
df["faixa_renda"] = np.select(condicoes_renda, valores_renda, default="desconhecida")

print("DataFrame com risco_credito e faixa_renda:")
df.head()


# In[10]:


# Condicionais em Várias Colunas
# Criar alerta_credito
condicoes_alerta = [
    (df["risco_credito"] == 1) & (df["faixa_renda"] == "baixa"),
    (df["risco_credito"] == 1) & (df["faixa_renda"].isin(["media", "alta"])),
]
valores_alerta = ["risco_alto", "monitorar"]
df["alerta_credito"] = np.select(condicoes_alerta, valores_alerta, default="normal")

print("DataFrame com alerta_credito:")
df.head()


# In[13]:


# Exibir resultados
print("\nDataFrame final:")
print(df)

# Resumo estatístico
print("\nProporção de maus pagadores:")
print(df["risco_credito"].value_counts(normalize=True))


# In[ ]:
