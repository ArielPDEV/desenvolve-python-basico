URLs = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]
dominios = []
for i in URLs:
    nome = i[4:-4]
    dominios.append(nome)
print("URL's: ", URLs)
print("Dominios: ", dominios)