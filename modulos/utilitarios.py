import os

def limpar_tela():
    os.system("cls || clear")

def formatar_cpf(cpf):
    cpf = str(cpf)
    cpf = cpf.replace(".", "")
    cpf = cpf.replace("-", "")
    cpf = cpf.replace(" ", "")
    return cpf