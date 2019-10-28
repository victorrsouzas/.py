"""O usuário deverá digitar uma frase. O programa deverá localizar a palavra ‘sábado’ na frase, se existir, substituir por ‘domingo’, caso contrário, mostrará uma mensagem informando que a palavra não foi encontrada."""

frase = input("Digite uma frase: ")

if "sábado" in frase:
    nova_frase = frase.replace("sábado","Domingo")
    print(nova_frase)
else:
    print("Palavra não encontrada")
