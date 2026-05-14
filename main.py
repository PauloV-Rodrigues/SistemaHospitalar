from funcoes import *


while True:
    usuario = boas_vindas()

    if usuario == "admin":
        print("\n🔐 Módulo administrativo em desenvolvimento...")
        input("\nPressione ENTER para continuar...")

    elif usuario == "paciente":

        paciente_logado = login_paciente()

        if paciente_logado:
            menu_paciente(paciente_logado)

    elif usuario == "sair":
        print("\n✅ Sistema encerrado com sucesso.")
        break