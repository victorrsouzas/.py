"""Faça um programa que inicialize uma lista vazia, solicite
ao usuário números ímpares, um por vez. Caso o
número digitado seja par, encerre o programa. Depois
disso, exiba os números ímpares digitados. Utilize break."""

lista = []

n = 0

while n >= 0:
    n = int(input("Digite Seu numero impar: "))
    if n % 2 == 0:
        break
    else:
        lista.append(n)
        
print(lista)
