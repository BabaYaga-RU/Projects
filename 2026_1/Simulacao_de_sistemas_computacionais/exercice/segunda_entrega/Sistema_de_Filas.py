import random
import math
import matplotlib.pyplot as matplotlib
import numpy as numpy_np
import pandas as pandas_pd

def gerar_intervalos(tempo_medio):
    # X = -ln(U) / λ
    if tempo_medio <= 0:
        return 0
    
    u = random.random()
    if u == 0:
        u = 0.0001
    
    _lambda = 1.0 / tempo_medio
    
    return -math.log(u) / _lambda

def calcular_media(lista_numeros):
    if not lista_numeros:
        return 0
    
    # Otimizar com array e calcular media
    return numpy_np.mean(numpy_np.array(lista_numeros))

def calcular_estatistica(lista_numeros):
    if not lista_numeros:
        return {}
    
    array_otimizado =  numpy_np.array(lista_numeros)

    estatistica = {
        'media': numpy_np.mean(array_otimizado),
        'mediana': numpy_np.median(array_otimizado),
        'desvio_padrao': numpy_np.std(array_otimizado),
        'variancia': numpy_np.var(array_otimizado),
        'minimo': numpy_np.min(array_otimizado),
        'maximo': numpy_np.max(array_otimizado),
        'percentil_25': numpy_np.percentile(array_otimizado, 25),
        'percentil_50': numpy_np.percentile(array_otimizado, 50), #Mediana
        'percentil_75': numpy_np.percentile(array_otimizado, 75),
        'quantidade': len(array_otimizado)
    }

    return estatistica

def gerar_dataframe(resultados_simulacao):
    # Transformar em DataFrame (estilo Excel) e deixar na vertical usando T 
    data_frame = pandas_pd.DataFrame(resultados_simulacao).T

    # Dar nome a coluna dos valores
    data_frame.columns = ['valor']
    #Criar a linha sobre a configuracao da simulacao 
    data_frame.loc['Configuracao'] = 'Taxa Chegada: 3, Taxa Atendimento: 5, Tempo: 1000'

    return data_frame

def comparador_matematico(resultados_simulacao):
    dados_comparacao = {
        'Metrica': [
            'Tempo Medio no Sistema',
            'Tempo Medio na Fila',
            'Numero Medio no Sistema',
            'Numero Medio na Fila'
        ],
        'Simulado': [
            resultados_simulacao['tempo_medio_sistema_simulado'],
            resultados_simulacao['tempo_medio_fila_simulado'],
            resultados_simulacao['numero_medio_sistema_simulado'],
            resultados_simulacao['numero_medio_fila_simulado']
        ],
        'Teorico': [
            resultados_simulacao['tempo_medio_sistema_teorico'],
            resultados_simulacao['tempo_medio_fila_teorico'],
            resultados_simulacao['numero_medio_sistema_teorico'],
            resultados_simulacao['numero_medio_fila_teorico']
        ]
    }
    data_frame = pandas_pd.DataFrame(dados_comparacao)

    # Calcular diferenca 
    data_frame['Diferenca'] =  data_frame['Simulado'] - data_frame['Teorico']
    data_frame['Erro (%0)'] = data_frame['Simulado'] / data_frame['Teorico'] * 100

    return data_frame

def exportar(data_frame):
    try:
        data_frame.to_excel('dataframe.xlxs', index = False)
    except Exception as e:
        print('Erro ao exportar')