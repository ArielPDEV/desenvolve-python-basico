import os

with open("frase.txt", "r") as f:
    frase = f.read()
palavras = frase.split()
if os.path.isfile("palavras.txt") == False:
    open("palavras.txt", "x")
for i in range(len(palavras)):
    with open("palavras.txt", "a") as g:
        g.write(palavras[i] + "\n")
read = open("palavras.txt", "r")
print(read.readlines())