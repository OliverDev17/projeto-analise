📊 Projeto de Análise Automática com Python e IA
Este projeto implementa um agente inteligente de análise de dados em Python que automatiza todo o fluxo de trabalho de um cientista de dados: desde o carregamento de dados até a geração de relatórios em PDF.

🚀 Funcionalidades
📥 Carregamento de CSV com Pandas

🧹 Pré-processamento (tratamento de nulos e variáveis categóricas)

🤖 Modelagem com RandomForest para classificação automática

📊 Relatório de métricas (precisão, recall, f1-score, acurácia)

🎨 Visualizações: distribuição, correlação e importância das variáveis

📑 Exportação em PDF salva automaticamente no Desktop

📂 Estrutura do Projeto
Código
projeto_analise/
│── main.py              # Arquivo principal (orquestra execução)
│── agente.py            # Classe AgenteAnalise (pipeline de IA)
│── utils.py             # Funções utilitárias (carregar dados)
│── dados.csv            # Base de dados exemplo
│── relatorio_analise.pdf # Relatório gerado automaticamente
⚙️ Como executar
Clone o repositório:

bash
git clone https://github.com/seuusuario/projeto-analise.git
cd projeto-analise
Crie e ative um ambiente virtual:

bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
Instale as dependências:

bash
pip install -r requirements.txt
Execute o projeto:

bash
python main.py
📑 Resultado
Relatório exibido no terminal

Gráficos gerados automaticamente

PDF consolidado salvo no Desktop

💡 Próximos passos
Envio automático por e-mail

Agendamento com Airflow

Dashboards interativos com Streamlit

👨‍💻 Autor
Gabriel – Desenvolvedor apaixonado por dados e automação.
📌 Conecte-se comigo no LinkedIn. https://www.linkedin.com/in/gabriel-oliveira1705/
