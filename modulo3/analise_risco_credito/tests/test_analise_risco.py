import pandas as pd
from src.analise_risco_credito import df  

def test_risco_credito():
    assert any(df['risco_credito'] == 1), "Não há maus pagadores no DataFrame"
    proporcao = df['risco_credito'].value_counts(normalize=True)[1]
    assert abs(proporcao - 0.454545) < 0.01, "Proporção de maus pagadores incorreta"