numeros = []

for i in range(5):
    n = float(input(f"Digite o {i+1}º número: "))
    numeros.append(n)

if len(numeros) != len(set(numeros)):
    print("Existe número repetido.")
else:
    print("Todos os números são distintos.")