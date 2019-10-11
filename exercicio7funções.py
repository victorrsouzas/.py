"""Faça um programa com uma função chamada soma_imposto. A função
possui dois parâmetros formais: taxa_imposto, que é a quantia de imposto sobre vendas
expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função
“altera” o valor de custo para incluir o imposto sobre vendas se o valor do custo for
menor que R$1000."""

def soma_imposto():
    taxa_imposto = float(input("Taxa: "))
    custo = float(input("Custo: "))
    if custo < 1000:
        resultado = custo + (custo * (taxa_imposto/100))
        print(f"O valor do novo custo é {resultado}")
    else:
        resultado = custo
        print(f"Como o custo é maior que 1000 então fica o mesmo de {custo}")
    
    return resultado

soma_imposto()
