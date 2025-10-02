frase = input("Digite a frase: ")
index = []
quantidade = 0
for letra in range(len(frase)):
    if frase[letra] in "aeiouAEIOUáàâãéèêíìîóòôõúùû":
        index.append(letra)
        quantidade += 1
print(f"{quantidade} vogais")
print(f"Índices: {index}")