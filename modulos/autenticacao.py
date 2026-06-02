import pandas as pd
from time import sleep
from getpass import getpass
from modulos.configuracoes import ARQUIVO_PACIENTES, ARQUIVO_ADMINS
from modulos.utilitarios import limpar_tela, formatar_cpf

def login_paciente():
    while True:
        limpar_tela()

        print("=" * 60)
        print("LOGIN DO PACIENTE")
        print("=" * 60)

        print("\nDigite [0] no CPF para voltar ao menu inicial.")

        cpf_digitado = input("\nCPF: ")

        if cpf_digitado == "0":
            return None

        senha_digitada = getpass("Senha: ")

        cpf_digitado = formatar_cpf(cpf_digitado)
        senha_digitada = str(senha_digitada).strip()

        try:
            pacientes = pd.read_csv(ARQUIVO_PACIENTES,dtype=str)

            pacientes.columns = pacientes.columns.str.strip()

            pacientes["CPF"] = pacientes["CPF"].apply(formatar_cpf)

            pacientes["SENHA"] = (pacientes["SENHA"].astype(str).str.strip())

            usuario = pacientes[
                (pacientes["CPF"] == cpf_digitado) &
                (pacientes["SENHA"] == senha_digitada)
            ]

            if not usuario.empty:
                nome = usuario.iloc[0]["NOME"]

                print("\nLogin realizado com sucesso!")
                print(f"Bem-vindo(a), {nome}.")

                sleep(2)

                return nome

            else:
                print("\nCPF ou senha inválidos.")
                input("\nPressione ENTER para continuar...")

        except FileNotFoundError:
            print("\nArquivo de pacientes não encontrado.")
            input("\nPressione ENTER para continuar...")

        except Exception as erro:
            print(f"\nErro ao realizar login: {erro}")
            input("\nPressione ENTER para continuar...")
            
def login_admin():
    while True:
        limpar_tela()

        print("=" * 60)
        print("LOGIN DO ADMINISTRADOR")
        print("=" * 60)

        print("\nDigite [0] na matrícula para voltar ao menu inicial.")

        matricula_digitada = input("\nMatrícula: ").strip()

        if matricula_digitada == "0":
            return None

        senha_digitada = getpass("Senha: ").strip()

        try:
            admins = pd.read_csv(
                ARQUIVO_ADMINS,
                dtype=str
            )

            admins.columns = admins.columns.str.strip()

            admins["MATRICULA"] = (
                admins["MATRICULA"]
                .astype(str)
                .str.strip()
            )

            admins["SENHA"] = (
                admins["SENHA"]
                .astype(str)
                .str.strip()
            )

            usuario = admins[
                (admins["MATRICULA"] == matricula_digitada) &
                (admins["SENHA"] == senha_digitada)
            ]

            if not usuario.empty:
                nome = usuario.iloc[0]["NOME"]

                print("\nLogin realizado com sucesso!")
                print(f"Bem-vindo(a), {nome}.")

                sleep(2)

                return nome

            else:
                print("\nMatrícula ou senha inválidas.")
                input("\nPressione ENTER para continuar...")

        except FileNotFoundError:
            print("\nArquivo de administradores não encontrado.")
            input("\nPressione ENTER para continuar...")

        except Exception as erro:
            print(f"\nErro ao realizar login: {erro}")
            input("\nPressione ENTER para continuar...")