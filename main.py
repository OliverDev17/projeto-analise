
from agente import AgenteAnalise
from utils import carregar_dados

def main():
    # 1. Carregar dados
    df = carregar_dados("dados.csv")

    # 2. Criar agente de análise
    agente = AgenteAnalise(df)

    # 3. Executar análise
    agente.executar_pipeline()

if __name__ == "__main__":
    main()
