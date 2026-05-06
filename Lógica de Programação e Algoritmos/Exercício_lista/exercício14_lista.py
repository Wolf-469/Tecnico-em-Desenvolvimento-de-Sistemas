positivos = 0
negativos = 0

for i in range(10):
    num = float(input(f"Digite o {i+1}º número: "))
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

print(f"Quantidade de positivos: {positivos}")
print(f"Quantidade de negativos: {negativo}")