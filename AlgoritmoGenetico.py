import random

import numpy

from Individuo import Individuo
from setup import Variaveis


def selecaoDePaisTorneio(populacao, qtdCompetidoresTorneio, qtdPais):
    pais = []
    for torneio in range(qtdPais):
        candidatosTorneio = []
        # seleciona qntCompetidores dos elementos da população de forma aleatoria para torneio
        for individuo in range(qtdCompetidoresTorneio):
            candidatosTorneio.append(random.choice(populacao))

        # verifica o elemento com menor fit
        paiVencedor = None
        for pai in candidatosTorneio:
            if paiVencedor == None:
                paiVencedor = pai
            else:
                if pai.fitness() > paiVencedor.fitness():
                    paiVencedor = pai

        # adiciona pai vencedor ao range de pais vencedores
        pais.append(paiVencedor)

    return pais


def crossover(pais):
    descendentes = []

    ponto_de_corte = numpy.uint8(
        random.randrange(Variaveis.possibilidadePontoDeCorteInicio, Variaveis.possibilidadePontoDeCorteFim))

    for k in range(Variaveis.tamanhoPopulacao):
        descendente = Individuo()

        pai_1 = k % len(pais)
        pai_2 = (k + 1) % len(pais)

        cromossomoFinal = pais[pai_1].genes[0:ponto_de_corte]

        for genePai2 in pais[pai_2].genes[ponto_de_corte:20]:
            cromossomoFinal.append(genePai2)

        descendente.setCromossomo(mutacao(cromossomoFinal, Variaveis.taxaDeMutacaoPorGene))

        descendentes.append(descendente)

    return descendentes


def mutacao(cromossomo, taxa_mutacao):
    cromossomoInicial = cromossomo
    houveMutacao = False
    for gene in range(20):
        if numpy.random.uniform(0.0, 1.0) < taxa_mutacao:
            houveMutacao = True
            if cromossomo[gene] == 1:
                cromossomo[gene] = 0
            else:
                cromossomo[gene] = 1
    return cromossomo


def geraPopulacaoInicial():
    individuos = []
    for x in range(Variaveis.tamanhoPopulacao):
        ind = Individuo().geraGenesAleatorios()
        individuos.append(ind)
    return individuos
