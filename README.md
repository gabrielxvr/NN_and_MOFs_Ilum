
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
<details>
  <summary>Importações</summary>
  <ul>
    <li>
      <code>import torch</code>: Importa o módulo torch, que é um framework de aprendizado de máquina de código aberto.
    </li>
    <li>
      <code>import torch.nn as nn</code>: Importa o submódulo nn do PyTorch, que fornece ferramentas para construir redes neurais.
    </li>
    <li>
      <code>import torch.optim as optim</code>: Importa o submódulo optim do PyTorch, que contém otimizadores para treinamento de modelos.
    </li>
    <li>
      <code>import matplotlib.pyplot as plt</code>: Importa o módulo pyplot do Matplotlib, que é uma biblioteca de visualização de dados em Python.
    </li>
    <li>
      <code>import seaborn as sns</code>: Importa o módulo seaborn, que é uma biblioteca de visualização de dados baseada no Matplotlib.
    </li>
    <li>
      <code>from sklearn.model_selection import train_test_split</code>: Importa a função train_test_split do submódulo model_selection do scikit-learn, que permite dividir conjuntos de dados em treino e teste.
    </li>
    <li>
      <code>from sklearn.preprocessing import MinMaxScaler</code>: Importa a classe MinMaxScaler do submódulo preprocessing do scikit-learn, que realiza a normalização dos dados.
    </li>
    <li>
      <code>from sklearn.metrics import mean_squared_error</code>: Importa a função mean_squared_error do submódulo metrics do scikit-learn, que calcula o erro quadrático médio entre as previsões e os valores verdadeiros.
    </li>
    <li>
      <code>import numpy as np</code>: Importa o módulo numpy, que é uma biblioteca para manipulação de arrays multidimensionais e cálculos matemáticos.
    </li>
    <li>
      <code>import pandas as pd</code>: Importa o módulo pandas, que é uma biblioteca para manipulação e análise de dados em Python.
    </li>
    <li>
      <code>import random</code>: Importa o módulo random, que fornece funções para geração de números aleatórios.
    </li>
    <li>
      <code>from funcoes import selecao_torneio_min as funcao_selecao</code>: Importa a função selecao_torneio_min do módulo funcoes e a renomeia como funcao_selecao.
    </li>
    <li>
      <code>from funcoes import cruzamento_ponto_simples as funcao_cruzamento</code>: Importa a função cruzamento_ponto_simples do módulo funcoes e a renomeia como funcao_cruzamento.
    </li>
  </ul>
</details>

<details>
  <summary>Tratamento de Dados</summary>
  <ul>
    <li>
      <code>df = extrair_cif(df, minimo = 5)</code>: Executa a função extrair_cif, que realiza o tratamento dos dados contidos no DataFrame df, mantendo apenas as amostras com um número mínimo de registros igual a 5.
    </li>
    <li>
      <code>df.keys()</code>: Retorna as chaves (nomes das colunas) do DataFrame df.
    </li>
  </ul>
</details>
<details>
  <summary>Divisão de Treino-Teste</summary>
  <ul>
    <li>
      <code>TAMANHO_TESTE = 0.1</code>: Define o tamanho da amostra de teste como 10% do conjunto de dados total.
    </li>
    <li>
      <code>SEMENTE_ALEATORIA = 61455</code>: Define a semente aleatória para garantir a reprodutibilidade dos resultados.
    </li>
    <li>
      <code>FEATURES = list(df.iloc[:,2:].keys())</code>: Cria uma lista com os nomes das colunas (características) a serem usadas como entrada para o modelo.
    </li>
    <li>
      <code>TARGET = ['void fraction']</code>: Define a variável alvo (porosidade do mof) a ser prevista pelo modelo.
    </li>
    <li>
      <code>indices = df.index</code>: Obtém os índices das amostras do DataFrame df.
    </li>
    <li>
      <code>indices_treino, indices_teste = train_test_split(indices, test_size=TAMANHO_TESTE, random_state=SEMENTE_ALEATORIA)</code>: Divide os índices das amostras em conjuntos de treino e teste, com base no tamanho do conjunto de teste e na semente aleatória.
    </li>
    <li>
      <code>df_treino = df.loc[indices_treino]</code>: Seleciona as amostras de treino do DataFrame df com base nos índices de treino.
    </li>
    <li>
      <code>df_teste = df.loc[indices_teste]</code>: Seleciona as amostras de teste do DataFrame df com base nos índices de teste.
    </li>
    <li>
      <code>X_treino = df_treino.reindex(FEATURES, axis=1)</code>: Cria uma matriz de treino X_treino contendo apenas as colunas de características selecionadas.
    </li>
    <li>
      <code>y_treino = df_treino.reindex(TARGET, axis=1)</code>: Cria um vetor de treino y_treino contendo a variável alvo (porosidade do mof).
    </li>
    <li>
      <code>X_teste = df_teste.reindex(FEATURES, axis=1)</code>: Cria uma matriz de teste X_teste contendo apenas as colunas de características selecionadas.
    </li>
    <li>
      <code>y_teste = df_teste.reindex(TARGET, axis=1)</code>: Cria um vetor de teste y_teste contendo a variável alvo (porosidade do mof).
    </li>
    <li>
      <code>normalizador_x = MinMaxScaler()</code>: Inicializa um objeto MinMaxScaler para normalização das características de entrada.
    </li>
    <li>
      <code>normalizador_y = MinMaxScaler()</code>: Inicializa um objeto MinMaxScaler para normalização da variável alvo.
    </li>
    <li>
      <code>normalizador_x.fit(X_treino)</code>: Ajusta o normalizador_x aos dados de treino X_treino.
    </li>
    <li>
      <code>normalizador_y.fit(y_treino)</code>: Ajusta o normalizador_y aos dados de treino y_treino.
    </li>
    <li>
      <code>X_treino = normalizador_x.transform(X_treino)</code>: Aplica a normalização aos dados de treino X_treino.
    </li>
    <li>
      <code>y_treino = normalizador_y.transform(y_treino)</code>: Aplica a normalização aos dados de treino y_treino.
    </li>
    <li>
      <code>X_teste = normalizador_x.transform(X_teste)</code>: Aplica a normalização aos dados de teste X_teste.
    </li>
    <li>
      <code>y_teste = normalizador_y.transform(y_teste)</code>: Aplica a normalização aos dados de teste y_teste.
    </li>
    <li>
      <code>X_treino = torch.tensor(X_treino, dtype=torch.float32)</code>: Converte a matriz de treino X_treino em um tensor do PyTorch com tipo de dado float32.
    </li>
    <li>
      <code>y_treino = torch.tensor(y_treino, dtype=torch.float32)</code>: Converte o vetor de treino y_treino em um tensor do PyTorch com tipo de dado float32.
    </li>
    <li>
      <code>X_teste = torch.tensor(X_teste, dtype=torch.float32)</code>: Converte a matriz de teste X_teste em um tensor do PyTorch com tipo de dado float32.
    </li>
    <li>
      <code>y_teste = torch.tensor(y_teste, dtype=torch.float32)</code>: Converte o vetor de teste y_teste em um tensor do PyTorch com tipo de dado float32.
    </li>
  </ul>
</details>

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
