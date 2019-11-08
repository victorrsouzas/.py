"""Faça uma função que receba como parâmetro um arquivo aberto para escrita. Nessa função, obtenha textos do teclado até que o usuário digite “sair” (sem aspas). Grave os textos no arquivo, envie-o como retorno para o programa principal e feche-o."""

def escrita_arquivo():
    with open('arquivo2.txt','w') as variavel:
        n = ""
        while n != "sair":
            n = input()
            variavel.write(n)
            variavel.write("\n")
        variavel.close()
        return n

escrita_arquivo()

    
    
        
