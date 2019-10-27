"""Faça um programa que inicialize uma lista vazia, solicite
ao usuário 10 números ímpares, um por vez. Caso o
número digitado seja par, solicite novamente um número,
até que o valor seja um número ímpar. Depois disso,
exiba os 10 números ímpares armazenados. Utilize
continue."""

lista = []

n = 0


while n >= 0:
    n = int(input("Digite o numero impar: "))
    if n % 2 == 0:
        print("Digite novamente o numero")
        continue
    if n % 2 != 0:
        lista.append(n)
    if len(lista) > 9:
        break
    
        
print(lista)
    
