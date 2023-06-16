
# Redes Neurais e MOFs
### Diciplina - Redes Neurais e Algoritmos Genéticos
<h>
<p align="center">
<img src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge"/>
</p>
<h>

### Objetivo do Trabalho
Por meio de várias características físico-químicas prever uma MOF (Metal-Organic Framework) com o tamanho de poro desejado, usando computação em Python por redes neurais é utilizar técnicas de aprendizado de máquina, especificamente redes neurais, para criar um modelo preditivo capaz de estimar o tamanho de uma MOF com base em suas características físico-químicas.

As MOFs são materiais altamente porosos com estruturas cristalinas formadas por ligações entre íons metálicos ou clusters metálicos e ligantes orgânicos. Seu tamanho, como a área de superfície específica, a porosidade e a distribuição de tamanho de poro, é uma característica crucial que afeta suas propriedades e aplicações.
<p align="center">
  <img src="https://webinftest.web.its.manchester.ac.uk/wp-content/uploads/2021/06/What-are-MOFs2-1024x486.png" alt="Exemplo Estrutural de MOFs" width="300">
</p>
A abordagem proposta neste projeto é a utilização de redes neurais, que são modelos computacionais inspirados no funcionamento do cérebro humano. Redes neurais são capazes de aprender padrões complexos a partir de conjuntos de dados e podem ser treinadas para realizar previsões e estimativas com base nessas informações.

Por meio da computação em Python, será implementado um modelo de redes neurais que receberá características físico-químicas das MOFs como entrada e fornecerá uma predição do VOID FRACTION como saída. Essas características podem incluir propriedades estruturais, características dos ligantes e íons metálicos, entre outros parâmetros relevantes.

O objetivo final é construir um modelo de redes neurais preciso e confiável, capaz de prever o VOID FRACTION de MOFs com base em características físico-químicas específicas. Isso pode contribuir para a seleção e o design racional de MOFs com propriedades desejadas, acelerando o processo de desenvolvimento de novos materiais porosos com aplicações em áreas como armazenamento de gases, separação seletiva de substâncias e catálise.
<h>
## Interpretação do Código Mestre(MOFs.ipynb)
- Importações
- Tratamento de Dados
- Código e Discussão
- Divisão Treino Teste
- Algoritmo Genético?

## Interpretação do Código Auxiliar(Funções.py)
<h> O objetivo principal do código é extrair informações relevantes dos dados e realizar operações como a geração de novas colunas e manipulação dos dados.<h>

<h> O código utiliza diversas bibliotecas, como os, requests, pymatgen, numpy, pandas, random e matminer. Essas bibliotecas fornecem funcionalidades para manipulação de arquivos, requisições HTTP, manipulação de estruturas químicas, manipulação de dados numéricos, geração de números aleatórios e extração de características dos materiais.<h>

<h> A função funcao_extrair_features_cif é responsável por gerar novas colunas no dataframe, contendo propriedades extraídas dos dados CIF (Crystallographic Information File) de cada material, como átomos e posições. A função adsorptions_MOF extrai informações sobre adsorção de gases em cada MOF.<h>

<h> A função funcao_extrair_features_isotherms gera novas colunas no dataframe, contendo propriedades extraídas dos dados de isotherm de cada material, como a adsorção de gases em pressões variadas.<h>

<h> A função count_freq_chemical conta a frequência de cada elemento químico em cada coluna do dataframe e remove colunas com valores iguais a zero ou com frequência abaixo de um valor mínimo especificado.<h>

<h> A função extrair_cif extrai características estruturais-químicas dos arquivos CIF das MOFs e gera um novo dataframe contendo essas propriedades. Essas características são obtidas através da análise dos elementos químicos presentes nas MOFs e de propriedades estruturais dos CIF.<h>

<h> As funções gene_mof, individuo_mof e populacao_mof são responsáveis por gerar genes, indivíduos e uma população para o problema das MOFs. Os genes representam propriedades específicas das MOFs, como número de espaço do grupo, sistema cristalino e número de operações de simetria. Os indivíduos são combinações de genes e a população é uma lista de indivíduos.<h>

<h> As funções cruzamento_ponto_simples e mutacao_mof são operadores de cruzamento e mutação, respectivamente, utilizados em algoritmos genéticos para modificar os indivíduos da população.<h>

<h> Por fim, a função selecao_torneio_min realiza a seleção de indivíduos da população usando o método do torneio, onde um número específico de indivíduos é selecionado com base em seu valor de fitness.<h>

<h> Em resumo, o código é uma implementação em Python que lida com dados de MOFs, realiza extração de características, geração de novas colunas, manipulação de dados e aplicação de algoritmos genéticos para resolver problemas relacionados a esses materiais.<h>

## Bibliotecas Utilizadas

- [Os](https://docs.python.org/3/library/os.html): Interação com o sistema operacional, incluindo manipulação de arquivos e pastas.
- [Requests](https://docs.python-requests.org): Biblioteca para fazer requisições HTTP e obter dados de uma URL específica.
- [Pymatgen](https://pymatgen.org): Manipulação de estruturas e materiais, como leitura de arquivos CIF, cálculos de propriedades e manipulação de estruturas cristalinas.
- [Matminer](https://github.com/hackingmaterials/matminer): Biblioteca para extração de características de materiais a partir de dados experimentais e teóricos.
- [PyTorch](https://pytorch.org/): Framework de aprendizado de máquina de código aberto.
- [seaborn](https://seaborn.pydata.org/): Biblioteca de visualização de dados baseada no Matplotlib.
- [scikit-learn](https://scikit-learn.org/stable/): Biblioteca para aprendizado de máquina e análise de dados.
- [NumPy](https://numpy.org/): Biblioteca para manipulação de arrays multidimensionais e cálculos matemáticos.
- [Pandas](https://pandas.pydata.org/): Biblioteca para manipulação e análise de dados em Python.
- [random](https://docs.python.org/3/library/random.html): Módulo Python para geração de números aleatórios.

Essas bibliotecas foram escolhidas para fornecer funcionalidades essenciais ao projeto, como construção de redes neurais, visualização de dados, pré-processamento de dados, métricas de avaliação e manipulação de arrays.
<h>



## Colaboradores✨

<table>
  <tr>
<table>
  <tr>
    <td align="center"><a href="https://github.com/CaioHubit"><img src="https://avatars.githubusercontent.com/u/110487580?v=4" width="100px;" alt=""/><br /><sub><b>Caio Eduardo</b></sub></a><br />Programmer</td>
    <td align="center"><a href="https://github.com/danischagas"><img src="https://avatars.githubusercontent.com/u/106709314?v=4" width="100px;" alt=""/><br /><sub><b>Danielle dos Santos</b></sub></a><br />Programmer</td>
    <td align="center"><a href="https://github.com/gabrielxvr"><img src="https://avatars.githubusercontent.com/u/107067724?v=4" width="100px;" alt=""/><br /><sub><b>Gabriel Xavier</b></sub></a><br />Programmer</td>
    <td align="center"><a href="https://github.com/Gbeneti"><img src="https://avatars.githubusercontent.com/u/107064808?v=4" width="100px;" alt=""/><br /><sub><b>Gustavo Beneti</b></sub></a><br />Programmer</td>

  </tr>
</table>


Tabela de Funções
=================

<!-- markdownlint-enable -->

## Mentores✨
<!-- ALL-MENTORES-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
<table>
  <tr>
    <td align="center"><a href="https://github.com/drcassar"><img src="https://avatars.githubusercontent.com/u/9871905?v=4" width="100px;" alt=""/><br /><sub><b>Daniel R. Cassar</b></sub></a><br />Professor</td>
  </tr>
</table>
<!-- markdownlint-enable -->
