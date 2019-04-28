import random

import numpy


class Individuo(object):

    # Initializer
    def __init__(self):
        self.genes = []  # inicializa array de genes do individuo

    #def __init__(self, gene):
    #    self.genes = [int(x) for x in str(gene).split("-")]

    def getX(self):
        geneXStr = ""
        for digit in self.genes[0:10]:
            geneXStr += str(digit)
        coord = int(geneXStr, 2)
        return (coord * 0.00978) - 5

    def getY(self):
        geneXStr = ""
        for digit in self.genes[10:20]:
            geneXStr += str(digit)
        coord = int(geneXStr, 2)
        return (coord * 0.00978) - 5

    def getGenes(self):
        geneXStr = ""
        for digit in self.genes:
            geneXStr += str(digit)
        return geneXStr

    def setCromossomo(self, cromossomo):
        self.genes = cromossomo

    def convertBinToDec(self, valor):
        return float(str(valor), 2)

    def crossover(self, individuo):
        # implementacao do crossover
        return individuo

    def mutacao(self, probabilidade):
        for gene in range(self.genes):
            # The random value to be added to the gene.
            if numpy.random.uniform(0.0, 1.0) < probabilidade:
                if gene == 1:
                    self[gene] == 0
                else:
                    self[gene] == 1

    def geraGenesAleatorios(self):
        self.genes = []
        for x in range(20):
            # self.genes.append(bool(random.getrandbits(1)))
            self.genes.append(random.choice([0, 1]))

        return self

    def fitness(self):
        x = self.getX()
        y = self.getY()

        resultadoFuncao = 20 + (x*x) + (y*y) - (10 * ((numpy.math.cos(2 * numpy.math.pi * x) + numpy.math.cos(2 * numpy.math.pi * y))))

        return (80.7046745258618 - resultadoFuncao)