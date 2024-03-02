import os


def CriarBagunca():
    ## Criar Pasta com varios ficheiros diferentes


    #0 Criar Pasta no diretorio corrente
    os.mkdir('PastaBagunca')

    #1 Tipos de ficheiros a criar
    l = ['.txt','.csv','.pdf','.jpeg','.ico','.json','.doc','.xls']

    #2 Criar os nomes dos ficheiros e gravar numa nova lista
    # Aqui quero criar uma string com os nomes dos ficheiros tipo teste.txt
    lista_nomes_ficheiros = []
    for j in range(len(l)):
        for i in range(10):
            nome_ficheiro = 'teste_'+ str(i) +l[j]
            lista_nomes_ficheiros.append(nome_ficheiro)

    #3 Apontar para a pasta bagunca
    pastabagunca = os.getcwd() + '\\PastaBagunca'
    os.chdir(pastabagunca)

    #4 Criar os ficheiros
    for i in range(len(lista_nomes_ficheiros)):
        cmd='type nul > '+lista_nomes_ficheiros[i]
        print(os.system(cmd))

CriarBagunca()