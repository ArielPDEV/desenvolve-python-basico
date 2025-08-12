classe = (input("Qual a sua classe? (guerreiro, mago ou arqueiro): "))
forca = int(input("Qual a força do seu personagem? "))
magia = int(input("Qual a magia do personagem? "))
guerreiro = classe == "guerreiro" and forca >= 15 and magia < 10
mago = classe == "mago" and forca < 10 and magia >= 15
magia_arco = magia > 5 and magia >= 15
forca_arco = forca > 5 and forca >= 15
arqueiro = classe == "arqueiro" and forca_arco and magia_arco
print(f"Pontos de atributo consistentes com a classe escolhida: {guerreiro or mago or arqueiro}")