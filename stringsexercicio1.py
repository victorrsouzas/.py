"""O usuário deverá digitar uma frase. O programa irá imprimir letra por letra na tela."""


frase = input("Digite uma frase: ")

for c in enumerate(frase):
    print(c)
