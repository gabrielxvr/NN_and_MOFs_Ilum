import numpy as np

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