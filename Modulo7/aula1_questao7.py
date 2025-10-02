def encrypt(x: list, y: int):
    strnum_list = []
    str_list = []
    temp_palavra = ""
    for i in range(len(x)):
        for j in range(len(x[i])):
            temp = ord(x[i][j]) + y
            while temp > 126:
                temp -= 94
            while temp < 33:
                temp += 94
            strnum_list.append(temp)
            temp_palavra += chr(strnum_list[j])
        str_list.append(temp_palavra)
        temp_palavra = ""
        strnum_list = []
    return str_list

palavras = []

quant = int(input("Quantas palavras tem a lista? "))
print("Quais as palavras da lista? ")
for i in range(quant):
    palavras.append(input())
chave = int(input("Qual a chave de criptografia? "))
pal_encr = encrypt(palavras, chave)
print(pal_encr)