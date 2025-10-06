import os, random
def estado(x, y): # Função que imprime o estado da forca (sendo "x" a lista, "y" a fatia(estado da forca), e "z" a linha da fatia)
    for z in range(len(x[y])):
        print(x[y][z])
    return ""

letras_acerto = []
forca = 0 # Define em qual estado da forca estamos
enforcado = [] # Lista dos estados da forca
with open("gabarito_forca.txt", "r") as f: # Lendo as palavras disponiveis
    palavras = f.readlines() # Importa as palavras do arquivo de palavras
    chave = palavras[random.randint(0, len(palavras)-1)] # Escolhendo uma palavra
    tracejado = ["_"]*(len(chave)-1) # Define o tracejado do tamanho da palavra chave
    chave = chave.strip() # Remove a quebra de linha da palavra
    letras_chave = set([i for i in chave]) # Organiza as letras
    chave = [i for i in chave]
with open("gabarito_enforcado.txt", "r") as f: # Importando as linhas do gabarito dos estados
    linhas = f.readlines()
    linhas = [i.strip() for i in linhas]
enforcado.append(linhas[0:5]) # Definindo os estados   *0*
enforcado.append(linhas[5:10]) # Definindo os estados  *1*
enforcado.append(linhas[11:15]) # Definindo os estados *2*
enforcado.append(linhas[15:20]) # Definindo os estados *3*
enforcado.append(linhas[20:25]) # Definindo os estados *4*
enforcado.append(linhas[25:30]) # Definindo os estados *5*
enforcado.append(linhas[30:35]) # Definindo os estados *6*

print(estado(enforcado, forca)) # Imprime o estado da forca
print(" ".join(tracejado))          # Imprime as quantidades de letras em underscore
while forca < 6 and sorted(letras_chave) != sorted(letras_acerto):
    letra = input("Digite uma letra: ") # Pede uma letra ao usuário 
    if letra in chave: # Entende um acerto
        if letra not in letras_acerto: # Verifica letras repetidas
            letras_acerto.append(letra) # Adiciona a letra ao aglomerado de letras certas
            for i, let in enumerate(chave): # Troca o "_" pela letra certa
                if let == letra: # Verifica a letra pelo indice
                    tracejado[i] = letra # Troca o tracejado do indice pela letra correta
    else:
        forca += 1 # Aumenta o estado em caso de erro
    print(estado(enforcado, forca)) # Imprime o estado atual do jogo
    print(" ".join(tracejado))
if forca >= 6: # Saida vitoria ou derrota
    print("Você perdeu, a palavra era ", chave)
else:
    print("Você ganhou")