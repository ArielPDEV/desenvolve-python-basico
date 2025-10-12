import sys

login_status = 0
arquivo = "usuarios.txt"
arquivo_produto = "teste_produtos.txt"

def ler_arquivo_usuarios(v=arquivo):
    linhas = []
    a = {}
    with open(v, "r", encoding= "utf-8") as f:
        texto = f.readlines()
    for i in texto:
        linhas.append(i.strip().split(' '))
    for nome, email, senha, nivelPerm in linhas:
        a[email] = {"nome":nome.replace('-',' '), "email":email, "senha":senha, "nivelPerm":nivelPerm}
    return a
def ler_arquivo_produtos(v=arquivo_produto):
    linhas = []
    a = {}
    with open(v, "r", encoding= "utf-8") as f:
        texto = f.readlines()
    for i in texto:
        linhas.append(i.strip().split(' '))
    for id, nome, cat, preco, quant, status in linhas:
        a[id] = {"id":id ,"nome":nome.replace('-',' '), "categoria":cat, "preço":preco, "quantidade":quant, "status":status}
    return a

users = ler_arquivo_usuarios()
produtos = ler_arquivo_produtos()

def pesquisar(x=produtos, y=users):
    while True:
        print("\n Opção 1: Pesquisar por usuario\n Opção 2: Pesquisar por produto/serviço\n Opção 3: Voltar")
        pesq_op = input("\nQual opção você deseja acessar? \n")
        if pesq_op == "1":
            user_email = input("Qual o email do usuario? ")
            print(y[user_email] if user_email in y else "\n Produto não cadastrado")
        elif pesq_op == "2":
            prod_id = input("Qual o código de barras do produto? ")
            print(x[prod_id] if prod_id in x else "\n Produto não cadastrado")
        elif pesq_op == "3":
            print("\nVoltando a tela anterior...\n")
            break
        else:
            print("Opção invalida")

def criar_produto(z=arquivo_produto):
    global produtos
    a = input("\nDigite o código de barras do produto: ")
    b = input("Digite o nome do produto: ")
    c = input("Digite a categoria do produto: ")
    d = input("Digite o preço do produto: ")
    e = input("Digite a quantidade do produto em estoque: ")
    while True:
        print("\nQual o status do produto?\n Status 1: Ativo\n Status 2: Inativo\n Status 3: Esgotado")
        sts = input()
        if sts == "1":
            f = "ativo"
            break
        elif sts == "2":
            f = "inativo"
            break
        elif sts == "3":
            f = "esgotado"
            break
        else:
            print("Opção invalida")
    with open(z, "a", encoding="utf-8") as y:
        y.write(f"{a} {b.replace(' ', '-')} {c} {d} {e} {f}\n")
    produtos = ler_arquivo_produtos()
    print(produtos)

def editar_produto(x=produtos, z=arquivo_produto):
    prt = input("\nDigite o código de barras do produto que deseja editar: ")
    if prt in x:
        print("\nPara manter os dados \nanteriores aperte 'enter' quando \nsolicitar o novo dado\n\n")
        id = input("Digite o novo código do produto: ")
        nome = input("Digite o novo nome do produto: ")
        cat = input("Digite a nova categoria do produto: ")
        preco = input("Digite o novo preço do produto: ")
        quant = input("Digite a nova quantidade do produto: ")
        while True:
            print("\nQual o status do produto terá?\n Status 1: ativo\n Status 2: inativo\n Status 3: esgotado")
            niv = input()
            if niv == "1":
                nivelPerm = "ativo"
                break
            elif niv == "2":
                nivelPerm = "inativo"
                break
            elif niv == "3":
                nivelPerm = "esgotado"
                break
            elif niv == "":
                nivelPerm = ""
                break
            else:
                print("Opção invalida")
        if id != "":
            x[prt]["id"] = id
        if nome != "":
            x[prt]["nome"] = nome
        if cat != "":
            x[prt]["categoria"] = cat
        if preco != "":
            x[prt]["preço"] = preco
        if quant != "":
            x[prt]["quantidade"] = quant
        with open(z, "w", encoding="utf-8") as a:
            for f in x.values():
                linha = f"{f['id']} {f['nome'].replace(' ', '-')} {f['categoria']} {f['preço']} {f['quantidade']} {f['status']}\n"
                a.write(linha)
        print("Produto editado com sucesso\n\n")
    else:
        print("Produto não encontrado\n\n")

def apagar_produto(x=produtos, z=arquivo_produto):
    apag_prt = input("\nDigite o código de barras do produto que deseja apagar: ")
    if apag_prt in x:
        del x[apag_prt]
        with open(z, "w", encoding="utf-8") as a:
            for f in x.values():
                linha = f"{f['id']} {f['nome'].replace(' ', '-')} {f['categoria']} {f['preço']} {f['quantidade']} {f['status']}\n"
                a.write(linha)
        print("Produto editado com sucesso\n\n")
    else:
        print("Produto não encontrado\n\n")

def gerenciar_produtos(x=produtos, z=arquivo_produto):
    while True:
        print("\n Opção 1: Criar produto\n Opção 2: Editar produto\n Opção 3: Apagar produto\n Opção 4: Vizualizar produtos\n Opção 5: Voltar\n")
        ger_prt_op = input("\nQual opção você deseja acessar?\n\n")
        if ger_prt_op == "1":
            criar_produto()
        elif ger_prt_op == "2":
            editar_produto()
        elif ger_prt_op == "3":
            apagar_produto()
        elif ger_prt_op == "4":
            vizualizar_produtos()
        elif ger_prt_op == "5":
            break
        else:
            print("\nOpção invalida\n")

def vizualizar_produtos():
    global produtos
    produtos = ler_arquivo_produtos()
    for i in produtos:
        print(produtos[i])

def vizualizar_usuarios():
    global users
    users = ler_arquivo_usuarios()
    for i in users:
        print(users[i])

def sair():
    print("\nObrigado por utilizar o sistema! \nVolte sempre! \n\nEm caso de problemas com o\nsistema solicite assistencia\ncom o administrador do sistema\n")
    print("Encerrando programa...\n")
    sys.exit()

def criar_usuario(b=arquivo):
    global users
    w = input("\nDigite o nome do usuario: ")
    x = input("Digite o seu email: ")
    y = input("Digite a senha do usuario: ")
    while True:
        print("\nQual o nível de acesso o usuario terá?\n Nível 1: Usuario\n Nível 2: Gerente\n Nível 3: Administrador")
        niv = input()
        if niv == "1":
            z = "usuario"
            break
        elif niv == "2":
            z = "gerente"
            break
        elif niv == "3":
            z = "administrador"
            break
        else:
            print("Opção invalida")
    if w == '' or x == '' or y == '':
        print("Todos os campos devem ser preenchidos.")
    elif x in users:
        print("Usuario já existente.")
    else:
        with open(b, "a", encoding="utf-8") as a:
            a.write(f"{w.replace(' ', '-')} {x} {y} {z}\n")
        users = ler_arquivo_usuarios()

def criar_usuario_menu(b=arquivo):
    global users
    w = input("\nDigite o nome do usuario: ")
    x = input("Digite o seu email: ")
    y = input("Digite a senha do usuario: ")
    z = "usuario"
    if w == '' or x == '' or y == '':
        print("Todos os campos devem ser preenchidos.")
    elif x in users:
        print("Usuario já existente.")
    else:
        with open(b, "a", encoding="utf-8") as a:
            a.write(f"{w.replace(' ', '-')} {x} {y} {z}\n")
        users = ler_arquivo_usuarios()

def editar_usuario(x=users, z=arquivo):
    user = input("\nDigite o email do usuario que deseja editar: ")
    if user in users:
        print("\nPara manter os dados \nanteriores aperte 'enter' quando \nsolicitar o novo dado\n\n")
        nome = input("Digite o novo nome do usuario: ")
        senha = input("Digite a nova senha do usuario: ")
        email = input("Digite o novo email do usuario: ")
        while True:
            print("\nQual o nível de acesso o usuario terá?\n Nível 1: Usuario\n Nível 2: Gerente\n Nível 3: Administrador")
            niv = input()
            if niv == "1":
                nivelPerm = "usuario"
                break
            elif niv == "2":
                nivelPerm = "gerente"
                break
            elif niv == "3":
                nivelPerm = "administrador"
                break
            elif niv == "":
                nivelPerm = ""
                break
            else:
                print("Opção invalida")
        if nome != "":
            x[user]["nome"] = nome
        if senha != "":
            x[user]["senha"] = senha
        if nivelPerm != "":
            x[user]["nivelPerm"] = nivelPerm
        if email != "":
            x[user]["email"] = email
        with open(z, "w", encoding="utf-8") as a:
            for f in users.values():
                linha = f"{f['nome'].replace(' ', '-')} {f['email']} {f['senha']} {f['nivelPerm']}\n"
                a.write(linha)
        print("Usuario editado com sucesso\n\n")
    else:
        print("Usuario não encontrado\n\n")

def apagar_usuario(x=users, z=arquivo):
    apag_user = input("\nDigite o email do usuario que deseja editar: ")
    if apag_user in users:
        del x[apag_user]
        with open(z, "w", encoding="utf-8") as a:
            for f in users.values():
                linha = f"{f['nome'].replace(' ', '-')} {f['email']} {f['senha']} {f['nivelPerm']}\n"
                a.write(linha)
        print("Usuario editado com sucesso\n\n")
    else:
        print("Usuario não encontrado\n\n")

def gerenciar_usuarios(x=users, z=arquivo):
    while True:
        print("\n Opção 1: Adicionar usuario\n Opção 2: Editar usuario\n Opção 3: Remover usuario\n Opção 4: Vizualizar usuarios\n Opção 5: Voltar\n")
        user_op = input("\nQual opção você deseja acessar? \n")
        if user_op == "1":
            criar_usuario()
        elif user_op == "2":
            editar_usuario()
        elif user_op == "3":
            apagar_usuario()
        elif user_op == "4":
            vizualizar_usuarios()
        elif user_op == "5":
            print("\nVoltando a tela anterior...\n")
            break
        else:
            print("Opção invalida")

def trocar_senha(y, x=users, z=arquivo):
    print("\nPara manter os dados \nanteriores aperte 'enter' quando \nsolicitar o novo dado\n\n")
    senha = input("Digite a nova senha do usuario: ")
    if senha != "":
        x[y]["senha"] = senha
        with open(z, "w", encoding="utf-8") as a:
            for f in users.values():
                linha = f"{f['nome'].replace(' ', '-')} {f['email']} {f['senha']} {f['nivelPerm']}\n"
                a.write(linha)
        print("Senha alterada com sucesso!\n\n")
    else:
        print("Senha não alterada\n\n")

def login_usuario(x, y, z):
    if y in x and x[y]["senha"] == z:
        return True
    return False

while login_status == 0:
    print("\nSeja bem vindo(a) ao nosso sistema\n\n Opção 1: Login\n Opção 2: Criar usuario\n Opção 3: Sair\n")
    inicio = input("Qual opção você deseja acessar? \n\n")
    if inicio == "1":
        for i in range(3):
            email = input("\nDigite seu email: ")
            senha = input("Digite sua senha: ")
            if login_usuario(users, email, senha):
                print("Login bem sucedido!!!")
                login_status = 1
                break
            else:
                print("\nUsuario ou senha incorreto")
        else:
            print("Excesso de tentativas, tente novamente mais tarde...")
    elif inicio == "2":
        print("\nBem vindo(a) a criação de usuario!!!")
        criar_usuario_menu()
    elif inicio == "3":
        sair()
    else:
        print("Opção invalida")

while True:
    perm = users[email]["nivelPerm"]
    if perm == "usuario":
        users = ler_arquivo_usuarios()
        produtos = ler_arquivo_produtos()
        print(f"Bem vindo(a) {users[email]['nome'].split(' ')[0]}")
        while True:
            print("\n Opção 1: Vizualizar produtos/serviços\n Opção 2: Vizualizar meus dados de usuario\n Opção 3: Trocar senha\n Opção 4: Sair\n")
            inicio_user = input("Qual opção você deseja acessar? \n\n")
            if inicio_user == "1":
                vizualizar_produtos()
            elif inicio_user == "2":
                print(users[email])
            elif inicio_user == "3":
                trocar_senha(email)
            elif inicio_user == "4":
                sair()
            else:
                print("Opção invalida")
    elif perm == "gerente":
        users = ler_arquivo_usuarios()
        produtos = ler_arquivo_produtos()
        print(f"Bem vindo(a) {users[email]['nome'].split(' ')[0]}")
        while True:
            print("\n Opção 1: Gerenciar produtos\n Opção 2: Vizualizar usuarios\n Opção 3: Pesquisar\n Opção 4: Sair\n")
            inicio_geren = input("Qual opção você deseja acessar? \n")
            if inicio_geren == "1":
                gerenciar_produtos()
            elif inicio_geren == "2":
                vizualizar_usuarios()
            elif inicio_geren == "3":
                pesquisar()
            elif inicio_geren == "4":
                sair()
            else:
                print("Opção invalida")
    elif perm == "administrador":
        users = ler_arquivo_usuarios()
        produtos = ler_arquivo_produtos()
        print(f"Bem vindo(a) {users[email]['nome'].split(' ')[0]}")
        while True:
            print("\n Opção 1: Gerenciar usuarios\n Opção 2: Gerenciar produtos/serviços\n Opção 3: Vizualizar usuarios\n Opção 4: Vizualizar produtos/serviços\n Opção 5: Pesquisar\n Opção 6: Sair\n")
            inicio_adm = input("Qual opção você deseja acessar? \n\n")
            if inicio_adm == "1":
                gerenciar_usuarios()
            elif inicio_adm == "2":
                gerenciar_produtos()
            elif inicio_adm == "3":
                vizualizar_usuarios()
            elif inicio_adm == "4":
                vizualizar_produtos()
            elif inicio_adm == "5":
                pesquisar()
            elif inicio_adm == "6":
                sair()
            else:
                print("Opção invalida")
    else:
        print("\nErro nas permissões de usuario\nEncerrando o sistema...\n\nContate o administrador")
        sys.exit()