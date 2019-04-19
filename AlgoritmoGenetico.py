import numpy

def calcula_fitness(equation_inputs, pop):
    # Calculating the fitness value of each solution in the current population.
    # The fitness function calulates the sum of products between each input and its corresponding weight.
    fitness = numpy.sum(pop * equation_inputs, axis=1)
    return fitness


def selecao_de_pais(populacao, fitness, quantidade_pais):
    # Selecting the best individuals in the current generation as parents for producing the offspring of the next generation.
    pais = numpy.empty((quantidade_pais, populacao.shape[1]))
    print("antes do for")
    print(pais)

    for parent_num in range(quantidade_pais):
        max_fitness_idx = numpy.where(fitness == numpy.max(fitness))
        max_fitness_idx = max_fitness_idx[0][0]
        pais[parent_num, :] = populacao[max_fitness_idx, :]
        fitness[max_fitness_idx] = -99999999999
        return pais


def crossover(pais, ponto_de_corte):
    offspring = numpy.empty(ponto_de_corte)
    # The point at which crossover takes place between two parents. Usually, it is at the center.
    crossover_point = numpy.uint8(ponto_de_corte[1] / 2)

    for k in range(ponto_de_corte[0]):
        # Index of the first parent to mate.
        parent1_idx = k % pais.shape[0]
        # Index of the second parent to mate.
        parent2_idx = (k + 1) % pais.shape[0]
        # The new offspring will have its first half of its genes taken from the first parent.
        offspring[k, 0:crossover_point] = pais[parent1_idx, 0:crossover_point]
        # The new offspring will have its second half of its genes taken from the second parent.
        offspring[k, crossover_point:] = pais[parent2_idx, crossover_point:]
    return offspring


def mutacao(offspring_crossover):
    # Mutation changes a single gene in each offspring randomly.
    for idx in range(offspring_crossover.shape[0]):
        # The random value to be added to the gene.
        random_value = numpy.random.uniform(-1.0, 1.0, 1)
        offspring_crossover[idx, 4] = offspring_crossover[idx, 4] + random_value
    return offspring_crossover
