import random

def embaralhar_palavras(x):
    x = x.split()
    embaralhado = []
    for i in range(len(x)):
        if len(x[i]) <= 3:
            embaralhado.append(x[i])
        else:
            primLetra = x[i][0]
            ultimaLetra = x[i][-1]
            letrasMeio = list(x[i][1:-1])
            random.shuffle(letrasMeio)
            palavraEmbaralhado = primLetra + ''.join(letrasMeio) + ultimaLetra
            embaralhado.append(palavraEmbaralhado)
    return ' '.join(embaralhado)

frase = input("Digite uma frase: ")
print(embaralhar_palavras(frase))
