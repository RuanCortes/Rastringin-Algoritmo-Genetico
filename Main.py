import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

import AlgoritmoGenetico
from Populacao import Populacao
from setup import Variaveis


def main():
    # guarda historico de todas as geracoes
    populacoes = []

    # populacao inicial
    populacaoInicial = AlgoritmoGenetico.geraPopulacaoInicial()
    populacoes.append(Populacao(populacaoInicial))

    # arrays para plotagem do grafico
    historicoMelhorFitness = []
    historicoFitnessMedio = []

    # executa algoritmo genetico ate um numero maximo de geracoes definido nos parametros do programa
    for k in range(Variaveis.numMaximoGeracoes):

        # seleciona pais para cruzamento
        pais = AlgoritmoGenetico.selecaoDePaisTorneio(populacaoInicial, 5,
                                                      len(populacaoInicial))

        # crossover e mutacao
        descendentes = AlgoritmoGenetico.crossover(pais)

        # imprime no console informacoes da geracao atual
        for descendente in descendentes:
            print("geração: " + str(k) + " genes: " + descendente.getGenes() + " - fitness: " + str(
                descendente.fitness()))

        # define a populacao de descendentes como principal e reinicia o processo
        populacaoInicial = descendentes

        # guarda historico da geracao
        populacoes.append(Populacao(descendentes))

    # exibicao no console de informacoes sobre a execucao do programa #
    print("############### POPULACAO FINAL ###############")
    for fim in populacaoInicial:
        print("fim: " + fim.getGenes() + " - fitness: " + str(fim.fitness()))

    print("############### MELHOR FITNESS - MEDIA ###############")
    for pop in populacoes:
        historicoMelhorFitness.append(pop.calculaFitnessMedioEMelhorFitness()[0])
        historicoFitnessMedio.append(pop.calculaFitnessMedioEMelhorFitness()[1])
        print(pop.calculaFitnessMedioEMelhorFitness())
    # FIM - exibicao no console de informacoes sobre a execucao do programa #

    # plotagem do grafico #
    fig, axs = plt.subplots(1, 1, constrained_layout=True)
    axs.plot(historicoMelhorFitness)
    axs.plot(historicoFitnessMedio)
    axs.set_title(
        'População total: ' + str(Variaveis.tamanhoPopulacao) + ' -  Gerações: ' + str(Variaveis.numMaximoGeracoes))
    axs.set_xlabel('geração')
    axs.set_ylabel('Fitness')
    axs.legend(['Melhor Fitness', 'Fitness Médio'], loc='lower right')
    axs.xaxis.set_major_locator(MaxNLocator(integer=True))

    plt.show()
    # salva imagem gerada
    # plt.savefig('relatorios/POPULACAO_' + str(Variaveis.tamanhoPopulacao) + '_GERACOES_' + str(Variaveis.numMaximoGeracoes) + '.png')

    # FIM plotagem do grafico #


if __name__ == "__main__":
    main()
