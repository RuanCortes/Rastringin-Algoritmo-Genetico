import numpy

""" Parametros populacao """
individuos = [4, -2, 3.5, 5, -11, -4.7]
quantidade_individuos = len(individuos)  # Numero de individuos


""" Parametros algoritmo genetico """
selecionados_por_populacao = 8
quantidade_pais_selecionados = 4
numero_geracoes = 5

tamanho_populacao = (selecionados_por_populacao, quantidade_individuos)
populacao_inicial = numpy.random.uniform(low=-4.0, high=4.0, size=tamanho_populacao)


""" Parametros EP """
menor_fracao_intervalo = 10 / 1023