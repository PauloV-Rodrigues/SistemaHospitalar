import pandas as pd
from modulos.utilitarios import limpar_tela
from modulos.utilitarios import limpar_tela,formatar_cpf
from modulos.configuracoes import ARQUIVO_PACIENTES, ARQUIVO_AGENDAMENTOS

def cadastrar_paciente():
    pass

def cadastrar_medico():
    pass

def historico_agendamentos():
    limpar_tela()

    print("=" * 60)
    print("HISTÓRICO DE AGENDAMENTOS")
    print("=" * 60)

    cpf = formatar_cpf(input("\nCPF do paciente: "))

    try:
        pacientes = pd.read_csv(ARQUIVO_PACIENTES,dtype=str)
        pacientes["CPF"] = pacientes["CPF"].apply(formatar_cpf)
        paciente = pacientes[pacientes["CPF"] == cpf]

        if paciente.empty:
            print("\nPaciente não encontrado.")
            input("\nPressione ENTER para continuar...")
            return

        nome_paciente = paciente.iloc[0]["NOME"]

        agendamentos = pd.read_csv(ARQUIVO_AGENDAMENTOS)

        historico = agendamentos[agendamentos["PACIENTE"] ==nome_paciente]

        if historico.empty:
            print("\nNenhum agendamento encontrado.")

        else:
            print(f"\nPaciente: {nome_paciente}")

            for i, (_, agendamento) in enumerate(historico.iterrows(),start=1):
                print("\n" + "=" * 60)
                print(f"AGENDAMENTO {i}")
                print("=" * 60)

                print(f"Especialidade: "f"{agendamento['ESPECIALIDADE']}")
                print(f"Médico: "f"{agendamento['MEDICO']}")
                print(f"Dia: "f"{agendamento['DIA']}")
                print(f"Horário: "f"{agendamento['HORARIO']}")

        input("\nPressione ENTER para continuar...")

    except Exception as erro:
        print(f"\nErro: {erro}")
        input("\nPressione ENTER para continuar...")

def deletar_paciente():
    pass

def deletar_medico():
    pass

def cancelar_agendamento():
    limpar_tela()

    print("=" * 60)
    print("CANCELAR AGENDAMENTO")
    print("=" * 60)

    cpf = formatar_cpf(input("\nCPF do paciente: "))

    try:
        pacientes = pd.read_csv(ARQUIVO_PACIENTES,dtype=str)
        pacientes["CPF"] = pacientes["CPF"].apply(formatar_cpf)
        paciente = pacientes[pacientes["CPF"] == cpf]

        if paciente.empty:
            print("\nPaciente não encontrado.")
            input("\nPressione ENTER para continuar...")
            return

        nome_paciente = paciente.iloc[0]["NOME"]

        agendamentos = pd.read_csv(ARQUIVO_AGENDAMENTOS)

        historico = agendamentos[agendamentos["PACIENTE"] ==nome_paciente]

        if historico.empty:
            print("\nNenhum agendamento encontrado.")
            input("\nPressione ENTER para continuar...")
            return

        print(f"\nPaciente: {nome_paciente}")
        print("\nAgendamentos:\n")

        for i, (_, agendamento) in enumerate(historico.iterrows(),start=1):
            print(
                f"[{i}] "
                f"{agendamento['ESPECIALIDADE']} | "
                f"{agendamento['DIA']} | "
                f"{agendamento['HORARIO']} | "
                f"{agendamento['MEDICO']}"
            )

        escolha = int(input("\nEscolha o agendamento a cancelar: "))

        indice_real = historico.index[escolha - 1]

        agendamentos = agendamentos.drop(indice_real)

        agendamentos.to_csv(ARQUIVO_AGENDAMENTOS,index=False)

        print("\nAgendamento cancelado com sucesso.")

        input("\nPressione ENTER para continuar...")

    except ValueError:
        print("\nOpção inválida.")
        input("\nPressione ENTER para continuar...")

    except Exception as erro:
        print(f"\nErro: {erro}")
        input("\nPressione ENTER para continuar...")

def menu_admin(nome_admin):
    while True:

        limpar_tela()

        print("=" * 60)
        print("ÁREA DO ADMINISTRADOR")
        print("=" * 60)
        
        print(f"\nAdministrador: {nome_admin}")
        
        print("\nMENU:")
        print("[1] Cadastrar paciente")
        print("[2] Cadastrar médico")
        print("[3] Histórico de agendamentos")
        print("[4] Deletar paciente")
        print("[5] Deletar médico")
        print("[6] Cancelar agendamento")
        print("[0] Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            cadastrar_paciente()

        elif opcao == "2":
            cadastrar_medico()

        elif opcao == "3":
            historico_agendamentos()

        elif opcao == "4":
            deletar_paciente()

        elif opcao == "5":
            deletar_medico()

        elif opcao == "6":
            cancelar_agendamento()

        elif opcao == "0":
            print("\nSaindo da área administrativa...")
            break

        else:
            print("\nOpção inválida.")
            input("\nPressione ENTER para continuar...")