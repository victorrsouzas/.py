"""Escreva um programa que lê duas notas de 10 alunos e armazena tais
notas em um dicionário, onde a chave é o nome do aluno. Por fim, deverá ser mostrado
a média de notas de cada aluno e o nome do aluno que obteve a maior média."""

dicionario = {}

for c in range(3):
    alunos = (input("nome: "))
    n1 = float(input("n1: "))
    n2 = float(input("n2: "))
    geral = dict({alunos: [n1, n2]})
    dicionario.update(geral)
    
print(dicionario)

media_geral = {}

for c in dicionario:
    media = sum(dicionario[c])/len(dicionario[c])
    quadro_media = dict({c: [media]})
    media_geral.update(quadro_media)
    #print(f"A media de {c} foi de {media}")
    maior = max(media_geral)
    
    
print(media_geral)
print(f"A maior media foi de {maior}")
    
