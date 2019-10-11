"""Faça um programa que leia um número indeterminado de notas. O Programa
finalizará quando o usuário digitar uma nota negativa. Após esta entrada de dados, faça
o seguinte:
○ Mostre a quantidade de notas que foram lidas.
○ Exiba todas as notas na ordem em que foram informadas.
○ Exiba todas as notas na ordem inversa à que foram informadas.
○ Calcule e mostre a soma das notas.
○ Calcule e mostre a média das notas.
○ Calcule e mostre a quantidade de notas acima da média calculada."""

lista_nota = []
nota = 0


while nota >= 0:
    nota = float(input())
    lista_nota.append(nota)
    
print("--------------------------------------------")
lista_nota.pop()
tamanho = len(lista_nota)
print(tamanho)
print(lista_nota)
lista_nota.reverse()
print(lista_nota)
print(sum(lista_nota))
media = sum(lista_nota)/len(lista_nota) 
print(f"{media:.2f}")
soma = 0
for medias in lista_nota:
    if medias > media:
        soma += 1

print(soma)



    
