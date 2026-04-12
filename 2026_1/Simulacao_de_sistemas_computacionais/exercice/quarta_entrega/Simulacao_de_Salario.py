import simpy
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

MINUTO_HORA = 60
MINUTO_DIA = 24 * MINUTO_HORA
DIAS_SIMULACAO = 14
REPLICACOES = 30

def obter_capacidade(tempo_atual, parametros):
    dia = int(tempo_atual // MINUTO_DIA)
    dia_semana = dia % 7
    minuto_dia = tempo_atual % MINUTO_DIA
    if dia_semana < 5:
        if (8 * MINUTO_HORA <= minuto_dia) and (minuto_dia < 12 * MINUTO_HORA):
            return parametros['producao_manha'], parametros['admin_manha']
        elif (13 * MINUTO_HORA <= minuto_dia) and (minuto_dia < 17 * MINUTO_HORA):
            return parametros['producao_tarde'], parametros['admin_tarde']
    return 0, 0


class SetorSalario:

    def __init__(self, ambiente, parametros):
        self.ambiente = ambiente
        self.parametros = parametros
        self.servidores_producao = simpy.Store(ambiente)
        self.servidores_admin = simpy.Store(ambiente)
        self.current_cap_producao = 0
        self.current_cap_admin = 0
        self.dados = []
        self.ambiente.process(self.atualizar_recursos())

    def atualizar_recursos(self):
        while True:
            cap_producao, cap_admin = obter_capacidade(self.ambiente.now, self.parametros)

            if cap_producao > self.current_cap_producao:
                for _ in range(cap_producao - self.current_cap_producao):
                    yield self.servidores_producao.put(object())
            elif cap_producao < self.current_cap_producao:
                for _ in range(self.current_cap_producao - cap_producao):
                    if self.servidores_producao.items:
                        yield self.servidores_producao.get()
            self.current_cap_producao = cap_producao

            if cap_admin > self.current_cap_admin:
                for _ in range(cap_admin - self.current_cap_admin):
                    yield self.servidores_admin.put(object())
            elif cap_admin < self.current_cap_admin:
                for _ in range(self.current_cap_admin - cap_admin):
                    if self.servidores_admin.items:
                        yield self.servidores_admin.get()
            self.current_cap_admin = cap_admin

            yield self.ambiente.timeout(1)


def processo_funcionario(ambiente, setor, fluxo):
    chegada = ambiente.now
    servidores = setor.servidores_producao if fluxo == 'producao' else setor.servidores_admin
    current_capacity = setor.current_cap_producao if fluxo == 'producao' else setor.current_cap_admin

    capacidade_fila = 30 if fluxo == 'producao' else 20
    tempo_servico = 15 if fluxo == 'producao' else 20

    funcionarios_no_sistema = len(servidores.get_queue) + (current_capacity - len(servidores.items))

    if funcionarios_no_sistema < capacidade_fila:
        token = yield servidores.get()
        espera = ambiente.now - chegada
        setor.dados.append({'fluxo': fluxo, 'espera': espera})
        yield ambiente.timeout(tempo_servico)
        yield servidores.put(token)
    else:
        setor.dados.append({'fluxo': fluxo, 'evento': 'bloqueio', 'tempo': ambiente.now})


def gerador_chegadas(ambiente, setor, fluxo, taxa_hora):
    taxa_minuto = taxa_hora / 60.0
    while True:
        yield ambiente.timeout(random.expovariate(taxa_minuto))
        ambiente.process(processo_funcionario(ambiente, setor, fluxo))


def executar_replicacao(parametros, semente):
    random.seed(semente)
    ambiente = simpy.Environment()
    setor = SetorSalario(ambiente, parametros)
    ambiente.process(gerador_chegadas(ambiente, setor, 'producao', 5))
    ambiente.process(gerador_chegadas(ambiente, setor, 'admin', 4))
    ambiente.run(until=DIAS_SIMULACAO * MINUTO_DIA)
    return pd.DataFrame(setor.dados)


parametros_ampliado = {
    'producao_manha': 3,
    'producao_tarde': 3,
    'admin_manha': 2,
    'admin_tarde': 2
}

resultados = [executar_replicacao(parametros_ampliado, s) for s in range(REPLICACOES)]
df_final = pd.concat(resultados)
print(df_final.groupby('fluxo')['espera'].mean())

parametros_anterior = {
    'producao_manha': 1,
    'producao_tarde': 1,
    'admin_manha': 1,
    'admin_tarde': 1
}

resultados_anterior = [executar_replicacao(parametros_anterior, s) for s in range(REPLICACOES)]
df_anterior = pd.concat(resultados_anterior)

resultados_ampliado = [executar_replicacao(parametros_ampliado, s) for s in range(REPLICACOES)]
df_ampliado = pd.concat(resultados_ampliado)

df_anterior['dia'] = (df_anterior.index // MINUTO_DIA).astype(int)
df_ampliado['dia'] = (df_ampliado.index // MINUTO_DIA).astype(int)

atend_anterior = df_anterior.groupby(['dia', 'fluxo']).size().unstack(fill_value=0)
atend_ampliado = df_ampliado.groupby(['dia', 'fluxo']).size().unstack(fill_value=0)

plt.figure(figsize=(10, 6))

plt.plot(atend_anterior.index, atend_anterior['producao'],
         label='Produção - Antes', color='blue', linestyle='-', marker='o')

plt.plot(atend_ampliado.index, atend_ampliado['producao'],
         label='Produção - Depois', color='green', linestyle='--', marker='s')

plt.plot(atend_anterior.index, atend_anterior['admin'],
         label='Administrativo - Antes', color='red', linestyle='-', marker='^')

plt.plot(atend_ampliado.index, atend_ampliado['admin'],
         label='Administrativo - Depois', color='purple', linestyle='--', marker='d')

plt.xlabel("Dias da Simulação", fontsize=12)
plt.ylabel("Número de Atendimentos", fontsize=12)
plt.title("Comparação de Atendimentos - Antes e Depois da Ampliação", fontsize=14, fontweight='bold')
plt.legend(loc='best', fontsize=10)
plt.grid(True, alpha=0.3)

plt.show()

print("\n=== ESTATÍSTICAS DO CENÁRIO ANTERIOR ===")
print(df_anterior.groupby('fluxo')['espera'].describe())

print("\n=== ESTATÍSTICAS DO CENÁRIO AMPLIADO ===")
print(df_ampliado.groupby('fluxo')['espera'].describe())

media_espera_anterior = df_anterior.groupby('fluxo')['espera'].mean()
media_espera_ampliado = df_ampliado.groupby('fluxo')['espera'].mean()

print("\n=== REDUÇÃO PERCENTUAL NO TEMPO DE ESPERA ===")
for fluxo in ['producao', 'admin']:
    reducao = ((media_espera_anterior[fluxo] - media_espera_ampliado[fluxo]) / media_espera_anterior[fluxo]) * 100
    print(f"{fluxo.capitalize()}: {reducao:.1f}% de redução")

bloqueios_anterior = df_anterior[df_anterior['evento'] == 'bloqueio'].shape[0] if 'evento' in df_anterior.columns else 0
bloqueios_ampliado = df_ampliado[df_ampliado['evento'] == 'bloqueio'].shape[0] if 'evento' in df_ampliado.columns else 0

print(f"\nBloqueios (funcionários que desistiram):")
print(f"  Cenário anterior: {bloqueios_anterior}")
print(f"  Cenário ampliado: {bloqueios_ampliado}")
