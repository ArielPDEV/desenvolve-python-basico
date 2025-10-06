import os

mais_tocadas = {}
caminho = os.path.join(os.getcwd(), "spotify-2023.csv")

with open(caminho, "r", encoding="latin-1") as f:
    linhas = f.readlines()

linhas = linhas[1:]

for linha in linhas:
    if '"' in linha:
        continue
    partes = linha.strip().split(",")
    if len(partes) < 9:
        continue
    try:
        nome = partes[0]
        artista = partes[1]
        ano = int(partes[3])
        tocadas = int(partes[8])
    except:
        continue
    if ano >= 2012 and ano <= 2022:
        if ano not in mais_tocadas:
            mais_tocadas[ano] = [nome, artista, ano, tocadas]
        else:
            if tocadas > mais_tocadas[ano][3]:
                mais_tocadas[ano] = [nome, artista, ano, tocadas]
anos = list(mais_tocadas.keys())
anos.sort()
for a in anos:
    print(mais_tocadas[a])