from time import sleep
from modulos.consultas import agendar_consulta, consultar_agendamentos
from modulos.utilitarios import limpar_tela

def menu_paciente(nome_paciente):
    while True:
        limpar_tela()

        print("=" * 60)
        print("ÁREA DO PACIENTE")
        print("=" * 60)

        print(f"\nPaciente: {nome_paciente}")

        print("\nMENU:")
        print("[1] Agendar consulta")
        print("[2] Agendar exames")
        print("[3] Consultar agendamentos")
        print("[4] Cancelar agendamentos")
        print("[0] Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            agendar_consulta(nome_paciente)

        elif opcao == "2":
            pass

        elif opcao == "3":
            consultar_agendamentos(nome_paciente)

        elif opcao == "4":
            pass

        elif opcao == "0":
            print("\nSaindo...")
            sleep(1)
            break

        else:
            print("\nOpção inválida.")
            sleep(1)