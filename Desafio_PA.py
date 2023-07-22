'''
15. Certo dia o professor de Johann Friederich Carl Gauss (aos 10 anos de idade)
mandou que os alunos somassem os números de 1 a 100. Imediatamente Gauss
achou a resposta – 5050 – aparentemente sem a soma de um em um. Supõe-se
que já aí, Gauss, houvesse descoberto a fórmula de uma soma de uma progressão
aritmética.
FAça um programa em Pascal que realize a soma de uma P.A. de n termos,
dado o primeiro termo a1 e o último termo an. A impressão do resultado deve
ser formatada com duas casas na direita.
Exemplo de entrada Saída esperada

n   | a1 | an   |soma
100 | 1  | 100  |5050.00
10  | 1  | 10   |55.00
50  | 30 | 100  |3250.00
'''

a1 = int(input("Informe o 1° termo: "))
an = int(input("Informe o ultimo termo: "))
n = int(input("Informe o total de termos: "))

somaPA = (a1+an) * (n/2)

print(f"Soma da PA: {somaPA:.2f}")