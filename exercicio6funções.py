"""Faça um programa que receba um valor em segundos e usando uma
função transforme-o em minutos. Em seguida, utilizando outra função, converta
de minutos para horas."""

segundos = 0

def conversão():
    global segundos
    segundos = int(input("Segundos: "))
    conversão = segundos / 60
    print(f"De {segundos}s para minutos é: {conversão}")
    conversão2(conversão)
    return segundos

def conversão2(conversão):
    horas = conversão / 60
    print(f"De {conversão}m para hora é igual a: {horas}")
    
    
conversão()
