# Inicializa um vetor vazio (lista)
numeros = []

# Lê 7 números
for i in range(7):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num) # Armazena no vetor

# Calcula a soma
soma = sum(numeros)

# Exibe o resultado
print("-" * 20)
print(f"Vetor: {numeros}")
print(f"A soma dos elementos é: {soma}")