def verifica_anagrama(x, y):
    return sorted(x) == sorted(y)

frase = input("Digite a frase: ").lower()
objetivo = input("Qual a palavra? ").lower()
temp_palavra = [] 
anagrama = []
palavra = ""
n = len(objetivo)
l = 0
for i in range(len(frase) -n +1):
    temp_palavra = frase[i:i+n]
    if verifica_anagrama(temp_palavra, objetivo):
        anagrama.append(temp_palavra)
print(anagrama)