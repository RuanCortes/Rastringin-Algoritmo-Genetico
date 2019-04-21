def gera_populacao_aleatoria():
    #TODO: gera populacao aleatoria (10 bits - binario)
    return


def converte_coordenada_decimal_para_binario(coordenada, casas_decimais):

    # Function returns octal representation

    # split() seperates whole number and decimal
    # part and stores it in two seperate variables
    valor_inteiro, decimal = str(coordenada).split(".")

    # Convert both whole number and decimal
    # part from string type to integer type
    valor_inteiro = int(valor_inteiro)
    decimal = int(decimal)

    # Convert the whole number part to it's
    # respective binary form and remove the
    # "0b" from it.
    res = bin(valor_inteiro).lstrip("0b") + "."

    # Iterate the number of times, we want the number of decimal places to be
    for x in range(casas_decimais):

        # Multiply the decimal value by 2
        # and seperate the whole number part and decimal part
        valor_inteiro, decimal = str((converte_decimal(decimal)) * 2).split(".")

        # Convert the decimal part to integer again
        decimal = int(decimal)

        # Keep adding the integer parts
        # receive to the result variable
        res += valor_inteiro

    return res


# Function converts the value passed as parameter to it's decimal representation
def converte_decimal(num):
    while num > 1:
        num /= 10
    return num


print(converte_coordenada_decimal_para_binario(10.69, casas_decimais=2))


def normaliza_coordenada():
    return