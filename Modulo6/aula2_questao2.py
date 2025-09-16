import random
elementos = []
num_elementos = random.randint(5, 20)
for i in range(num_elementos):
    elementos += [random.randint(1, 10)]
print("Lista: ", (elementos))
print("Soma dos elementos: ", sum(elementos))
print(f"Média dos elementos: {((sum(elementos))/(len(elementos))):,.2f}")