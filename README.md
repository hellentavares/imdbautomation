# Movie Organizer - Automação IMDb
  Este é um projeto Python que automatiza a organização de filmes a partir de uma planilha CSV e realiza avaliações automáticas no IMDb para cada filme da lista.

# Funcionalidades
- Organização da Planilha
- O programa lê uma planilha CSV contendo informações sobre filmes.
- Realiza a renomeação de colunas, limpeza de títulos e gêneros, tratamento de valores nulos, remoção de duplicatas e renumeração dos filmes.
- Os filmes organizados são salvos em uma nova planilha CSV.
- Automação IMDb
- Utiliza Selenium WebDriver para automatizar a navegação e interação com o IMDb.
- Para cada filme na planilha organizada, pesquisa o título no IMDb, extrai a avaliação e adiciona essa informação de volta à planilha.
  
# Pré-requisitos
- Python 3.x instalado
- Gerenciador de pacotes pip instalado
- Chrome instalado (necessário para o Selenium WebDriver)
  
# Instalação
  1. Clone o repositório do GitHub:
   git clone https://github.com/hellentavares/imdbautomation.git
  2. Navegue até o diretório do projeto:
   cd movie-organizer
  3. Instale as dependências necessárias:
    pip install -r requirements.txt

# Como Executar
1. Certifique-se de estar no diretório do projeto.
2. Execute o arquivo main.py:
  python main.py
  
# Estrutura do Projeto
    movie-organizer/
    
    ── main.py                  # Script principal para execução do programa
    
    ── organizador.py           # Módulo responsável pela organização da planilha de filmes
    
    ── automacao_imdb.py        # Módulo com a automação do IMDb usando Selenium
    
    ── movies.csv               # Planilha de entrada com os dados dos filmes
    
    ── filmes_organizados.csv   # Planilha de saída com os filmes organizados e avaliações IMDb
    
    ── README.md                # Arquivo README com instruções e descrição do projeto
  
# Detalhes de Implementação
  - main.py: Ponto de entrada do programa que utiliza OrganizadorDeFilmes e IMDbScraper para processar a planilha e automatizar o IMDb.
  - organizador.py: Contém a classe OrganizadorDeFilmes que implementa métodos para organizar a planilha de filmes.
  - automacao_imdb.py: Contém a classe IMDbScraper que utiliza Selenium para interagir com o IMDb.
  - movies.csv: Planilha de entrada contendo dados dos filmes.
  -ilmes_organizados.csv: Planilha de saída com os filmes organizados e avaliações IMDb.
