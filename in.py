import os

path = os.getcwd()
arquivos = [i for i in os.listdir(path) if os.path.isfile(i) and '.py' not in i]

tipos = list(set([i.split('.')[-1] for i in arquivos]))

for tipo in tipos:
    os.mkdir(tipo)

for arquivo in arquivos:
    from_path = os.path.join(path, arquivo)
    to_path = os.path.join(path, arquivo.split('.')[-1], arquivo)
    os.replace(from_path, to_path)



