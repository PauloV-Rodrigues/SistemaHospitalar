import os
import pandas as pd
from modulos.configuracoes import ARQUIVO_MEDICOS,ARQUIVO_AGENDAMENTOS,ARQUIVO_EXAMES,ARQUIVO_AGENDAS_EXAMES
from modulos.utilitarios import limpar_tela

#Comentário: Função auxiliar para agendamento de consultas
def salvar_agendamento(nome_paciente,especialidade,medico,dia,horario):
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
        agendamentos = pd.concat([agendamentos, novo_agendamento],ignore_index=True)

    else:
        agendamentos = novo_agendamento

    agendamentos.to_csv(ARQUIVO_AGENDAMENTOS,index=False)

#Comentário: Função auxiliar para remover horário do médico no momento do agendamento
def remover_horario_medico(indice_medico,horario_escolhido):
    medicos = pd.read_csv(ARQUIVO_MEDICOS)
    horarios = medicos.loc[indice_medico,"HORA_DISPO"]
    lista_horarios = [
        h.strip()
        for h in horarios.split(",")
    ]

    lista_horarios.remove(horario_escolhido)
    medicos.loc[indice_medico,"HORA_DISPO"] = ",".join(lista_horarios)
    medicos.to_csv(ARQUIVO_MEDICOS,index=False)

#Comentário: Função para realizar agendamento de consulta
def agendar_consulta(nome_paciente):
    limpar_tela()

    print("=" * 60)
    print("AGENDAMENTO DE CONSULTA")
    print("=" * 60)

    try:
        medicos = pd.read_csv(ARQUIVO_MEDICOS)
        especialidades = medicos["ESPECIALIDADE"].unique()

        print("\nEspecialidades disponíveis:\n")
        for i, especialidade in enumerate(especialidades,start=1):
            print(f"[{i}] {especialidade}")

        escolha_especialidade = int(input("\nEscolha uma especialidade: "))
        especialidade_selecionada = especialidades[escolha_especialidade - 1]

        limpar_tela()

        medicos_especialidade = medicos[medicos["ESPECIALIDADE"] == especialidade_selecionada]

        print("\nMédicos disponíveis:\n")
        for i, (_, medico) in enumerate(medicos_especialidade.iterrows(),start=1):
            print(f"[{i}] {medico['NOME']}")

        escolha_medico = int(input("\nEscolha um médico: "))
        medico_selecionado = medicos_especialidade.iloc[escolha_medico - 1]
        indice_medico = medico_selecionado.name
        
        dias = medico_selecionado["DIAS_DISPO"].split(",")

        limpar_tela()

        for i, dia in enumerate(dias,start=1):
            print(f"[{i}] {dia.strip()}")

        escolha_dia = int(input("\nEscolha um dia: "))
        dia_selecionado = dias[escolha_dia - 1].strip()

        horarios = medico_selecionado["HORA_DISPO"].split(",")

        limpar_tela()

        for i, horario in enumerate(horarios,start=1):
            print(f"[{i}] {horario.strip()}")

        escolha_horario = int(input("\nEscolha um horário: "))
        horario_selecionado = horarios[escolha_horario - 1].strip()

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

#Comentário: Função para encontrar um agendamento de consulta
def consultar_agendamentos(nome_paciente):
    limpar_tela()

    print("=" * 60)
    print("CONSULTA DE AGENDAMENTOS")
    print("=" * 60)

    try:
        agendamentos = pd.read_csv(ARQUIVO_AGENDAMENTOS)
        agendamentos_paciente = agendamentos[agendamentos["PACIENTE"] == nome_paciente]

        if agendamentos_paciente.empty:
            print("\nNenhum agendamento encontrado.")

        else:
            print(f"\nPaciente: {nome_paciente}")
            print("\nSeus agendamentos:\n")
            for i, (_, agendamento) in enumerate(agendamentos_paciente.iterrows(),start=1):
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

#Comentário: Função para cancelar um agendamento de consulta
def cancelar_agendamento_paciente(nome_paciente):
    limpar_tela()
    
    print("=" * 60)
    print("CANCELAMENTO DE AGENDAMENTO")
    print("=" * 60)

    try:
        agendamentos = pd.read_csv(ARQUIVO_AGENDAMENTOS)
        agendamentos_paciente = agendamentos[agendamentos["PACIENTE"] == nome_paciente]

        if agendamentos_paciente.empty:
            print("\nNenhum agendamento encontrado.")
            input("\nPressione ENTER para continuar...")
            return

        print(f"\nPaciente: {nome_paciente}")
        print("\nAgendamentos disponíveis:\n")
        for i, (_, agendamento) in enumerate(agendamentos_paciente.iterrows(),start=1):
            print(
                f"[{i}] "
                f"{agendamento['ESPECIALIDADE']} | "
                f"{agendamento['DIA']} | "
                f"{agendamento['HORARIO']} | "
                f"{agendamento['MEDICO']}"
            )

        escolha = int(input("\nEscolha o agendamento que deseja cancelar: "))
        indice_real = agendamentos_paciente.index[escolha - 1]
        agendamento_cancelado = (agendamentos_paciente.loc[indice_real])
        
        nome_medico = (agendamento_cancelado["MEDICO"])
        horario_cancelado = (agendamento_cancelado["HORARIO"])
        medicos = pd.read_csv(ARQUIVO_MEDICOS)
        medico = medicos[medicos["NOME"] == nome_medico]

        if not medico.empty:
            indice_medico = medico.index[0]
            horarios_atuais = str(medicos.loc[indice_medico,"HORA_DISPO"])

            if (horarios_atuais == "nan" or horarios_atuais.strip() == ""):
                lista_horarios = []

            else:
                lista_horarios = [
                    h.strip()
                    for h in horarios_atuais.split(",")
                ]

            if (horario_cancelado not in lista_horarios):
                lista_horarios.append(horario_cancelado)
                lista_horarios.sort()
                medicos.loc[indice_medico,"HORA_DISPO"] = ",".join(lista_horarios)
                medicos.to_csv(ARQUIVO_MEDICOS,index=False)

        agendamentos = agendamentos.drop(indice_real)
        agendamentos.to_csv(ARQUIVO_AGENDAMENTOS,index=False)

        print("\nConsulta cancelada com sucesso!")
        input("\nPressione ENTER para continuar...")

    except ValueError:
        print("\nOpção inválida.")
        input("\nPressione ENTER para continuar...")

    except IndexError:
        print("\nAgendamento inexistente.")
        input("\nPressione ENTER para continuar...")

    except FileNotFoundError:
        print("\nArquivo não encontrado.")
        input("\nPressione ENTER para continuar...")

    except Exception as erro:
        print(f"\nErro: {erro}")
        input("\nPressione ENTER para continuar...")

#Comentário: Função para realizar agendamento de exame        
def agendar_exame(nome_paciente):
    limpar_tela()

    print("=" * 60)
    print("AGENDAMENTO DE EXAME")
    print("=" * 60)

    try:
        exames = pd.read_csv(ARQUIVO_EXAMES)

        print("\nExames disponíveis:\n")

        for i, (_, exame) in enumerate(exames.iterrows(),start=1):
            print(f"[{i}] {exame['NOME_EXAME']}")

        escolha_exame = int(input("\nEscolha um exame: "))
        exame_selecionado = exames.iloc[escolha_exame - 1]
        datas = str(exame_selecionado["DATAS_DISPO"]).split(";")

        limpar_tela()

        print("=" * 60)
        print(f"EXAME: " f"{exame_selecionado['NOME_EXAME']}")
        print("=" * 60)

        print("\nDatas disponíveis:\n")
        for i, data in enumerate(datas,start=1):
            print(f"[{i}] {data.strip()}")

        escolha_data = int(input("\nEscolha uma data: "))
        data_escolhida = datas[escolha_data - 1].strip()

        novo_agendamento = pd.DataFrame([
            {
                "PACIENTE": nome_paciente,
                "EXAME": exame_selecionado["NOME_EXAME"],
                "DATA": data_escolhida,
                "OBSERVACAO":  ("Ordem de chegada a partir das 08:00")
            }
        ])

        if os.path.exists(ARQUIVO_AGENDAS_EXAMES):
            agenda_exames = pd.read_csv(ARQUIVO_AGENDAS_EXAMES)
            agenda_exames = pd.concat([agenda_exames,novo_agendamento],ignore_index=True)

        else:
            agenda_exames = (novo_agendamento)

        agenda_exames.to_csv(ARQUIVO_AGENDAS_EXAMES,index=False)

        limpar_tela()

        print("=" * 60)
        print("EXAME AGENDADO COM SUCESSO")
        print("=" * 60)

        print(f"\nPaciente: " f"{nome_paciente}")
        print(f"Exame: " f"{exame_selecionado['NOME_EXAME']}")
        print(f"Data: " f"{data_escolhida}")
        print("\nCompareça a partir das 08:00.")
        print("O atendimento ocorre por ordem de chegada.")
        input("\nPressione ENTER para continuar...")

    except FileNotFoundError:
        print("\nArquivo de exames não encontrado.")
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

#Comentário: Função para encontrar um agendamento de exame        
def consultar_exames(nome_paciente):
    limpar_tela()

    print("=" * 60)
    print("CONSULTA DE EXAMES")
    print("=" * 60)

    try:
        exames = pd.read_csv(ARQUIVO_AGENDAS_EXAMES)
        exames_paciente = exames[exames["PACIENTE"] == nome_paciente]

        if exames_paciente.empty:
            print("\nNenhum exame agendado.")
        else:
            print(f"\nPaciente: {nome_paciente}")
            print("\nExames agendados:\n")

            for i, (_, exame) in enumerate(exames_paciente.iterrows(),start=1):
                print("=" * 60)
                print(f"EXAME {i}")
                print("=" * 60)

                print(f"🧪 Exame: " f"{exame['EXAME']}")
                print(f"📅 Data: " f"{exame['DATA']}")
                print(f"ℹ️ Observação: " f"{exame['OBSERVACAO']}")

        input("\nPressione ENTER para continuar...")

    except FileNotFoundError:
        print("\nArquivo de exames não encontrado.")
        input("\nPressione ENTER para continuar...")

    except Exception as erro:
        print(f"\nErro: {erro}")
        input("\nPressione ENTER para continuar...")

#Comentário: Função para cancelar um agendamento de exame
def cancelar_exame(nome_paciente):
    limpar_tela()

    print("=" * 60)
    print("CANCELAMENTO DE EXAME")
    print("=" * 60)

    try:
        exames = pd.read_csv(ARQUIVO_AGENDAS_EXAMES)
        exames_paciente = exames[exames["PACIENTE"] == nome_paciente]

        if exames_paciente.empty:
            print("\nNenhum exame agendado.")
            input("\nPressione ENTER para continuar...")
            return

        print(f"\nPaciente: {nome_paciente}")
        print("\nExames agendados:\n")

        for i, (_, exame) in enumerate(exames_paciente.iterrows(),start=1):
            print(
                f"[{i}] "
                f"{exame['EXAME']} | "
                f"{exame['DATA']}"
            )

        escolha = int(input("\nEscolha o exame que deseja cancelar: "))
        indice_real = exames_paciente.index[escolha - 1]
        exames = exames.drop(indice_real)
        exames.to_csv(ARQUIVO_AGENDAS_EXAMES,index=False)

        print("\nExame cancelado com sucesso!")
        input("\nPressione ENTER para continuar...")

    except ValueError:
        print("\nOpção inválida.")
        input("\nPressione ENTER para continuar...")

    except IndexError:
        print("\nExame inexistente.")
        input("\nPressione ENTER para continuar...")

    except FileNotFoundError:
        print("\nArquivo de exames não encontrado.")
        input("\nPressione ENTER para continuar...")

    except Exception as erro:
        print(f"\nErro: {erro}")
        input("\nPressione ENTER para continuar...")