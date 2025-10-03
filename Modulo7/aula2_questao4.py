def validador_senha(x):
    verif1 = 0
    verif2 = 0
    verif3 = 0
    verif4 = 0
    if len(x) >= 8:
        print("maior q 8")
        for i in range(len(x)):
            if x[i] in "qwertyuiopasdfghjklçzxcvbnm":
                verif1 = 1
                print("minusculo")
            if x[i] in "QWERTYUIOPASDFGHJKLÇZXCVBNM":
                verif2 = 1
                print("maiusculo")
            if x[i] in "0123456789":
                verif3 = 1
                print("numero")
            if x[i] in "!@#$%¨&*()-_=+{[]}<>:;/\?|'°ºª¬¢£³²¹":
                verif4 = 1
                print("especial")
    if verif1 == 1 and verif1 == verif2 and verif2 == verif3 and verif3 == verif4:
        return True
    return False

senha = input("Digite sua senha: ")
print(validador_senha(senha))