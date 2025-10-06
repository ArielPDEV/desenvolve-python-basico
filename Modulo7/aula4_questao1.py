import os

frase = input("Escreva uma frase: ")
with open("frase.txt", "w") as f:
    f.write(frase + "\n")
print(os.path.abspath("frase.txt"))