tamanho = 0
lista = []
while True:
    tamanho = int(input("Qual o tamanho da lista? "))
    if tamanho >= 4:
        break
    print("O valor deve ser igual ou maior que '4' ")
for i in range(1, tamanho + 1):
    val = int(input(f"Qual o {i}° elemento na lista? "))
    lista += [val]
print("Lista: ", lista)
print("3 primeiros itens: ", lista[0:3])
print("2 ultimos itens: ", lista[-1:-3:-1])
print("Lista inversa: ", lista[::-1])
print("Números pares: ", lista[1::2])
print("Números impares: " , lista[::2])