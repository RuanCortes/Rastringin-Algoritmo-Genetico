import AlgoritmoGenetico
import setup.Variaveis as InitSetup


def main():

    count = 0

    for geracao in range(InitSetup.numero_geracoes):
        # mensurar o fitness pra cada cromossomo da populacao
        fitness = AlgoritmoGenetico.calcula_fitness(InitSetup.individuos, InitSetup.populacao_inicial)

        # selecao de melhores pais para crossover
        pais = AlgoritmoGenetico.selecao_de_pais(InitSetup.populacao_inicial, fitness,
                                                 InitSetup.quantidade_pais_selecionados)

        # geracao de descendentes
        descendentes = AlgoritmoGenetico.crossover(pais,
                                                   comprimento_descendente=(
                                                       InitSetup.tamanho_populacao[0] - pais.shape[0],
                                                       InitSetup.quantidade_individuos))

        # mutacao de descendentes
        mutacao_descendentes = AlgoritmoGenetico.mutacao(descendentes)

        # substituicao dos pais pelos filhos - atualizacao da populacao
        InitSetup.populacao_inicial[0:pais.shape[0], :] = pais
        InitSetup.populacao_inicial[pais.shape[0]:, :] = mutacao_descendentes

        count = count + 1

    print("total de geracoes")
    print(count)

if __name__ == "__main__":
    main()
