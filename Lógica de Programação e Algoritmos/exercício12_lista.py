nomes = []

print("Digite 5 nomes:")
for i in range(5):
    nome = input(f"{i+1}º nome: ")
    nomes.append(nome) 

print("\nNomes na ordem inversa:")
for nome in nomes[-1]:
    print(nome)