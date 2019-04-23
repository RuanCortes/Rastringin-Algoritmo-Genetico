class Populacao(object):

    # Initializer
    def __init__(self):
        self.individuos = []
        self.fitnessMedio = -1
        self.melhorFitness = -1

    def adicionaIndividuo(self, individuo):
        self.individuos.append(self, individuo)
