"""Exercício
○ Faça dois vetores para armazenar as idades e alturas de 30 alunos,
usando input;
○ O programa deverá determinar quantos alunos com mais de 13
anos possuem altura inferior à média das alturas dos alunos."""

idades = []
altura = []

for c in range(2):
    idades.append(int(input()))
    
for i in range(2):    
    altura.append(float(input()))
    
print(idades)
print(altura)

media_altura = sum(altura)/len(altura)
print('{:.2f}'.format(media_altura))

soma = 0

for idade in idades:
    print(end = '') # comando (idade, end = " ") pra ficar na mesma linha com espaço
for alturas in altura:
    if alturas < media_altura:
        if idade > 13:
            soma +=1

print(soma)



        

