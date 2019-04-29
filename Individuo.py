import random

import numpy


class Individuo(object):

    # Initializer
    def __init__(self):
        self.genes = []  # inicializa array de genes do individuo

    # gera valor inteiro X com base nos 10 primeiros bits do cromossomo do individuo
    def getX(self):
        geneXStr = ""
        for digit in self.genes[0:10]:
            geneXStr += str(digit)
        coord = int(geneXStr, 2)
        return (coord * 0.00978) - 5

    # gera valor inteiro Y com base nos 10 primeiros bits do cromossomo do individuo
    def getY(self):
        geneXStr = ""
        for digit in self.genes[10:20]:
            geneXStr += str(digit)
        coord = int(geneXStr, 2)
        return (coord * 0.00978) - 5

    # retorna o cromossomo do individuo no formato string
    def getGenes(self):
        geneXStr = ""
        for digit in self.genes:
            geneXStr += str(digit)
        return geneXStr

    # atribui um cromossomo ao individuo
    def setCromossomo(self, cromossomo):
        self.genes = cromossomo

    # gera um cromossomo totalmente aleatorio
    def geraGenesAleatorios(self):
        self.genes = []
        for x in range(20):
            # self.genes.append(bool(random.getrandbits(1)))
            self.genes.append(random.choice([0, 1]))

        return self

    # calcula fitness do individuo
    def fitness(self):
        x = self.getX()
        y = self.getY()

        resultadoFuncao = 20 + (x * x) + (y * y) - (
                10 * ((numpy.math.cos(2 * numpy.math.pi * x) + numpy.math.cos(2 * numpy.math.pi * y))))

        return (80.7046745258618 - resultadoFuncao)
