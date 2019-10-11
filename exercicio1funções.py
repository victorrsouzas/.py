"""Crie uma função que realize a conversão de Polegadas (pol) 
para Centímetros (cm), onde pol é passado como parâmetro e cm é retornado.
 Sabe-se que 1 polegada está para 2,54 centímetros."""
 
polegadas = 0

def conversao():
    global polegadas
    polegadas = float(input("Digite quantas polegadas você quer converter: \n"))
    converter = polegadas * 2.54
    print(f"De {polegadas} polegadas para centrimetros é igual a {converter}")
    
    return polegadas


conversao()
