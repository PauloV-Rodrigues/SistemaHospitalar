import os

#Comentário: Função simples para limpar o terminal
def limpar_tela():
    os.system("cls || clear")

#Comentário: Função simples para formatar o CPF digitado pelo usuário, evitando que ele digite de uma forma que o sistema não compreenda
def formatar_cpf(cpf):
    cpf = str(cpf)
    cpf = cpf.replace(".", "")
    cpf = cpf.replace("-", "")
    cpf = cpf.replace(" ", "")
    return cpf