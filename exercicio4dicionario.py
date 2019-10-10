"""Exercício
○ Uma pista de Kart permite 10 voltas para cada um de 6
corredores. Escreva um programa que leia todos os tempos em
segundos e os guarde em um dicionário, onde a chave é o nome
do corredor. Ao final diga de quem foi o campeão, lembre-se, o
campeão tem a menor média de tempos."""

voltasfechado = {}
corredor = 0
volta = 0
    
def corrida():
    global corredor
    corredor = int(input("Corredor: "))
    return corredor

def voltas():
    global volta
    volta = int(input())
    return volta
        
        

while corrida() < 7:
        volta1= int(input())
        volta2= int(input())
        volta3= int(input())
        volta4= int(input())
        volta5= int(input())
        volta6= int(input())
        volta7= int(input())
        volta8= int(input())
        volta9= int(input())
        volta10= int(input())
        voltas = dict({corredor: [volta1,volta2,volta3,volta4,volta5,volta6,volta7,volta8,volta9,volta10]})             
        voltasfechado.update(voltas)      
   
        
print(voltasfechado)

media_geral ={}

for tempo in voltasfechado:
    media = int(sum(voltasfechado[tempo])/len(voltasfechado[tempo]))
    print(f" o corredor {tempo} teve media de {media} segundos")
    quadro_de_media = dict({tempo: [media]})
    media_geral.update(quadro_de_media)

print(media_geral)
minimo = min(media_geral)
print(f'Logo o vencedor com a menor media é {minimo}º corredor')

    
