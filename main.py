from modulos.menus import boas_vindas
from modulos.autenticacao import login_paciente, login_admin
from modulos.paciente import menu_paciente
from modulos.administrador import menu_admin

while True:
    usuario = boas_vindas()

    if usuario == "admin":
        admin_logado = login_admin()

        if admin_logado:
            menu_admin(admin_logado)

    elif usuario == "paciente":
        paciente_logado = login_paciente()

        if paciente_logado:
            menu_paciente(paciente_logado)

    elif usuario == "sair":
        print("\nSistema encerrado com sucesso.")
        break