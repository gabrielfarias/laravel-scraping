import psycopg2
from selenium import webdriver
import time

# Função para inserir um único conjunto de dados no banco de dados
def inserir_dados(nome, valor, variacao, created_at):
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
        sql = """INSERT INTO moedas (nome, valor, variacao, created_at)
                 VALUES (%s, %s, %s, %s)"""

        # Executa o comando SQL, passando os parâmetros
        cur.execute(sql, (nome, valor, variacao, created_at))

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

        # Captura os dados necessários
        currencies_section = driver.find_element_by_class_name('currencies')
        info_divs = currencies_section.find_elements_by_class_name('info')

        # Itera sobre as divs e insere os dados no banco de dados
        for info_div in info_divs:
            nome = info_div.find_element_by_class_name('name').text.strip()
            valor = info_div.find_element_by_class_name('value').text.strip()
            variacao = info_div.find_element_by_class_name('data').text.strip()

            # Data da coleta
            created_at = time.strftime('%Y-%m-%d %H:%M:%S')

            # Insere os dados no banco de dados
            inserir_dados(nome, valor, variacao, created_at)
    finally:
        # Fecha o navegador
        driver.quit()

# Chamada da função para capturar dados e inserir no banco de dados
capturar_dados_e_inserir()
