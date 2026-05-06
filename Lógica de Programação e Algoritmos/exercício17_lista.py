palavra = input("Digite uma palvra: ")

vogais = "aeiouAEIOUáéíóúâêîôûãõàèìòùÁÉÍÓÚÂÊÎÔÛÃÕÀÈÌÒÙ"
contador = 0

for letra in palavra:
    if letra in vogais:
        conatdor + 1 

print("Quantidade de vogais", contador)
