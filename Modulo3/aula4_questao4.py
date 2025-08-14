distancia = float(input("Qual a distancia da entrega em km? "))
peso = float(input("Qual o peso do pacote em kg? "))
valor = peso
if distancia <= 100:
    if peso > 10:
        valor += 10
    print(f"O valor do frete é R${valor * 1:,.2f}")
if distancia > 100 and distancia <= 300:
    if peso > 10:
        valor += 10
    print(f"O valor do frete é R${valor * 1.5:,.2f}")
if distancia > 300:
    if peso > 10:
        valor += 10
    print(f"O valor do frete é R${valor * 2:,.2f}")