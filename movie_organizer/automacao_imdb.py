from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

class IMDbScraper:
    def __init__(self):
        # Configurar o driver do Selenium (certifique-se de ter o chromedriver ou geckodriver instalado)
        options = Options()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument('--accept-insecure-certs')
        self.driver = webdriver.Chrome(options=options) # Você pode escolher o driver apropriado para o seu navegador


    def entrar_no_imdb(self):
        self.driver.get("https://www.imdb.com")
        print("Entrou no site do IMDb com sucesso.") 

    def pesquisar_filme(self, titulo):
        campo_de_digitacao = self.driver.find_element(By.XPATH, '//*[@id="suggestion-search"]')
        campo_de_digitacao.send_keys(titulo)
        campo_de_digitacao.send_keys(Keys.RETURN)
            
    def selecionar_filme(self):
        primeiro_filme = self.driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/section/div/div[1]/section[2]/div[2]/ul/li[1]/div[2]')
        primeiro_filme.click()
        print('selecionou o filme')
        
        try:
            # Esperar até que o elemento seja visível (aqui você pode ajustar o tempo de espera conforme necessário)
            elemento_esperado = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[2]/div/div[1]/a'))
            )

            return elemento_esperado
        except NoSuchElementException:
            # A exceção será capturada se o elemento não for encontrado
            print("Elemento não encontrado. Avaliação não disponível.")
            return None
                
    def extrair_avaliacao_filme(self):
        try:
            # Tentar encontrar o elemento de avaliação
            avaliacao_element = self.driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/section/div/section/div/div[1]/section[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/span[1]')
            # Extrair a nota de avaliação do elemento
            avaliacao = avaliacao_element.text.replace(',', '.')  # Substituir a vírgula por um ponto
            print(avaliacao)
            return float(avaliacao)  # Converter a avaliação para float
        except NoSuchElementException:
            print("Avaliação não encontrada")
            return "Avaliação não encontrada"

        
    def adicionar_avaliacao_ao_excel(self, nome_filme, avaliacao):
        try:
            # Ler o arquivo CSV
            df = pd.read_csv("filmes_organizados.csv")
        except FileNotFoundError:
            print("Arquivo 'filmes_organizados.csv' não encontrado.")
            return
        
        # Adicionar a avaliação na coluna "Nota IMDb" correspondente ao filme
        df.loc[df['Titulo'] == nome_filme, 'Nota IMDb'] = avaliacao
        
        # Salvar o DataFrame de volta no arquivo CSV
        df.to_csv("filmes_organizados.csv", index=False)

        print(f'Avaliação do filme {nome_filme} adicionada ao arquivo CSV: {avaliacao}')


    def fechar_navegador(self):
        # Fechar o navegador quando terminar
        self.driver.quit()
        print('Automação Encerrada.')
