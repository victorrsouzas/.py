""" Faca uma função que recebe a media final de um aluno por parâmetro e retorna o seu conceito, conforme a tabela?:
De 0 a 4.9   D
De 5.0 a 6.9 C
De 7.0 a 8.9 B
De 9.0 a 100 A""" 

nota = 0
lista = []

def notas():
    global nota
    for c in range(2):
        nota = float(input("Digite sua nota: "))
        lista.append(nota)
    mediaGeral = sum(lista)/len(lista)
    if mediaGeral > -1:
        parametro(mediaGeral)
    
    
    return nota
      

def parametro(mediaGeral):
    if mediaGeral < 5:
        print("D")
    elif mediaGeral >= 5 and mediaGeral < 7:
        print("C")
    elif mediaGeral >= 7 and mediaGeral < 9:
        print("B")
    else:
        print("A")
    
notas()



