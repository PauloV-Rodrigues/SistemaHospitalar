from time import sleep
from modulos.consultas import agendar_consulta, agendar_exame, consultar_agendamentos, consultar_exames, cancelar_agendamento_paciente, cancelar_exame
from modulos.utilitarios import limpar_tela

#Comentário: Função principal que chama o menu do paciente e as devidas funções dos módulos
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
        print("[3] Consultar consultas")
        print("[4] Consultar exames")
        print("[5] Cancelar consultas")
        print("[6] Cancelar exames")
        print("[0] Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            agendar_consulta(nome_paciente)

        elif opcao == "2":
            agendar_exame(nome_paciente)

        elif opcao == "3":
            consultar_agendamentos(nome_paciente)
        
        elif opcao == '4':
            consultar_exames(nome_paciente)

        elif opcao == "5":
            cancelar_agendamento_paciente(nome_paciente)
        
        elif opcao == '6':
            cancelar_exame(nome_paciente)

        elif opcao == "0":
            print("\nSaindo...")
            sleep(1)
            break

        else:
            print("\nOpção inválida.")
            sleep(1)