mes = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro","Outubro", "Novembro", "Dezembro"]

data = input("Digite sua data de nascimento(no formato DD/MM/AAAA)")
data = data.split("/")
print(data[0])
print(data[1])
print(data[2])
print(f"Você nasceu no dia {data[0]} de {mes[int(data[1]) - 1]} de {data[2]}")