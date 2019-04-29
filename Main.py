import math

import matplotlib.pyplot as plt
import AlgoritmoGenetico
import numpy as np
from Populacao import Populacao
from setup import Variaveis


def main():
    populacoes = []

    populacaoInicial = AlgoritmoGenetico.geraPopulacaoInicial()
    populacoes.append(Populacao(populacaoInicial))

    historicoMelhorFitness = []
    historicoFitnessMedio = []

    for k in range(Variaveis.numMaximoGeracoes):
        # print("################# Pais Selecionados #################")
        pais = AlgoritmoGenetico.selecaoDePaisTorneio(populacaoInicial, 5,
                                                      len(populacaoInicial))

        descendentes = AlgoritmoGenetico.crossover(pais)
        for descendente in descendentes:
            print("geração: " + str(k) + " genes: " + descendente.getGenes() + " - fitness: " + str(
                descendente.fitness()))
        populacaoInicial = descendentes
        populacoes.append(Populacao(descendentes))

    print("############### POPULACAO FINAL ###############")
    for fim in populacaoInicial:
        print("fim: " + fim.getGenes() + " - fitness: " + str(fim.fitness()))

    print("############### MELHOR FITNESS - MEDIA ###############")
    for pop in populacoes:
        historicoMelhorFitness.append(pop.calculaFitnessMedioEMelhorFitness()[0])
        historicoFitnessMedio.append(pop.calculaFitnessMedioEMelhorFitness()[1])
        print(pop.calculaFitnessMedioEMelhorFitness())

    plt.plot(historicoMelhorFitness)
    plt.plot(historicoFitnessMedio)

    plt.legend(['Melhor Fitness', 'Fitness Médio'], loc='down right')

    plt.show()


if __name__ == "__main__":
    main()
