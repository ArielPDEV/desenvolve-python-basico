import random
lista1 = []
lista2 = []
for i in range(20):
    lista1 += [random.randint(0, 50)]
for i in range(20):
    lista2 += [random.randint(0, 50)]
interseccao = list(set(lista1) & set(lista2))
print(lista1)
print(lista2)
print(sorted(interseccao))
for i in interseccao:
    print(f"{i}, ({lista1.count(i)}, {lista2.count(i)})")