import shutil, os

arquivo = input("nome do arquivo: ")
operacao = int(input("digite o numero da operação: \n1 - apagar\n2 - copiar\n3 - mover\n"))


if (operacao == 1):
    try:
        os.remove(arquivo)
    except FileNotFoundError:
        print("arquivo não encontrado")
    else:
        print("arquivo deletado com sucesso")
if (operacao == 2):
    try:
        shutil.copyfile(arquivo,f'copia {arquivo}')
    except FileNotFoundError:
        print("arquivo não encontrado")
    else:
        print("arquivo copiado com sucesso")
if (operacao == 3):
    try:
        shutil.move(arquivo)
    except FileNotFoundError:
        print("arquivo não encontrado")
    else:
        print("arquivo movido com sucesso")