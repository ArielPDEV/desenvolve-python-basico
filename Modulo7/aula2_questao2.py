frase = input("Digite uma frase: ")
for i in range(len(frase)):
    if frase[i].lower() in "aeiou":
        frase = frase.replace(frase[i],"*")
print(frase)