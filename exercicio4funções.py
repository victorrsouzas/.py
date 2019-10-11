"""Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais:
#taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o
#custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto
#sobre vendas."""


def soma_imposto():
    taxaImposto = float(input())
    custo = float(input())
    resultado = custo + (custo * (taxaImposto/100))
    print(f" O valor com a inclusão do imposto é {resultado:.2f}")
    return resultado

soma_imposto()



    
