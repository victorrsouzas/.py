"""Exercício
○ Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
■ 1. "Telefonou para a vítima?"
■ 2. "Esteve no local do crime?"
■ 3. "Mora perto da vítima?"
■ 4. "Devia para a vítima?"
■ 5. "Já trabalhou com a vítima?"
○ O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa
responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como
"Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente"."""

perguntas = []
respostas = []

for c in range(5):
    perguntas.append(str(input("Digite a pergunta: ")))
    respostas.append(str(input()))


soma = 0

for resposta in respostas:
    if resposta != 'nao' and resposta != 'NAO':
        soma += 1
        
if soma <= 2:
    print("suspeita")
elif soma > 2 and soma <= 4:
    print("Cúmplice")
elif soma > 4:
    print("Assassino")
        
