import AlgoritmoGenetico
import setup.Variaveis as InitSetup
from Individuo import Individuo


def main():

    individuos = []
    for x in range(100):
        ind = Individuo().geraGenesAleatorios()
        print("fitness: " + str(ind.fitness()))
        individuos.append(ind)

    print(individuos.__len__())
    print(individuos)


if __name__ == "__main__":
    main()
