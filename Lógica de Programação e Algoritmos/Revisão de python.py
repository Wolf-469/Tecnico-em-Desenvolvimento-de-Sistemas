#Criando uma variável númerica
numero = 10

#Criando uma variável texto
nome = "Brenda"

#Usuário inseir um texto 
nome_completo = int(input("Digite seu nome: "))

#Usuário inseir um número inteiro 
idade = int("Digite sua idade: ")

#Usuário inseir um número decimal
salario = float(input("Digite seu salário: "))

#Estruturas condicionais - IF
if(salario > 1500 and idade > 18 ):
    print("Você pode tirar carta! ")
elif(salario < 1500 or idade > 18):
    print("Você não pode tirar carta! ")
else:
    print("Inválido")


#Estrutura condicionais exemplo2
turno = input("Digite seu turno (M/V/N): ")

if(turno == "M"):
    print("Bom dia! ☀️")
elif(turno == "V"):
    print("Boa Tarde! ☕")
elif(turno == "N"):
    print("Boa Noite! 🌒")
else:#else não tem parênteses
    print("Inválido🫥")

#Estrutrura de repetição
#0 - > 10
for i in range(11):#Sempre coloque +1
    print(i)

#1 - > 15
for i in range(1,16):#Vai do 1 até o 15
    print(i)

#5 - > 65 (aumentando de 5 em 5)
for i in range (5,66,+5):
    print(i)

#122 - > (tirando de 2 em 2)
for i in range (122,-1,-2):
    print(i)

#Usuário escolhe o inicio e fim
#inicio - > fim
inicio = int(input("Início: "))
Fim = int(input("Fim: "))

for i in range (inicio,fim +1):
    print(i)


#Vetores
nomes = []

#Sempre utilizar para preencher o vetor
for i in range (5):
    nomes.append(input("Digite um nome: "))
#Sempre utilizar para exibir o vetor
for i in nomes:
    print(nomes)