import AlgoritmoGenetico


def main():
    populacaoInicial = AlgoritmoGenetico.geraPopulacaoInicial()

    for k in range(300):
        # print("################# Pais Selecionados #################")
        pais = AlgoritmoGenetico.selecaoDePaisTorneio(populacaoInicial, 5,
                                                      len(populacaoInicial))

        descendentes = AlgoritmoGenetico.crossover(pais)
        for descendente in descendentes:
            print("geração: " + str(k) + " genes: " + descendente.getGenes() + " - fitness: " + str(descendente.fitness()))
        populacaoInicial = descendentes

    print("############### POPULACAO FINAL ###############")
    for fim in populacaoInicial:
        print("fim: " + fim.getGenes() + " - fitness: " + str(fim.fitness()))


if __name__ == "__main__":
    main()
