import random
lista = []
for i in range(20):
    lista += [random.randint(-100, 100)]
print("Lista organizada: ", sorted(lista))
print("Lista original: ", lista)
print("Maior número: ", max(lista))
print("Menor número: ", min(lista))