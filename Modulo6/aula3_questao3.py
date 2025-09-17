import random
lista = []
tamAtual = 0
iniAtual = 0
tamMaior = 0
iniMaior = 0
for i in range(20):
    lista += [random.randint(-10,10)]
print(lista)
for i in range(len(lista)):
    if lista[i] < 0:
        tamAtual += 1
        if tamAtual == 1:
            iniAtual = i
    else:
        if tamAtual > tamMaior:
            iniMaior = iniAtual
            tamMaior = tamAtual
        iniAtual = 0
        tamAtual = 0
if tamAtual > tamMaior:
    iniMaior = iniAtual
    tamMaior = tamAtual
fim = iniMaior + tamMaior
del lista[iniMaior:fim]
print(iniMaior, fim)
print(lista)