import random
lista = []
listaPar2050 = []
listaQuadrado = []
listaDiv7 = []
listaPar030 = []
confere030 = []
for i in range(10):
    lista += [random.randint(0, 100)]
lista = sorted(lista)
for i in range(0, 30, 3):
    confere030 += [i]
for i in range(len(lista)):
    if lista[i] >= 20 and lista[i] <= 50 and lista[i] % 2 == 0:
        listaPar2050 += [lista[i]]
    listaQuadrado += [(lista[i])**2]
    if lista[i] % 7 == 0:
        listaDiv7 += [lista[i]]
    if lista[i] in confere030:
        par = ("par" if lista[i] % 2 == 0 else "impar")
        listaPar030 += [par]
print("Lista original: ", lista)
print("Pares entre 20 e 50: ", listaPar2050)
print("Lista dos quadrados: ", listaQuadrado)
print("Lista dos multiplos de 7: ", listaDiv7)
print("Par ou impar(itens entre 0 e 30 pulando de 3 em 3): ", listaPar030)