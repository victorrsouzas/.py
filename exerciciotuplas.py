"""Faça um programa que armazene a altura e nome de 10 pessoas, apenas se a
altura for menor ou igual a 1.70. Por fim, adicione-os em uma tupla onde o primeiro
index será para os nomes e o segundo para as alturas."""

alturas = []
nomes = []

for c in range(10):
    altura = float(input("altura: "))
    if altura <= 1.70:
        alturas.append(altura)
        nomes.append(input("nome: "))
        
print(nomes, alturas)
