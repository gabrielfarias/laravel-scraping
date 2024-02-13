import psycopg2
from selenium import webdriver
import time
from bs4 import BeautifulSoup

# Função para inserir um único conjunto de dados no banco de dados
def inserir_dados(nome, variacao, created_at):
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

        # Comando SQL para inserir os dados na tabela
        sql = """INSERT INTO indicadores_financeiros (nome, variacao, created_at)
                 VALUES (%s, %s, %s)"""

        # Executa o comando SQL, passando os parâmetros
        cur.execute(sql, (nome, variacao, created_at))

        # Confirma a transação
        conn.commit()
    except psycopg2.Error as e:
        print(f"Erro ao inserir dados: {e}")
    finally:
        # Fecha o cursor e a conexão
        cur.close()
        conn.close()

# Função para capturar dados do site e chamar a função de inserção
def capturar_dados_e_inserir():
    # Configurações do Chrome WebDriver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")  # Modo headless (sem interface gráfica)

    # Inicializa o navegador
    driver = webdriver.Chrome(executable_path='scripts/chromedriver', options=chrome_options)

    try:
        # URL a ser acessada
        url = 'https://economia.uol.com.br/cotacoes/cambio/'

        # Acessa a URL
        driver.get(url)

        # Aguarda 5 segundos para o conteúdo ser carregado
        time.sleep(5)

        # Parsing do HTML com BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Encontrando a seção de IPCA
        ipca_section = soup.find('section', class_='ipca')
        if ipca_section:
            ipca_info = ipca_section.find('div', class_='info')
            if ipca_info:
                nome_ipca = ipca_info.find('span', class_='name').text.strip()
                variacao_ipca = ipca_info.find('span', class_='data').text.strip()
                created_at = time.strftime('%Y-%m-%d %H:%M:%S')
                inserir_dados(nome_ipca, variacao_ipca, created_at)

        # Encontrando a seção de SELIC
        selic_section = soup.find('section', class_='indicators')
        if selic_section:
            selic_info = selic_section.find('span', class_='name', text='SELIC').find_parent('div', class_='info')
            if selic_info:
                nome_selic = selic_info.find('span', class_='name').text.strip()
                variacao_selic = selic_info.find('span', class_='data').text.strip()
                created_at = time.strftime('%Y-%m-%d %H:%M:%S')
                inserir_dados(nome_selic, variacao_selic, created_at)

        # Encontrando a seção da Bovespa
        bovespa_section = soup.find('section', class_='stock')
        if bovespa_section:
            bovespa_info = bovespa_section.find('div', class_='info')
            if bovespa_info:
                nome_bovespa = bovespa_info.find('span', class_='name').text.strip()
                variacao_bovespa = bovespa_info.find('span', class_='data').text.strip()  # Alterado de 'value' para 'data'
                created_at = time.strftime('%Y-%m-%d %H:%M:%S')
                inserir_dados(nome_bovespa, variacao_bovespa, created_at)

    finally:
        # Fecha o navegador
        driver.quit()

# Chamada da função para capturar dados e inserir no banco de dados
capturar_dados_e_inserir()
