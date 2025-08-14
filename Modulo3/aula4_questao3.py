ano = int(input("Digite um ano: "))
por4 = ano % 4 == 0
por100 = ano % 100 == 0
por400 = ano % 400 == 0
if por4 and not por100 or por400:
    print("O ano é bissexto")
else:
    print("O ano não é bissexto")