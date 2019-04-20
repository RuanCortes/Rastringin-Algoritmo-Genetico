import numpy

"""
equation_inputs -> definir quantidade de individuos na população. cada, 10 genes cada individuo (10 bits).
cada gene deve ser aleatorio e binário (0 e 1).
Normalizar os valores inteiros desses individuos multiplicando
e retornar a população (vetores de binerios/individuos).
"""
# Inputs of the equation.
individuos = [4, -2, 3.5, 5, -11, -4.7]

# Number of the weights we are looking to optimize.
quantidade_individuos = len(individuos)  # Numero de individuos

""" Genetic algorithm parameters: Mating pool size - Population size """
selecionados_por_populacao = 8
quantidade_pais_selecionados = 4
numero_geracoes = 5
taxa_mutacao = 0.05

# Defining the population size.
tamanho_populacao = (selecionados_por_populacao, quantidade_individuos)
# Creating the initial population.
nova_populacao = numpy.random.uniform(low=-4.0, high=4.0, size=tamanho_populacao)

menor_fracao_intervalo = 10 / 1023