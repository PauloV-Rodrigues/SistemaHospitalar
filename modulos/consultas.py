import os
import pandas as pd
from modulos.configuracoes import (ARQUIVO_MEDICOS,ARQUIVO_AGENDAMENTOS)
from modulos.utilitarios import limpar_tela

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
        agendamentos = pd.read_csv(
            ARQUIVO_AGENDAMENTOS
        )

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
    medicos = pd.read_csv(
        ARQUIVO_MEDICOS
    )

    horarios = medicos.loc[
        indice_medico,
        "HORA_DISPO"
    ]

    lista_horarios = [
        h.strip()
        for h in horarios.split(",")
    ]

    lista_horarios.remove(
        horario_escolhido
    )

    medicos.loc[
        indice_medico,
        "HORA_DISPO"
    ] = ",".join(lista_horarios)

    medicos.to_csv(
        ARQUIVO_MEDICOS,
        index=False
    )

def consultar_agendamentos(nome_paciente):
    limpar_tela()

    print("=" * 60)
    print("CONSULTA DE AGENDAMENTOS")
    print("=" * 60)

    try:
        agendamentos = pd.read_csv(
            ARQUIVO_AGENDAMENTOS
        )

        agendamentos_paciente = agendamentos[
            agendamentos["PACIENTE"] == nome_paciente
        ]

        if agendamentos_paciente.empty:
            print("\nNenhum agendamento encontrado.")

        else:
            print(f"\nPaciente: {nome_paciente}")

            print("\nSeus agendamentos:\n")

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
        print("\nArquivo de agendamentos não encontrado.")
        input("\nPressione ENTER para continuar...")

    except Exception as erro:
        print(f"\nErro: {erro}")
        input("\nPressione ENTER para continuar...")


def agendar_consulta(nome_paciente):
    limpar_tela()

    print("=" * 60)
    print("AGENDAMENTO DE CONSULTA")
    print("=" * 60)

    try:
        medicos = pd.read_csv(
            ARQUIVO_MEDICOS
        )

        especialidades = medicos[
            "ESPECIALIDADE"
        ].unique()

        print("\nEspecialidades disponíveis:\n")

        for i, especialidade in enumerate(
            especialidades,
            start=1
        ):
            print(f"[{i}] {especialidade}")

        escolha_especialidade = int(
            input("\nEscolha uma especialidade: ")
        )

        especialidade_selecionada = especialidades[
            escolha_especialidade - 1
        ]

        limpar_tela()

        medicos_especialidade = medicos[
            medicos["ESPECIALIDADE"] ==
            especialidade_selecionada
        ]

        print("\nMédicos disponíveis:\n")

        for i, (_, medico) in enumerate(
            medicos_especialidade.iterrows(),
            start=1
        ):
            print(f"[{i}] {medico['NOME']}")

        escolha_medico = int(
            input("\nEscolha um médico: ")
        )

        medico_selecionado = medicos_especialidade.iloc[
            escolha_medico - 1
        ]

        indice_medico = medico_selecionado.name

        dias = medico_selecionado[
            "DIAS_DISPO"
        ].split(",")

        limpar_tela()

        for i, dia in enumerate(
            dias,
            start=1
        ):
            print(f"[{i}] {dia.strip()}")

        escolha_dia = int(
            input("\nEscolha um dia: ")
        )

        dia_selecionado = dias[
            escolha_dia - 1
        ].strip()

        horarios = medico_selecionado[
            "HORA_DISPO"
        ].split(",")

        limpar_tela()

        for i, horario in enumerate(
            horarios,
            start=1
        ):
            print(f"[{i}] {horario.strip()}")

        escolha_horario = int(
            input("\nEscolha um horário: ")
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

        print("\nConsulta agendada com sucesso!")

        input("\nPressione ENTER para continuar...")

    except FileNotFoundError:
        print("\nArquivo não encontrado.")
        input("\nPressione ENTER para continuar...")

    except ValueError:
        print("\nEntrada inválida.")
        input("\nPressione ENTER para continuar...")

    except IndexError:
        print("\nOpção inexistente.")
        input("\nPressione ENTER para continuar...")

    except Exception as erro:
        print(f"\nErro: {erro}")
        input("\nPressione ENTER para continuar...")