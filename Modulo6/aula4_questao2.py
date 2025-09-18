frase = input("Frase: ").lower()
vogais = sorted([i for i in frase if i in "aeiou"])
consoantes = [i for i in frase if i.isalpha() and i not in "aeiou"]
print("Vogais: ", vogais)
print("Consoantes: ", consoantes)