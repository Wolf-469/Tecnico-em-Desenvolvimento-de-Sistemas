soma = 0
numeros = []

for i in range (4):
    num = int(input("Digite um número: "))
    numeros.append(num)


for numero in numeros:
    soma = soma + numero
media = (soma)/4

if(numero < 4):
    print("Reprovado:")
elif(numero >=4 and numero <= 7):
    print("Recuperação:")
else:
    print("Aprovado")
