import os
import pandas as pd
from time import sleep

ARQUIVO_PACIENTES = "dados/pacientes.csv"
ARQUIVO_MEDICOS = "dados/medicos.csv"
ARQUIVO_AGENDAMENTOS = "dados/agendamentos.csv"

def limpar_tela():
    os.system("cls || clear")

def formatar_cpf(cpf):
    cpf = str(cpf)
    
    cpf = cpf.replace(".", "")
    cpf = cpf.replace("-", "")
    cpf = cpf.replace(" ", "")
    
    return cpf

def boas_vindas():
    limpar_tela()

    print("=" * 60)
    print("🏥        SISTEMA HOSPITALAR        🏥")
    print("=" * 60)

    print("\nSeja bem-vindo ao sistema de gerenciamento hospitalar.\n")
    print("Este sistema foi desenvolvido para auxiliar no")
    print("controle administrativo e atendimento de pacientes.")

    sleep(1)

    print("\n📌 Selecione o módulo desejado:\n")

    print("[1] Administrador")
    print("[2] Paciente")
    print("[0] Encerrar sistema")

    while True:
        opcao = input("\n➡️  Digite sua opção: ")

        if opcao == "1":
            print("\n🔐 Redirecionando para o módulo administrativo...")
            sleep(1)
            return "admin"

        elif opcao == "2":
            print("\n🩺 Redirecionando para o módulo do paciente...")
            sleep(1)
            return "paciente"

        elif opcao == "0":
            print("\n🚪 Encerrando sistema...")
            sleep(1)
            return "sair"

        else:
            print("\n❌ Opção inválida! Tente novamente.")

def login_paciente():
    limpar_tela()

    print("=" * 60)
    print("🔐 LOGIN DO PACIENTE")
    print("=" * 60)

    cpf_digitado = input("\nCPF: ")
    senha_digitada = input("Senha: ")

    cpf_digitado = formatar_cpf(cpf_digitado)
    senha_digitada = str(senha_digitada).strip()

    try:
        pacientes = pd.read_csv(
            ARQUIVO_PACIENTES,
            dtype=str
        )

        pacientes.columns = pacientes.columns.str.strip()

        pacientes["CPF"] = pacientes["CPF"].apply(formatar_cpf)

        pacientes["SENHA"] = pacientes["SENHA"].astype(str).str.strip()

        usuario = pacientes[
            (pacientes["CPF"] == cpf_digitado) &
            (pacientes["SENHA"] == senha_digitada)
        ]

        if not usuario.empty:
            nome = usuario.iloc[0]["NOME"]

            print(f"\n✅ Login realizado com sucesso!")
            print(f"Bem-vindo(a), {nome}.")

            sleep(2)

            return nome

        else:
            print("\n❌ CPF ou senha inválidos.")
            sleep(2)

            return None

    except FileNotFoundError:
        print("\n❌ Arquivo de pacientes não encontrado.")
        sleep(2)

        return None

    except Exception as erro:
        print(f"\n❌ Erro ao realizar login: {erro}")
        sleep(2)

        return None

def salvar_agendamento(
    nome_paciente,
    especialidade,
    medico,
    dia,
    horario
):
    novo_agendamento = pd.DataFrame([
        {
            "PACIENTE": nome_paciente,
            "ESPECIALIDADE": especialidade,
            "MEDICO": medico,
            "DIA": dia,
            "HORARIO": horario
        }
    ])

    if os.path.exists(ARQUIVO_AGENDAMENTOS):
        agendamentos = pd.read_csv(ARQUIVO_AGENDAMENTOS)

        agendamentos = pd.concat(
            [agendamentos, novo_agendamento],
            ignore_index=True
        )

    else:
        agendamentos = novo_agendamento

    agendamentos.to_csv(
        ARQUIVO_AGENDAMENTOS,
        index=False
    )

def remover_horario_medico(
    indice_medico,
    horario_escolhido
):
    medicos = pd.read_csv(ARQUIVO_MEDICOS)

    horarios = medicos.loc[
        indice_medico,
        "HORA_DISPO"
    ]

    lista_horarios = [
        h.strip()
        for h in horarios.split(",")
    ]

    lista_horarios.remove(horario_escolhido)

    novos_horarios = ",".join(lista_horarios)

    medicos.loc[
        indice_medico,
        "HORA_DISPO"
    ] = novos_horarios

    medicos.to_csv(
        ARQUIVO_MEDICOS,
        index=False
    )

def consultar_agendamentos(nome_paciente):
    limpar_tela()

    print("=" * 60)
    print("📋 CONSULTA DE AGENDAMENTOS")
    print("=" * 60)

    try:
        agendamentos = pd.read_csv(
            ARQUIVO_AGENDAMENTOS
        )

        agendamentos_paciente = agendamentos[
            agendamentos["PACIENTE"] == nome_paciente
        ]

        if agendamentos_paciente.empty:
            print("\n❌ Nenhum agendamento encontrado.")

        else:
            print(f"\n👤 Paciente: {nome_paciente}")

            print("\n📅 Seus agendamentos:\n")

            for i, (_, agendamento) in enumerate(
                agendamentos_paciente.iterrows(),
                start=1
            ):

                print("=" * 60)
                print(f"AGENDAMENTO {i}")
                print("=" * 60)

                print(f"🏥 Especialidade: {agendamento['ESPECIALIDADE']}")
                print(f"👨‍⚕️ Médico: {agendamento['MEDICO']}")
                print(f"📅 Dia: {agendamento['DIA']}")
                print(f"⏰ Horário: {agendamento['HORARIO']}")

        input("\nPressione ENTER para continuar...")

    except FileNotFoundError:
        print("\n❌ Arquivo de agendamentos não encontrado.")
        input("\nPressione ENTER para continuar...")

    except Exception as erro:
        print(f"\n❌ Erro: {erro}")
        input("\nPressione ENTER para continuar...")

def agendar_consulta(nome_paciente):
    limpar_tela()

    print("=" * 60)
    print("📅 AGENDAMENTO DE CONSULTA")
    print("=" * 60)

    try:
        medicos = pd.read_csv(ARQUIVO_MEDICOS)

        especialidades = medicos["ESPECIALIDADE"].unique()

        print("\n🏥 Especialidades disponíveis:\n")

        for i, especialidade in enumerate(especialidades, start=1):
            print(f"[{i}] {especialidade}")

        escolha_especialidade = int(
            input("\n➡️ Escolha uma especialidade: ")
        )

        especialidade_selecionada = especialidades[
            escolha_especialidade - 1
        ]

        limpar_tela()

        print("=" * 60)
        print(f"🏥 ESPECIALIDADE: {especialidade_selecionada}")
        print("=" * 60)

        medicos_especialidade = medicos[
            medicos["ESPECIALIDADE"] == especialidade_selecionada
        ]

        print("\n👨‍⚕️ Médicos disponíveis:\n")

        for i, (_, medico) in enumerate(
            medicos_especialidade.iterrows(),
            start=1
        ):
            print(f"[{i}] {medico['NOME']}")

        escolha_medico = int(
            input("\n➡️ Escolha um médico: ")
        )

        medico_selecionado = medicos_especialidade.iloc[
            escolha_medico - 1
        ]

        indice_medico = medico_selecionado.name
        
        limpar_tela()

        dias = medico_selecionado["DIAS_DISPO"].split(",")

        print("=" * 60)
        print(f"📅 DIAS DISPONÍVEIS - {medico_selecionado['NOME']}")
        print("=" * 60)

        for i, dia in enumerate(dias, start=1):
            print(f"[{i}] {dia.strip()}")

        escolha_dia = int(
            input("\n➡️ Escolha um dia: ")
        )

        dia_selecionado = dias[escolha_dia - 1].strip()

        limpar_tela()

        horarios = medico_selecionado["HORA_DISPO"].split(",")

        print("=" * 60)
        print(f"⏰ HORÁRIOS DISPONÍVEIS")
        print("=" * 60)

        for i, horario in enumerate(horarios, start=1):
            print(f"[{i}] {horario.strip()}")

        escolha_horario = int(
            input("\n➡️ Escolha um horário: ")
        )

        horario_selecionado = horarios[
            escolha_horario - 1
        ].strip()

        salvar_agendamento(
            nome_paciente,
            especialidade_selecionada,
            medico_selecionado["NOME"],
            dia_selecionado,
            horario_selecionado
        )

        remover_horario_medico(
            indice_medico,
            horario_selecionado
        )

        limpar_tela()

        print("=" * 60)
        print("✅ CONSULTA AGENDADA COM SUCESSO")
        print("=" * 60)

        print(f"\n👤 Paciente: {nome_paciente}")
        print(f"🏥 Especialidade: {especialidade_selecionada}")
        print(f"👨‍⚕️ Médico: {medico_selecionado['NOME']}")
        print(f"📅 Dia: {dia_selecionado}")
        print(f"⏰ Horário: {horario_selecionado}")

        input("\nPressione ENTER para continuar...")

    except FileNotFoundError:
        print("\n❌ Arquivo não encontrado.")
        input("\nPressione ENTER para continuar...")

    except ValueError:
        print("\n❌ Entrada inválida.")
        input("\nPressione ENTER para continuar...")

    except IndexError:
        print("\n❌ Opção inexistente.")
        input("\nPressione ENTER para continuar...")

    except Exception as erro:
        print(f"\n❌ Erro: {erro}")
        input("\nPressione ENTER para continuar...")

def menu_paciente(nome_paciente):
    while True:
        limpar_tela()

        print("=" * 60)
        print("🩺 ÁREA DO PACIENTE")
        print("=" * 60)

        print(f"\nPaciente: {nome_paciente}")

        print("\n📌 MENU:")
        print("[1] Agendar consulta")
        print("[2] Agendar exames")
        print("[3] Consultar agendamentos")
        print("[4] Cancelar agendamentos")
        print("[0] Sair")

        opcao = input("\n➡️  Escolha uma opção: ")

        if opcao == "1":
            agendar_consulta(nome_paciente)

        elif opcao == "2":
            print("\n🧪 Função de agendamento de exames em desenvolvimento...")
            input("\nPressione ENTER para continuar...")

        elif opcao == "3":
            consultar_agendamentos(nome_paciente)

        elif opcao == "4":
            print("\n❌ Função de cancelamento em desenvolvimento...")
            input("\nPressione ENTER para continuar...")

        elif opcao == "0":
            print("\n🚪 Saindo da área do paciente...")
            sleep(1)
            break

        else:
            print("\n❌ Opção inválida.")
            sleep(1)