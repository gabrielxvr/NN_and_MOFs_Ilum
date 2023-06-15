import os
import requests
from pymatgen.core.structure import Structure
import numpy as np
import pandas as pd
import random as rd
from matminer.featurizers.structure import GlobalSymmetryFeatures
from matminer.featurizers.composition import ElementProperty

def funcao_extrair_features_cif(dataframe):
    """Essa função gera, a partir dos dados de cif de cada material, novas colunas contendo as propriedades contidas nas cifs: cada átomo do material e cada posição.
    
    Args:
        dataframe: conjunto de dados do problema
    
    Return:
        Um novo dataframe contendo novas colunas relativas aos dados da cif
    """

def adsorptions_MOF(mof):
    """Extrai as adsorções de cada MOF
    
    Args:
        mof: linha do dataframe
    
    Return:
        lista contendo os dados de absorção contidos no dataframe e lista contendo as informações
    """
    infs = []
    adsorps = []
    
    for trabalho in mof:
        for experimento in trabalho['isotherm_data']:
            informacao = trabalho['adsorbates'][0]['formula'] + '_' + str(experimento['pressure'])
            dado = experimento['total_adsorption']
            infs.append(informacao)
            adsorps.append(dado)
    
    return infs, adsorps



def funcao_extrair_features_isotherms(df):
    """Essa função gera, a partir dos dados de isotherm de cada material, novas colunas contendo as propriedades contidas nos isotherms: adsorção de gases em pressões variadas.
    
    Args:
        df: conjunto de dados do problema

    Return:
        Um novo dataframe contendo novas colunas relativas aos dados de isotherm
    """
    dataframe = df.copy()
    
    informacoes = adsorptions_MOF(dataframe['isotherms'][0])[0]
    
    CO2_0_01 = []
    CO2_0_1 = []
    CO2_2_5 = []
    CO2_0_05 = []
    CO2_0_5 = []
    N2_0_09 = []
    N2_0_9 = []
    CH4_2_5 = []
    CH4_4_5 = []
    CH4_0_05 = []
    CH4_0_5 = []
    CH4_0_9 = []
    CH4_35 = []
    Xe_1 = []
    Xe_5 = []
    Xe_10 = []
    H2_2 = []
    H2_100 = []
    
    lista_informacoes = [CO2_0_01, CO2_0_1, CO2_2_5, CO2_0_05, CO2_0_5, N2_0_09, N2_0_9, CH4_2_5, CH4_4_5, CH4_0_05, CH4_0_5, CH4_0_9, CH4_35, Xe_1, Xe_5, Xe_10, H2_2, H2_100]
    
    for mof in dataframe['isotherms']:
        adsorptions = adsorptions_MOF(mof)
        if adsorptions[0] == informacoes:
            ind = 0
            for informacao in lista_informacoes:
                informacao.append(adsorptions[1][ind])
                ind += 1
        else:
            ind = 0
            for informacao in lista_informacoes:
                informacao.append(np.nan)
                ind += 1
                
    for informacao1, informacao2 in zip(informacoes, lista_informacoes):
        dataframe[informacao1] = informacao2
        
    dataframe = dataframe.drop('isotherms', axis=1)    
    
    return dataframe


def count_freq_chemical(df_elements,minimo):
    '''
    Função que conta a frequencia do elemento por coluna. Remove se tudo zero ou se não atingir o minimo de frequencia estabelecido pelo usuário,
    
    Args:
        df_elements: DataFrame com os elementos quimicos.
        minimo: frequencia minima de elementos quimicos, avaliado por coluna.
        
    Returns:
        DataFrame com elementos de frequencia maior ou igual que o estabelecido pelo usuario.
        
    '''
    
    df_elements = df_elements.loc[:, (df_elements != 0).any(axis=0)] #retira colunas com zeros
    df_elements_range = [p for p in range(0,df_elements.shape[1])] #range de colunas
    

    list_non_zeros = [] #lista que armazena frequencia de elementos non-zero
    for i in df_elements_range:
        non_zeros = np.count_nonzero(df_elements.iloc[:,i]) #iterar em cada coluna
        list_non_zeros.append(non_zeros) #armazenar frequencias

    for non_zeros_index,element_index in zip(df_elements_range,df_elements_range):
        if list_non_zeros[non_zeros_index] < minimo: #se frequencia retirada < minimo de frequencia de elementos
            df_elements.iloc[:,element_index] = np.full((df_elements.iloc[:,element_index].shape[0],1),np.nan) #substituir valores coluna por NaN
    df_elements = df_elements.dropna(axis=1) #dropar valores NaN
    #display(df_elements) #exibir se necessário
    return df_elements



def extrair_cif(df_mof,minimo):
    '''
    Função que extrai features estruturais-quimicas de strings .CIF contidas em dicionários tipo .json extraídos da API.

    Args:
        df_mof = DataFrane com informações fisico-quimicas das MOF's, extraídas da coluna de CIF's.
        minimo = numero minimo de ocorrências de elementos químicos no DataFrame.

    Returns:
        DataFrame contendo propriedades quimico-conformacionais das CIF's da pasta selecionada.
    '''
    #modificado de: https://matsci.org/t/how-to-extract-structure-features-from-cif-collection-question-from-jason/3111

    structures = [Structure.from_str(mof_cif,fmt='cif') for mof_cif in df_mof['cif']] #transforma as strings de .cif em .cif, provenientes da API.
    df = pd.DataFrame({"structure": structures, "composition": [s.composition for s in structures]}) #coloca os arquivos em um DataFrame

    gsf = GlobalSymmetryFeatures() #extrai propriedades estruturais dos CIF's
    df = gsf.featurize_dataframe(df, 'structure', ignore_errors=True, return_errors=True) #transforma as estruturas em features e coloca em df

    ep = ElementProperty.from_preset("matminer") #extrai propriedades elementares dos CIF's
    df = ep.featurize_dataframe(df, "composition", ignore_errors=True, return_errors=True) #transforma as estruturas em features e coloca em df
    #df.to_csv('df_all_cif.csv',index=False) #exportar toda a tabela se necessário
    #print('df_sem_corte', df)

    df = df.iloc[:,1:7] #corta o dataframe por index especificos

    composition_list = [] #armazena os dicts com os elementos e suas quantidades nas MOF's
    for i in range(0,len(df['composition'])):
        composition_list.append(df['composition'][i].as_dict()) #converte type Structures em dict
    df_composition = pd.DataFrame(composition_list).fillna(float(0)) #DataFrame com os dados estruturais-quimicos; troca NaN por zeros
    df_composition = count_freq_chemical(df_composition,minimo) #teste pls
    
    df = df.drop(['composition'],axis=1) #retura a coluna 'composition', já foi desempacotada
    df_composition_cif = pd.concat([df,df_composition],axis=1) #une os dados estruturais-quimicos com o DataFrame principal
    
    df_mof = df_mof.drop(labels='cif', axis=1)
    df_mof = pd.concat([df_mof,df_composition_cif],axis=1)
    
    #display(df_composition_cif) #exibir se necessário
    #df_composition_cif.to_csv('df_composition_cif.csv',index=False) #exportar tabela se necessário
    return df_mof

def gene_mof(valor_max, valor_min):
    """Gera um gene válido para as mofs
    
    Args:
        valor_max: Valor máximo do gene
        valor_min: Valor mínimo do gene
    
    Return:
        Um valor entre o mínimo e o máximo.
    """
    gene = rd.randint(valor_min, valor_max)
    return gene

def individuo_mof(n, valor_max_elementos):
    """Gera um indivíduo para o problema das mofs
    
    Args:
        n: número de elementos presentes
        valor_max_elementos: Quantidade máxima de cada elemento da mof
        
    Return:
        Uma lista com n genes.
    """
    gene_spacegroup_num = gene_mof(230, 1)
    gene_crystal_system_int = gene_mof(7, 1)
    gene_n_symmetry_ops = gene_mof(12, 1)
    individuo = [gene_spacegroup_num, gene_crystal_system_int, gene_n_symmetry_ops]
    
    for _ in range(n):
        gene = gene_mof(valor_max_elementos, 0)
        individuo.append(gene)
    return individuo

def populacao_mof(tamanho, n, valor_max_elementos):
    """Cria uma população para o problema das mofs
    
    Args:
        tamanho: Número de Indivíduos
        n: número de elementos presentes
        valor_max_elementos: Quantidade máxima de cada elemento da mof
    
    Return:
        Uma lista contendo cada indivíduo
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_mof(n, valor_max_elementos))
    return populacao

def cruzamento_ponto_simples(pai, mae):
    """Operador de cruzamento de ponto simples
    
    Args:
        pai: uma lista representando um indivíduo
        mão: uma lista representando um indivíduo
    
    Returns:
        Duas listas, sendo que cada uma representa um filho dos pais que foram os argumentos
    """
    ponto_de_corte = rd.randint(1, len(pai) - 1)
    
    filho1 = pai[:ponto_de_corte] + mae[ponto_de_corte:]
    filho2 = mae[:ponto_de_corte] + pai[ponto_de_corte:]
    
    return filho1, filho2

def mutacao_mof(individuo, valor_max_elementos):
    """Realiza a mutação de um gene no problema das mofs
    
    Args:
        individuo: uma lista representando o individuo no problema das caixas binárias
        valor_max_elementos: Quantidade máxima de cada elemento da mof
        
    Return:
        Um indivíduo com um gene mutado.
    """
    gene_a_ser_mutado = rd.randint(0, len(individuo) - 1)
    if gene_a_ser_mutado == 0:
        individuo[gene_a_ser_mutado] = gene_mof(230, 1)
        
    elif gene_a_ser_mutado == 1:
        individuo[gene_a_ser_mutado] = gene_mof(7, 1)
    
    elif gene_a_ser_mutado == 2:
        individuo[gene_a_ser_mutado] = gene_mof(12, 1)
    
    else:
        individuo[gene_a_ser_mutado] = gene_mof(valor_max_elementos, 0)
    
    return individuo

def selecao_torneio_min(populacao, fitness, tamanho_torneio=3):
    """Faz a seleção de uma população usando torneio.
    Nota: da forma que está implementada, só funciona em problemas de
    minimização.
    Args:
      populacao: população do problema
      fitness: lista com os valores de fitness dos individuos da população
      tamanho_torneio: quantidade de invidiuos que batalham entre si
    Returns:
      Individuos selecionados. Lista com os individuos selecionados com mesmo
      tamanho do argumento `populacao`.
    """
    selecionados = []

    # criamos essa variável para associar cada individuo com seu valor de fitness
    par_populacao_fitness = list(zip(populacao, fitness))

    # vamos fazer len(populacao) torneios! Que comecem os jogos!
    for _ in range(len(populacao)):
        combatentes = rd.sample(par_populacao_fitness, tamanho_torneio)

        # é assim que se escreve infinito em python
        minimo_fitness = float("inf")

        for par_individuo_fitness in combatentes:
            individuo = par_individuo_fitness[0]
            fit = par_individuo_fitness[1]

            # queremos o individuo de menor fitness
            if fit < minimo_fitness:
                selecionado = individuo
                minimo_fitness = fit

        selecionados.append(selecionado)

    return selecionados