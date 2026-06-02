from time import sleep
from modulos.utilitarios import limpar_tela

def boas_vindas():
    limpar_tela()

    print("=" * 60)
    print("🏥        SISTEMA HOSPITALAR        🏥")
    print("=" * 60)

    sleep(1)

    print("\nSelecione o módulo desejado:\n")

    print("[1] Administrador")
    print("[2] Paciente")
    print("[0] Encerrar sistema")

    while True:
        opcao = input("\nDigite sua opção: ")

        if opcao == "1":
            print("\nRedirecionando para o módulo administrativo...")
            sleep(1)
            return "admin"

        elif opcao == "2":
            print("\nRedirecionando para o módulo do paciente...")
            sleep(1)
            return "paciente"

        elif opcao == "0":
            print("\nEncerrando sistema...")
            sleep(1)
            return "sair"

        else:
            print("\nOpção inválida! Tente novamente.")