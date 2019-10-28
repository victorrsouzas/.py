"""O usuário deverá digitar uma frase. O programa irá imprimir na tela apenas a primeira e última palavra, concatenadas em uma única frase, com espaço entre elas."""

frase = input("Digite a frase: ")

ordenar = frase.split()

print(ordenar[0]+" "+ordenar[-1])
