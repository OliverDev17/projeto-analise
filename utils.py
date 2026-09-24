import pandas as pd

def carregar_dados(caminho: str) -> pd.DataFrame:
    print(f"📥 Carregando dados de {caminho}...")
    return pd.read_csv(caminho)
