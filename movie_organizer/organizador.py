import pandas as pd
import unicodedata
import re
import locale

class OrganizadorDeFilmes:
    def __init__(self, arquivo_csv):
        self.arquivo_csv = arquivo_csv
        self.df = pd.read_csv(arquivo_csv)

    def renomear_colunas(self):
        # Renomear colunas
        self.df.rename(columns={'movieId': 'id do filme', 'title': 'Titulo', 'genres': 'Genero'}, inplace=True)

    def limpar_titulos_e_generos(self):
        # Limpar títulos usando unidecode e remover caracteres especiais no começo das palavras
        self.df['Titulo'] = self.df['Titulo'].apply(lambda x: re.sub(r"[^\w\s]", "", unicodedata.normalize('NFKD', str(x)).encode('ASCII', 'ignore').decode()))

        # Limpar gêneros
        self.df['Genero'] = self.df['Genero'].str.strip()

    def tratar_valores_nulos(self):
        # Preencher valores nulos com uma string vazia (pode ser ajustado conforme necessário)
        self.df.fillna('', inplace=True)

    def remover_duplicatas(self):
        # Remover duplicatas baseadas em todas as colunas
        self.df.drop_duplicates(inplace=True)

    def organizar_e_renumerar(self):
        # Configurar a localidade para ordenação correta
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

        # Adicionando uma coluna temporária para ordenação personalizada
        self.df['ordenacao_temp'] = self.df['Titulo'].apply(lambda x: unicodedata.normalize('NFKD', str(x)).encode('ASCII', 'ignore').decode())

        # Ordenar pelos títulos de forma alfabetica usando a localidade configurada
        self.df.sort_values(by=['ordenacao_temp'], key=lambda x: x.str.lower(), inplace=True)

        # Remover a coluna temporária
        self.df.drop(columns=['ordenacao_temp'], inplace=True)

        # Reindexar
        self.df['id do filme'] = range(1, len(self.df) + 1)

    '''def mostrar_amostra(self, n_primeiras=5, n_ultimas=5):
        print("Primeiras 5 linhas:")
        print(self.df.head(n_primeiras))
        print("\nÚltimas 5 linhas:")
        print(self.df.tail(n_ultimas))'''

    def salvar_novo_csv(self, novo_arquivo_csv):
        self.df.to_csv(novo_arquivo_csv, index=False)
