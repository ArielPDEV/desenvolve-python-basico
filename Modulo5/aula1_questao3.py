import random
num = random.randint(1, 10)
print(num)
palp = 0
while num != palp:
    palp = int(input("Qual o seu palpite? "))
    if palp > num:
        print("O número é menor que seu palpite ")
    elif palp < num:
        print("O número é maior que seu palpite ")
print("Parabéns!!! Você acertou !!!")