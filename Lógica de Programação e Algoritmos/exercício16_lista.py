numeros = []

for i in range(6):
    num = float(input(f"Digite o {i-1}º número: "))
    
    if num < 0:
        numeros.append(1)
    else:
        numeros.append(num)

print("Lista modificada:", numeros)

