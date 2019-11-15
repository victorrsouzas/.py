import time
#Variaveis
estoque={}
a=0 #função PRINCIPAL
b=1 #função PRINCIPAL
c=0 #função ADICIONAR
d=1 ##função ADICIONAR
e=1#função RETIRAR

#listas 
lista1 = ["SKOL","BRAHMA","BOHEMIA","DEVASSA"]
lista2 = ["COCA COLA","GUARANA","SPRITE","FANTA"]
lista3 = ["ORLOFF","SLOVA","XIXI DE MOÇA","NATASHA"]
listaSkol = []
listaBrahma = []
listaBohemia = []
listaDevassa = []
listaOutroC = []
listaCoca = []
listaGuarana = []
listaSprite = []
listaFanta = []
listaOutroR = []
listaOrloff = []
listaSlova = []
listaXixi = []
listaNatasha = []
listaOutroD = []

#Função de ADICIONAR
def adicionando(x1,x2):
  add = dict({x1:x2})
  estoque.update(add)
  
#Função de CONSULTAR
def consultar(a):
    print("""
   -----------------------------
            ESTOQUE
   -----------------------------    
   """)
    if len(estoque)<=0:
        print('NENHUM ITEM NO ESTOQUE')
    else:
        print(estoque)
    return estoque

#Função de Adicionar o Estoque        
def adicionar(a):
    while d==1:
        print("    ------ADICIONAR ESTOQUE------")
        print("""
        Escolha a opção do produto:
        1. Cervejas
        2. Refrigerantes
        3. Destilados
        4.Sair
        """)
        c = int(input("Opção: "))
        if c == 1:
            print("""
        1.SKOL
        2.BRAHMA
        3.BOHEMIA
        4.DEVASSA
        5.Outro
        6.Sair
            """)
            cerveja = int(input("Qual cerveja: "))
            if cerveja == 1:
                adc1 = lista1[0]
                qtd = int(input(f"Quantidade de {adc1}: "))
                listaSkol.append(qtd)
                soma = sum(listaSkol)
                adc2 = soma
                adicionando(adc1,adc2)
            elif cerveja == 2:
                adc1 = lista1[1]
                qtd = int(input(f"Quantidade de {adc1}: "))
                listaBrahma.append(qtd)
                soma = sum(listaBrahma)
                adc2 = soma
                adicionando(adc1,adc2)
            elif cerveja == 3:
                adc1 = lista1[2]
                qtd = int(input(f"Quantidade de {adc1}: "))
                listaBohemia.append(qtd)
                soma = sum(listaBohemia)
                adc2 = soma
                adicionando(adc1,adc2)
            elif cerveja == 4:
                adc1 = lista1[3]
                qtd = int(input(f"Quantidade de {adc1}: "))
                listaDevassa.append(qtd)
                soma = sum(listaDevassa)
                adc2 = soma
                adicionando(adc1,adc2)
            elif cerveja == 5:
                adc1=str(input("Qual o produto?\n")).upper()
                lista1.append(adc1)
                qtd = int(input(f"Quantidade de {adc1}: "))
                listaOutroC.append(qtd)
                soma = sum(listaOutroC)
                adc2 = soma
                adicionando(adc1,adc2)
            elif cerveja == 6:
                return adicionar(a)
                
        elif c == 2:
            print("""
        1.COCA COLA
        2.GUARANA
        3.SPRITE
        4.FANTA
        5.Outro
        6.Sair
            """)
            refrigerante = int(input("Qual Refrigerante: "))
            if refrigerante == 1:
                adc1 = lista2[0]
                qtd = int(input(f"Quantidade de {adc1}: "))
                listaCoca.append(qtd)
                soma = sum(listaCoca)
                adc2 = soma
                adicionando(adc1,adc2)
            elif refrigerante == 2:
                adc1 = lista2[1]
                qtd = int(input(f"Quantidade de {adc1}: "))
                listaGuarana.append(qtd)
                soma = sum(listaGuarana)
                adc2 = soma
                adicionando(adc1,adc2)
            elif refrigerante == 3:
                adc1 = lista2[2]
                qtd = int(input(f"Quantidade de {adc1}: "))
                listaSprite.append(qtd)
                soma = sum(listaSprite)
                adc2 = soma
                adicionando(adc1,adc2)
            elif refrigerante == 4:
                adc1 = lista2[3]
                qtd = int(input(f"Quantidade de {adc1}: "))
                listaFanta.append(qtd)
                soma = sum(listaFanta)
                adc2 = soma
                adicionando(adc1,adc2)
            elif refrigerante == 5:
                adc1=str(input("Qual o produto?\n")).upper()
                lista2.append(adc1)
                qtd = int(input(f"Quantidade de {adc1}: "))
                listaOutroR.append(qtd)
                soma = sum(listaOutroR)
                adc2 = soma
                adicionando(adc1,adc2)
            elif refrigerante == 6:
                return adicionar(a)
            
        elif c == 3:
            print("""
        1.ORLOFF
        2.SLOVA
        3.XIXI DE MOÇA
        4.NATASHA
        5.Outro
        6.Sair
            """)
            destilado = int(input("Qual destilado: "))
            if destilado == 1:
                adc1 = lista3[0]
                qtd = int(input(f"Quantidade de {adc1}: "))
                listaOrloff.append(qtd)
                soma = sum(listaOrloff)
                adc2 = soma
                adicionando(adc1,adc2)
            elif destilado == 2:
                adc1 = lista3[1]
                qtd = int(input(f"Quantidade de {adc1}: "))
                listaSlova.append(qtd)
                soma = sum(listaSlova)
                adc2 = soma
                adicionando(adc1,adc2)
            elif destilado == 3:
                adc1 = lista3[2]
                qtd = int(input(f"Quantidade de {adc1}: "))
                listaXixi.append(qtd)
                soma = sum(listaXixi)
                adc2 = soma
                adicionando(adc1,adc2)
            elif destilado == 4:
                adc1 = lista3[3]
                qtd = int(input(f"Quantidade de {adc1}: "))
                listaNatasha.append(qtd)
                soma = sum(listaNatasha)
                adc2 = soma
                adicionando(adc1,adc2)
            elif destilado == 5:
                adc1=str(input("Qual o produto?\n")).upper()
                lista3.append(adc1)
                qtd = int(input(f"Quantidade de {adc1}: "))
                listaOutroD.append(qtd)
                soma = sum(listaOutroD)
                adc2 = soma
                adicionando(adc1,adc2)
            elif destilado == 6:
                return adicionar(a)
        elif c == 4:
            break
        else:
            print("\nRESPONDA APENAS (1-2-3-4-5-6)")
  
        print("-------------------------")
        print("1.VOLTAR MENU")
        b=int(input(""))
        if d==2:
            break

#Função de Retirar o Estoque    
def retirar(a):
    print("    ------RETIRAR ESTOQUE--------\n")
    if len(estoque)<=0:
        print('    NENHUM ITEM NO ESTOQUE')
    else:
        while e == 1:
            print("-------------------------")
            print("""
        Qual o produto deseja retirar:
        1. Cervejas
        2. Refrigerantes
        3. Destilados
        4.Sair
        """)  
            
            retirar1=int(input("Opção: "))
            if retirar1 == 1:
                print("""
        1.SKOL
        2.BRAHMA
        3.BOHEMIA
        4.DEVASSA
        5.Outro
        6.Sair
            """)
                cerveja = int(input("Qual cerveja: "))
                if cerveja == 1:
                    adc1 = lista1[0]
                    qtd = int(input(f"Quantidade de {adc1} retirada: "))
                    inversão = qtd * - 1
                    listaSkol.append(inversão)
                    soma = sum(listaSkol)
                    adc2 = soma
                    adicionando(adc1,adc2)
                elif cerveja == 2:
                    adc1 = lista1[1]
                    qtd = int(input(f"Quantidade de {adc1} retirada: "))
                    inversão = qtd * - 1
                    listaBrahma.append(inversão)
                    soma = sum(listaBrahma)
                    adc2 = soma
                    adicionando(adc1,adc2)
                elif cerveja == 3:
                    adc1 = lista1[2]
                    qtd = int(input(f"Quantidade de {adc1} retirada: "))
                    inversão = qtd * - 1
                    listaBohemia.append(inversão)
                    soma = sum(listaBohemia)
                    adc2 = soma
                    adicionando(adc1,adc2)
                elif cerveja == 4:
                    adc1 = lista1[3]
                    qtd = int(input(f"Quantidade de {adc1} retirada: "))
                    inversão = qtd * - 1
                    listaDevassa.append(inversão)
                    soma = sum(listaDevassa)
                    adc2 = soma
                    adicionando(adc1,adc2)
                elif cerveja == 5:
                    adc1=str(input("Qual o produto?\n")).upper()
                    qtd = int(input(f"Quantidade de {adc1}: "))
                    inversão = qtd * - 1
                    listaOutroC.append(inversão)
                    soma = sum(listaOutroC)
                    adc2 = soma
                    adicionando(adc1,adc2)
                elif cerveja == 6:
                    return retirar(a)
            elif retirar1 == 4:
                break
            else:
                print("\nRESPONDA APENAS (1-2-3-4-5-6)")
  
            print("-------------------------")
            print("1.VOLTAR MENU")
            b=int(input(""))
            if e==2:
                break

#FUNÇÃO PRINCIPAL - loop para voltar menu
def gestaoEstoque(b):
    print("""
    -----------------------------
             BAR DO VÉI
    -----------------------------
    """)
    time.sleep(1)
    while b==1:
        print("""
    -----------------------------
      SISTEMA GESTÃO MERCADORIA
    -----------------------------
        1.CONSULTAR ESTOQUE
        2.ADICIONAR ESTOQUE
        3.RETIRAR ESTOQUE
        4.SAIR
    -----------------------------""")
        a=int(input("Opção: "))
        if a==1:
            consultar(a) 
        elif a==2:
            adicionar(a) 
        elif a==3:
            retirar(a)
        elif a==4:
            break
        else:
            print("\nRESPONDA APENAS (1-2-3-4)")
  
        print("-------------------------")
        print("1.VOLTAR MENU")
        b=int(input(""))
        if b==1:
            continue

gestaoEstoque(b)
