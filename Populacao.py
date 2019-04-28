class Populacao(object):

    # Initializer
    def __init__(self, pop):
        self.individuos = pop

    def adicionaIndividuo(self, individuo):
        self.individuos.append(self, individuo)

    def calculaFitnessMedioEMelhorFitness(self):
        melhorFitness = 0
        fitnessTotal = 0


        for i in range(len(self.individuos)):
            # verifica melhor fitness da populacao
            if self.individuos[i].fitness() > melhorFitness:
                melhorFitness = self.individuos[i].fitness()

            # calcula fitness medio
            fitnessTotal += self.individuos[i].fitness()

        return melhorFitness, (fitnessTotal / len(self.individuos))
