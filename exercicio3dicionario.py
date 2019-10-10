"""Exercício
○ Escreva um programa que faça a atualização no dicionário a de
acordo com os valores de b. Porém, ele não deve adicionar novos
valores, só atualizar os existentes.
■ a = {'a': 100, 'b': 200, 'c':300}
■ b = {'a': 300, 'b': 200, 'd':400, ‘c’:500, ‘e’:250}"""

a = {'a': 100, 'b': 200, 'c':300}
b = {'a': 300, 'b':200, 'c':500, 'd':400, 'e':250}

a.update(b)

print(a)

