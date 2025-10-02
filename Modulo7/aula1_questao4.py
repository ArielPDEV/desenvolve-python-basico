tel = input("Digite seu número de telefone: ")
tel_separado = ""
telTemp1 = ""
telTemp2 = ""
if len(tel) == 8:
    tel = "9" + tel
    print(tel, "menos q 9 digitos")
if len(tel) == 9 :#and tel[0] == 9
    print(tel, "9 digitos")
    for i in range(5):
        telTemp1 += tel[i]
        print(telTemp1, "primeira metade")
    for i in range(5,9):
        telTemp2 += tel[i]
        print(telTemp2, "segunda metade")
    tel_separado = telTemp1 + "-" + telTemp2
    print(tel_separado)
print(tel_separado)