import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from matplotlib.backends.backend_pdf import PdfPages

class AgenteAnalise:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def executar_pipeline(self):
        print("🚀 Iniciando análise automática...")

        # Pré-processamento
        self.df = self.df.dropna()
        X = self.df.drop("target", axis=1)
        y = self.df["target"]

        # Transformar variáveis categóricas
        X = pd.get_dummies(X)

        # Divisão dos dados
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

        # Modelagem
        modelo = RandomForestClassifier()
        modelo.fit(X_train, y_train)
        y_pred = modelo.predict(X_test)

        # Relatório
        relatorio = classification_report(y_test, y_pred)
        print("📊 Relatório de Classificação:")
        print(relatorio)

        # Gerar PDF com gráficos e relatório
        self.gerar_relatorio_pdf(X, y, modelo, relatorio)

    def gerar_relatorio_pdf(self, X, y, modelo, relatorio):
        import os

        desktop = os.path.join(os.path.expanduser("~"), "Desktop", "relatorio_analise.pdf")
        with PdfPages(desktop) as pdf:
            # Página 1 - Relatório de texto
            plt.figure(figsize=(8,6))
            plt.text(0.01, 0.05, relatorio, fontsize=12)
            plt.axis("off")
            plt.title("Relatório de Classificação")
            pdf.savefig()
            plt.close()

            # Página 2 - Distribuição da variável alvo
            plt.figure(figsize=(6,4))
            sns.countplot(x=y)
            plt.title("Distribuição da variável alvo")
            pdf.savefig()
            plt.close()

            # Página 3 - Correlação entre variáveis
            plt.figure(figsize=(8,6))
            sns.heatmap(X.corr(), annot=True, cmap="coolwarm")
            plt.title("Mapa de correlação")
            pdf.savefig()
            plt.close()

            # Página 4 - Importância das variáveis
            importancias = pd.Series(modelo.feature_importances_, index=X.columns)
            importancias.sort_values().plot(kind="barh", figsize=(8,6))
            plt.title("Importância das variáveis")
            pdf.savefig()
            plt.close()

        print(f"✅ Relatório salvo em: {desktop}")

