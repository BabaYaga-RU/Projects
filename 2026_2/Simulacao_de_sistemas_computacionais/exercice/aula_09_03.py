import os
import warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
# ==============================================================
# Desafio
'''
A prefeitura quer otimizar o atendimento em uma
Unidade Básica de Saúde (UBS), onde há filas longas e
tempo de espera elevado. Você deve modelar e simular
o fluxo de pacientes para propor melhorias.
Dados Necessários
• Número médio de pacientes por hora
• Tempo médio de atendimento por profissional
• Número de profissionais disponíveis
• Horário de funcionamento
'''

# Etapas para otimizar o atendimento de uma UBS com simulação computacional
'''
1
Definição do Problema
• Identifique os principais gargalos: filas longas, tempo
de espera elevado, sobrecarga de profissionais.
• Estabeleça objetivos claros: reduzir tempo de espera,
melhorar fluxo de pacientes, aumentar a eficiência.

2
Coleta de Dados
• Levante dados reais da UBS:
✓ Número de pacientes por dia
✓ Tempo médio de atendimento por tipo de serviço
(consulta, vacinação, triagem)
✓ Número de profissionais disponíveis
✓ Horários de pico
• Registre eventos e tempos de espera em diferentes
etapas do atendimento.

3
Modelagem do Sistema
• Escolha uma ferramenta de simulação.
• Modele o fluxo de pacientes:
Chegada → Triagem → Atendimento médico → Saída
• Inclua recursos limitados (salas, médicos, enfermeiros)
e regras de prioridade (ex: urgência).

4
Validação do Modelo
• Compare os resultados da simulação com os dados
reais da UBS.
• Ajuste parâmetros até que o modelo represente
fielmente a realidade.
'''
# Etapas para otimizar o atendimento de uma UBS com simulação computacional
'''
Simulação de Cenários

• Teste diferentes estratégias:
• Aumento de profissionais em
horários de pico
• Separação de fluxo por tipo
de atendimento
• Implementação de
agendamento prévio
• Atendimento por ordem
de prioridade clínica
• Avalie os impactos em
tempo de espera, utilização
de recursos e satisfação dos
pacientes.

Análise dos Resultados

• Gere gráficos e relatórios
com os indicadores-chave:
• Tempo médio de espera
• Taxa de utilização dos
profissionais
• Número de pacientes
atendidos por hora
• Compare os cenários
simulados para identificar
o mais eficiente.

Proposta de Melhoria

• Com base nos resultados,
elabore um plano de ação:
• Mudanças operacionais
• Reorganização de equipes
• Investimentos em Tecnologia
ou infraestrutura
• Apresente os benefícios
esperados com dados da
simulação.
'''
# Implementação e Monitoramento
'''
• Aplique as melhorias na UBS em fases, se possível.
• Monitore os indicadores após a implementação
para validar os ganhos.
• Refaça simulações periodicamente para ajustar o
sistema conforme novas demandas.
'''