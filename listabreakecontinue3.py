"""Faça um programa que armazene em uma lista a idade
de várias pessoas. O programa deve finalizar quando -1
for digitado. Informar a maior idade, a menor idade e a
média de idades. Utilize break."""



lista = []

idade = -1

while idade >= -1:
    idade = int(input("Digite sua idade: "))
    if idade == -1:
        break
    else:
        lista.append(idade)
        
print(lista)
maior = print(f'a maior idade é: {max(lista)}')
menor = print(f'a menor idade é: {min(lista)}')
media = print(f'a media das idades é: {sum(lista)/len(lista)}')
