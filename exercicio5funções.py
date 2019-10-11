"""Implemente uma calculadora (numeros reais) com suas funções básicas: soma, subtração, multiplicação e divisão. O usuário deve informar dois numeros no programa principal e escolher a operação que quer efetuar(+, -, * ou /), o programa chamará a função de acordo com a operação escolhida"""

numero = 0
lista = []

def calculadora():
    global numero
    for c in range(2):
        numero = float(input())
        lista.append(numero)
    operação = str(input("Escolha a operação (+, -, * ou /): "))
    if operação == "+":
        soma(lista)
    elif operação == "-":
        subtração(lista)
    elif operação == "*":
        multiplicação(lista)
    elif operação == "/":
        divisão(lista)   
    
    return numero

def soma(lista):
    soma = sum(lista)
    print(f"A soma de {lista[0]} + {lista[1]} é igual {soma}")

def subtração(lista):
    sub = lista[0] - lista[1]
    print(f"A subtração de {lista[0]} - {lista[1]} é igual {sub}")
    
def multiplicação(lista):
    multi = lista[0] * lista[1]
    print(f"A multiplicação de {lista[0]} * {lista[1]} é igual {multi}")
    
def divisão(lista):
    div = lista[0] / lista[1]
    print(f"A divisão de {lista[0]} / {lista[1]} é igual {div:.2f}")
    
    
calculadora()
