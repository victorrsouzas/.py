"""Faça uma função que receba como parâmetro o arquivo acima, aberto para leitura e uma palavra que o usuário digitou. O retorno da função deve ser uma tupla, onde o primeiro índice é a quantidade de linhas que contém a palavra digitada pelo usuário e o segundo índice é uma lista com essas linhas. O programa principal deve exibir o primeiro e segundo índice da tupla, exibir o texto completo e fechar o arquivo.Saída: A quantidade de linhas que contém a palavra digitada é: [quantidade]           As linhas são: [lista com o texto das linhas]Texto completo"""

arquivo = "texto.txt"

def ler(arquivo):
    with open(arquivo,"r") as variavel:
        print(variavel.read())
        variavel.close
        return variavel

def questão3(arquivo):
    with open(arquivo,"r") as variavel:
        linhas = variavel.readlines()
        c = 0
        for linha in linhas:
            c +=1
        print(f"A quantidade de linhas que contém a palavra digitada é: {c}\n")
        print(f"As linhas são: {linhas}\n")
        print("             Texto Completo \n")
        ler(arquivo)
        variavel.close()
        return linhas
    
questão3(arquivo)
    
    
