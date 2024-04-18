from organizador import OrganizadorDeFilmes
from automacao_imdb import IMDbScraper
import time
import pandas as pd

if __name__ == "__main__":
    # Organizar filmes
    organizador = OrganizadorDeFilmes("movies.csv")
    organizador.renomear_colunas()
    organizador.limpar_titulos_e_generos()
    organizador.tratar_valores_nulos()
    organizador.remover_duplicatas()
    organizador.organizar_e_renumerar()
    #organizador.mostrar_amostra()
    organizador.salvar_novo_csv("filmes_organizados.csv")

    # Automatizar avaliações do IMDb
    scraper = IMDbScraper()
    scraper.entrar_no_imdb()
    
    # Ler nomes de filmes da tabela organizada
    df_filmes = pd.read_csv("filmes_organizados.csv")
    nomes_filmes = df_filmes['Titulo']

    for nome_filme in nomes_filmes:
        scraper.pesquisar_filme(nome_filme)
        botao_avaliacao = scraper.selecionar_filme()  
        if botao_avaliacao:
            botao_avaliacao.click()  
            avaliacao = scraper.extrair_avaliacao_filme()
            scraper.adicionar_avaliacao_ao_excel(nome_filme, avaliacao)
        time.sleep(5)

    scraper.fechar_navegador()
