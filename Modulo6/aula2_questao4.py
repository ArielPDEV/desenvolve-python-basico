menor = lambda x, y:x if x < y else y
listaMaior = lambda x, y:x if len(x) > len(y) else y
lista1 = []
lista2 = []
lista3 = []
itns1 = int(input("Quantos elementos tem a primeira lista? "))
print(f"Digite os {itns1} da primeira lista")
for i in range(1, itns1 + 1):
    item = int(input())
    lista1 += [item]
itns2 = int(input("Quantos elementos tem a segunda lista? "))
print(f"Digite os {itns2} da segunda lista")
for i in range(1, itns2 + 1):
    item = int(input())
    lista2 += [item]
listaAdd = listaMaior(lista1, lista2)
for i in range(menor(itns1, itns2)):
    lista3.append(lista1[i])
    lista3.append(lista2[i])
    listaAdd.pop(i)
listaFim = lista3 + listaAdd
print("Lista intercalada: ", listaFim)