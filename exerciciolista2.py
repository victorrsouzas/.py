"""Exercício
○ Preencher uma lista com 10 números inteiros, usando input;
○ Mostrar os valores armazenados na lista;
○ Informar o menor elemento da lista usando o min();
○ Informar o maior elemento da lista e seu índice sem o uso de
funções;
○ Informar quantos valores ímpares existem na lista."""

lista = []

for c in range(10):
    lista.append(int(input()))
    
print(lista)
minimo = min(lista)
maximo = max(lista)
posicao_maximo = lista.index(maximo)

print(f'{minimo}, {maximo}, {posicao_maximo}')

soma = 0

#Dps do in tem que usar a lista principal
for listas in lista:
    if listas % 2 != 0: #pego a lista secundaria varro só atras dos impares.
        soma += 1 #uso pra contar a qtd de vezes
        
print(f"valor da qtd de impares é {soma}")
