"""Escreva um programa que lê duas notas de vários alunos e
armazena tais notas em um dicionário, onde a chave é o nome do
aluno. A entrada de dados deve terminar quando for lida uma
string vazia como nome. Por fim, deverá ser mostrado a média de
notas de cada aluno."""

notasfechado = {}
nome=""
def ler():      #função para ler
    global nome
    nome = input("Digite o nome:")
    return nome #retorno da função
while ler()!="":         #comparação.
    nota1 = float(input())
    nota2 = float(input())
    notas = dict({nome: [nota1,nota2]})
    notasfechado.update(notas)#pra atualizar as notas

print(notasfechado)

for notaa in notasfechado:
    media = sum(notasfechado[notaa])/len(notasfechado[notaa])
    print(f"A media de {notaa} é {media}")
    

