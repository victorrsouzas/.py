"""Dado um arquivo de texto, descubra quantas linhas ele tem."""

arquivo = "texto.txt"

def ler_arquivo(arquivo):
    with open(arquivo,'r') as variavel:
        print(variavel.read())
        variavel.close()
        return variavel
        
def contar_linhas(arquivo):
    with open(arquivo, 'r') as variavel:
        t = variavel.readlines()
        contador = 0
        for linha in t:
            contador +=1
        print(f'O numero total de linhas é {contador}')
        variavel.close()
        return t
    
    
ler_arquivo(arquivo)
contar_linhas(arquivo)
