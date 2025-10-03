frase = ""
inverso = []

while frase != "fim":
    frase = input("Digite uma frase (digite 'fim' para encerrar): ")
    for i in range(len(frase)):
        j = i + 1
        inverso.append(frase[-j])
        print(inverso)
    print(frase)
    inverso = ''.join(inverso)
    if frase == inverso:
        print(f"'{frase}' é um palindromo!")
    else:
        print(f"'{frase}' não é um palindromo!")