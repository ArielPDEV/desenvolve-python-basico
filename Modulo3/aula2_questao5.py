genero = input("Qual seu gênero? (M ou F) ")
idade = int(input("Qual a sua idade? "))
temp_servico = int(input("Quanto tempo de serviço você tem? "))
homem = genero == "M" and idade >= 65 or temp_servico >= 30
mulher = genero == "F" and idade >= 60 or temp_servico >= 25
print(f"Pode se aposentar?: {homem or mulher}")