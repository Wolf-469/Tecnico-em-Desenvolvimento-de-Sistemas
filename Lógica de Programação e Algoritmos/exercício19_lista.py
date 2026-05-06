#Leia 4 números e ordene-os em ordem cresce

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))
n4 = float(input("Digite o quarto número: "))

numeros = [n1, n2, n3, n4]

numeros_ordenados = sorted(numeros)

print("Números em ordem crescente:", numeros_ordenados)