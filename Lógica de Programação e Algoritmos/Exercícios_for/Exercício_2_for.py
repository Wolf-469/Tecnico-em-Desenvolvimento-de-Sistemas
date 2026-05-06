inicio = int(input("Digite um número de início: "))
fim = int(input("Digite um número final: "))
soma = 0

for i in range (inicio, fim+1):
    if(i%2 == 0):
      soma = soma + i

print(soma)
    

    