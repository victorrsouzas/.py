"""Exercício
○ Faça um programa que verifica se um palavra digitada pelo usuário
é um palíndromo (Palavras ou números que são iguais mesmo
sendo lidos de trás para frente). Informe ao usuário."""

palavra=input()#entrada do usuario
total=len(palavra)#tamanho total da palavra
contador = 0
for c in range(0,total):#repetição de zero ao total da palavra
    x = total-c-1
    if palavra[x] == palavra[c]:
        contador += 1
        
if contador == total:
    print("É um palindromo")
else:
    print("Nao e um palindromo")
    

palavra = input()
total = len(palavra)
contador = 0

for c in range(0, total):
    x = total-c-1
    if palavra[x] == palavra[c]:
        contador += 1
if total == contador:
    print("Palindromo")
else:
    print("Não é palindromo")



