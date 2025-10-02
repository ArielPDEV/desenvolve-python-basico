def verificaCPF(x):
    verif1 = 0
    verif2 = 0
    temp = 0
    j = 2
    if len(x) == 11: 
        for i in range(-3, -12, -1):
            temp += int(x[i]) * j
            j += 1
        if temp % 11 < 2:
            verif1 = 0
        else:
            verif1 = 11 - (temp % 11)
        if int(x[-2]) == verif1:
            temp = 0
            j = 2
            for i in range(-2, -12, -1):
                temp += int(x[i]) * j
                j += 1
            if temp % 11 < 2:
                verif2 = 0
            else:
                verif2 = 11 - (temp % 11)
            if int(x[-1]) == verif2:
                return True
    return False

cpf = input("Digite seu cpf (apenas números): ")
print(("Válido" if verificaCPF(cpf) else "Inválido"))