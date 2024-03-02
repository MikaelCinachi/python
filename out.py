import os

path = os.getcwd()
pastas = [i for i in os.listdir(path) if os.path.isdir(i)]

for pasta in pastas:
    path1 = os.path.join(path, pasta)

    arquivos = os.listdir(path1)
    for arquivo in arquivos:
        from_path = os.path.join(path1, arquivo)
        to_path = os.path.join(path, arquivo)
        os.replace(from_path, to_path)
    os.rmdir(path1)
    

 


