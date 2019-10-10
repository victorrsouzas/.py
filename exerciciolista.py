notas = []

for c in range(5): # primeiro for pra add na LISTA notas
    notas.append(float(input()))
    
print(notas)
#tirar os parametros de minimo, maximo,soma e media
minimo = min(notas)
maximo = max(notas)
soma = sum(notas)
media = sum(notas)/len(notas)
print(f'{minimo}, {maximo}, {soma}, {media}')

#segundo FOR para pegar so as notas maiores que a media.OBS: não é necessario usar parametro ().
for nota in notas:
    if nota > media:
        print(f'{nota} foi maior que a media')
