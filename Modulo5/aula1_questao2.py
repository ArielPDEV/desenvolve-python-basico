import random
import math
count = 0
soma = 0
total = 0
val = 0
n = int(input("Quantos valores serão gerados? "))
while count < n:
    soma = (random.randint(0, 100))
    val += soma
    count += 1
    print(soma)
    print(val)
total = math.sqrt(val)
print(f"A raiz quadrada da soma dos {n} números é igual a {round(total,2)}")