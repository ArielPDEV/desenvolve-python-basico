idade = int(input("Qual sua idade? "))
ja_jogou = (input("Jogou jogos de tabuleiro nos últimos 3 anos? "))
venceu = int(input("Quantos jogos você já venceu? "))
idade = bool(idade > 16 and idade < 19)
ja_jogou == "sim" or ja_jogou == "Sim"
venceu = bool(venceu > 0)
print(idade and ja_jogou and venceu)