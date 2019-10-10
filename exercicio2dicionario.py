"""Exercício
○ Faça um programa que crie um dicionário onde as chaves serão os
números de 1 a 15 e os valores serão o quadrado desses números.
○ Final esperado:
○ {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11:
121, 12: 144, 13: 169, 14: 196, 15: 225}"""

numerosDict = {}
x = 0
soma = 0
for c in range(15+1):
    numeros = dict({c: c**2})
    numerosDict.update(numeros)

del numerosDict[0]
print(numerosDict)

    
