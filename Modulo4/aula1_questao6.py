quant = int(input("Quantos experimentos foram registrados? "))
cont = 0
n = 1
valC = 0
valS = 0
valR = 0
valG = 0
while quant > cont:
    val = input(f"Quantos animais foram utilizados no experimento {n}. (Ex: 10 C)").split()
    tipo = val[1]
    if tipo == "C":
        valC += int(val[0])
        valG += int(val[0])
    elif tipo == "S":
        valS += int(val[0])
        valG += int(val[0])
    elif tipo == "R":
        valR += int(val[0])
        valG += int(val[0])
    else:
        print("entrada invalida")
    cont += 1
print(f"Total de cobaias: {valG}")
print(f"Total de coelhos: {valC}")
print(f"Total de ratos: {valR}")
print(f"Total de sapos: {valS}")
print(f"Percetual de coelhos: {(valC / valG) * 100:,.2f}%")
print(f"Percetual de ratos: {(valR / valG) * 100:,.2f}%")
print(f"Percetual de sapos: {(valS / valG) * 100:,.2f}%")