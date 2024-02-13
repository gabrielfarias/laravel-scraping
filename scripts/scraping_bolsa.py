import psycopg2
from selenium import webdriver
import time
from bs4 import BeautifulSoup

# Função para inserir um único conjunto de dados de ação no banco de dados
def inserir_acao(nome, valor, variacao, created_at):
    try:
        # Configuração da conexão com o banco de dados
        conn = psycopg2.connect(
            dbname="dados_financeiros",
            user="postgres",
            password="123",
            host="localhost"
        )

        # Cria um cursor para executar comandos SQL
        cur = conn.cursor()

        # Comando SQL para inserir os dados na tabela de ações
        sql = """INSERT INTO bolsa (nome, valor, variacao, created_at)
                 VALUES (%s, %s, %s, %s)"""

        # Executa o comando SQL, passando os parâmetros
        cur.execute(sql, (nome, valor, variacao, created_at))

        # Confirma a transação
        conn.commit()
    except psycopg2.Error as e:
        print(f"Erro ao inserir dados da ação: {e}")
    finally:
        # Fecha o cursor e a conexão
        cur.close()
        conn.close()

# Função para capturar e inserir os dados das ações no banco de dados
def capturar_e_inserir_dados_acoes():
    # Configurações do Chrome WebDriver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")  # Modo headless (sem interface gráfica)

    # Inicializa o navegador
    driver = webdriver.Chrome(executable_path='scripts/chromedriver', options=chrome_options)

    try:
        # URL a ser acessada
        url = 'https://economia.uol.com.br/cotacoes/bolsas/'

        # Acessa a URL
        driver.get(url)

        # Aguarda 5 segundos para o conteúdo ser carregado
        time.sleep(5)

        # Parsing do HTML com BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Encontrando todas as seções com a classe 'stock-rankings'
        sections = soup.find_all('section', class_='stock-rankings')

        for section in sections:
            # Itera sobre as ações da seção atual
            for item in section.find_all('tr', class_='dadosRankings'):
                nome_acao = item.find('td', class_='title').text.strip()

                # Verifica se há uma classe 'up' ou 'down' para determinar a variação percentual
                variacao_percentual = item.find('td', class_='up').text.strip() if item.find('td', class_='up') else item.find('td', class_='down').text.strip()

                valor_acao = item.find_all('td')[2].text.strip()

                # Data da coleta
                created_at = time.strftime('%Y-%m-%d %H:%M:%S')

                # Insere os dados da ação no banco de dados
                inserir_acao(nome_acao, valor_acao, variacao_percentual, created_at)

    finally:
        # Fecha o navegador
        driver.quit()

# Chamada da função para capturar e inserir os dados das ações no banco de dados
capturar_e_inserir_dados_acoes()
