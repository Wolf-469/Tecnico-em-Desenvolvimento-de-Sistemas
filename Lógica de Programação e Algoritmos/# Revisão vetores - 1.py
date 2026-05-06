# Revisão vetores - 1
# Solicitar ao usuário a quantidade de números
# Preencher o vetor
# percorrer o vetor e calcular a soma dos números
# Exibir a soma
#---------------------------------------------------------------------

# Passo) Criar as variáveis
qtd = int(input("Digite a quntidade de números: "))
vetor = []
soma = 0 

# Passo 2) Preencher o vetor
for i in range(qtd):
    vetor.append(int(input("Digite um número: ")))

#Passo 3) Percorrer o vetor 
for num in vetor:
    soma = soma + num 

print("Soma é: ", soma)