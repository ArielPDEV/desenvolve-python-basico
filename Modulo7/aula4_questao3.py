import os

mencoes = []
with open("estomago.txt", "r", encoding="utf-8") as read:
    linha = read.readlines()
    linha = [l.strip() for l in linha]
for i in range(25):
    print(f"Linha {i + 1}: {linha[i]}")
print(f"Quantidade de linhas: {len(linha)}")
print(f"Maior linha:         '{max(linha)}'")
for i in range(len(linha)):
    temp_linha = linha[i].split(" ")
    for i in range(len(temp_linha)):
        if temp_linha[i] == "Nonato" or temp_linha[i] == "Íria":
            mencoes.append(temp_linha[i])
print(f"Número de menções à Nonato e Íria: {len(mencoes)}")