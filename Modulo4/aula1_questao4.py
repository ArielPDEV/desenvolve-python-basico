valor1 = int(input("Digite um valor: "))
maior = 0
while valor1 >= maior:
    valor2 = int(input("Digite outro valor: "))
    if valor2 > maior:
        maior = valor2
    else:
        valor1 -= 1
print(maior)