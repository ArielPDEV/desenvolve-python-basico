comprimento = int(input("Qual o comprimento do terreno?"))
largura = int(input("Qual a largura do terreno?"))
metro_quadrado = float(input("Qual o preço do metro quadrado na região?"))
area = comprimento * largura
valor_terreno = area * metro_quadrado
print(f"O terreno possui {area}m² e custa R${valor_terreno:,.2f}")