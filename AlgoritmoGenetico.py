import numpy
import relatorios.Execucao

def calcula_fitness(equation_inputs, pop):
    # Calculating the fitness value of each solution in the current population.
    # The fitness function calculates the sum of products between each input and its corresponding weight.
    fitness = numpy.sum(pop * equation_inputs, axis=1)
    return fitness


def selecao_de_pais(populacao, fitness, quantidade_pais):
    # Selecting the best individuals in the current generation as parents for producing the offspring of the next generation.
    pais = numpy.empty((quantidade_pais, populacao.shape[1]))

    for parent_num in range(quantidade_pais):
        max_fitness_idx = numpy.where(fitness == numpy.max(fitness))
        max_fitness_idx = max_fitness_idx[0][0]
        pais[parent_num, :] = populacao[max_fitness_idx, :]
        fitness[max_fitness_idx] = -99999999999
        return pais


def crossover(pais, comprimento_descendente):
    descendente = numpy.empty(comprimento_descendente)
    # The point at which crossover takes place between two parents. Usually, it is at the center.

    ponto_de_corte = numpy.uint8(comprimento_descendente[1] / 2)

    for k in range(comprimento_descendente[0]):
        #TODO: pegar pais de forma aleatoria mais confiavel
        # Index of the first parent to mate.
        pai_1 = k % pais.shape[0]
        # Index of the second parent to mate.
        pai_2 = (k + 1) % pais.shape[0]
        # The new offspring will have its first half of its genes taken from the first parent.
        descendente[k, 0:ponto_de_corte] = pais[pai_1, 0:ponto_de_corte]
        # The new offspring will have its second half of its genes taken from the second parent.
        descendente[k, ponto_de_corte:] = pais[pai_2, ponto_de_corte:]
    return descendente


def mutacao(descendente, taxa_mutacao):
    # TODO: Revisar este método para ver se está funcionando crretamente
    # Mutation changes a single gene in each offspring randomly.
    for gene in range(descendente.shape[0]):
        # The random value to be added to the gene.
        if numpy.random.uniform(0.0, 1.0) < taxa_mutacao:
            if gene == 1:
                descendente[gene] == 0
            else:
                descendente[gene] == 1
    return descendente
