part = int(input("Qual a quantidade de participantes? "))
num = part
total = 0
n = 1
while num >= 1:
    idade = int(input(f"Qual a idade do participante {n}? "))
    total += idade
    n += 1
    num -= 1
total /= part
print(f"A média das idades dos participantes é igual a {int(total)}")