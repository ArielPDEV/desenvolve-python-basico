num1 = int(input("Digite o valor 1: "))
num2 = int(input("Digite o valor 2: "))
num3 = int(input("Digite o valor 3: "))
media = (num1 + num2 + num3) / 3
if media >= 60:
    print("Aprovado")
elif media >= 40:
    print("Recuperação")
else:
    print("Reprovado")
print("Fim")