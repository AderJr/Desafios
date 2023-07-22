import math

def achar_digitos_Fibonacci():
    verdadeiro = False
    numI = 1
    numF = 1
    numAtual = 1
    indFibonacci = 2
    numDigitsMin = 3

    while not verdadeiro:
        numI = numF
        numF = numAtual
        numAtual = numI + numF
        indFibonacci = indFibonacci + 1

        numDigits = math.floor(math.log(numAtual, 10) + 1)
        if numDigits >= numDigitsMin:
            verdadeiro = True

    resultado = f'''
    Número buscado: {numAtual}
    Número de dígitos: {numDigits}
    Índice de Fibonacci: {indFibonacci}'''
    print(resultado)

achar_digitos_Fibonacci()