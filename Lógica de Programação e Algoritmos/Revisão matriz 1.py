# Revisão Matriz 1
#Solicitar a quantidade de linhas
#Solicitar a quantidade de colunas
#Preencher a matriz 
#Calcular a soma de todos os números
#-----------------------------------

#Passo1) Variáveis
linhas = int(input("Digite a quantiade de linhas: "))
colunas = int(input("Digite a quantiade de colunas: "))
matriz = []
soma = 0

#Passo2) Preencher matriz 
#Sempre repetir quando preencher matriz 
for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(int(input("Digite um número: ")))
    matriz.append(linha)

#Passo3) Percorrer a matriz e calcular a soma
for i in range(linhas):
    for j in range(colunas):
        soma = soma + matriz[i][j]
print("A soma é: ", soma)