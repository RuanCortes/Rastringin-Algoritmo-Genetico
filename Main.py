import AlgoritmoGenetico
import Variaveis


def main():
    for geracao in range(Variaveis.numero_geracoes):
        # mensurar o fitness pra cada cromossomo da populacao
        fitness = AlgoritmoGenetico.calcula_fitness(Variaveis.individuos, Variaveis.nova_populacao)

        # selecao de melhores pais para crossover
        pais = AlgoritmoGenetico.selecao_de_pais(Variaveis.nova_populacao, fitness,
                                                 Variaveis.quantidade_pais_selecionados)

        # geracao de descendentes
        descendentes = AlgoritmoGenetico.crossover(pais,
                                                   comprimento_descendente=(
                                                       Variaveis.tamanho_populacao[0] - pais.shape[0],
                                                       Variaveis.quantidade_individuos))

        # mutacao de descendentes
        mutacao_descendentes = AlgoritmoGenetico.mutacao(descendentes, taxa_mutacao)

        # substituicao dos pais pelos filhos - atualizacao da populacao
        Variaveis.nova_populacao[0:pais.shape[0], :] = pais
        Variaveis.nova_populacao[pais.shape[0]:, :] = mutacao_descendentes


if __name__ == "__main__":
    main()
