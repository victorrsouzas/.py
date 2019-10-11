"""Faça um programa que manipula uma lista com informações de 4 carros,
contendo os modelos do carro e seu consumo (km/l), como no seguinte exemplo:
[[‘Vectra’, 9], [‘Gol’, 10], [‘Fit’, 12.5]]. O programa deve preencher uma lista no
mesmo formato do exemplo acima e mostrar na tela o nome do modelo mais
econômico. Além disso, deve mostrar na tela quanto cada um desses modelos gastaria
para percorrer 1000 Km, assumindo que o valor do litro da gasolina é R$ 4,50."""

lista_carros = []
gasto_total = []


for c in range(4):
    modelo = input()
    consumo = float(input())
    lista_carros.append([modelo,consumo])
    gasto = ((1000/consumo)*4.50)
    gasto_total.append([modelo, gasto])
    
    
print(lista_carros)
print(gasto_total)


