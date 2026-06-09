import pandas as pd
import random
from modulos.utilitarios import limpar_tela,formatar_cpf
from modulos.configuracoes import ARQUIVO_PACIENTES, ARQUIVO_AGENDAMENTOS, ARQUIVO_MEDICOS

#Comentário: Função auxiliar para cadastrar os horários dos médicos
def selecionar_dias():
    dias_semana = ["Segunda-feira","Terça-feira","Quarta-feira","Quinta-feira","Sexta-feira"]

    print("\nDias disponíveis:")

    for i, dia in enumerate(dias_semana,start=1):
        print(f"[{i}] {dia}")

    print("\nDigite os números separados por vírgula.")
    exemplo = "1,3,5"
    escolha = input(f"Exemplo ({exemplo}): ")

    dias_escolhidos = []

    for numero in escolha.split(","):
        indice = int(numero.strip()) - 1
        dias_escolhidos.append(dias_semana[indice])

    return ",".join(dias_escolhidos)

#Comentário: Função auxiliar para cadastrar os horários dos médicos
def selecionar_horarios():
    horarios = ["08:00","09:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00"]
    
    print("\nHorários disponíveis:")

    for i, horario in enumerate(horarios,start=1):
        print(f"[{i}] {horario}")

    print("\nDigite os números separados por vírgula.")
    escolha = input("Exemplo (1,2,3): ")
    horarios_escolhidos = []

    for numero in escolha.split(","):
        indice = int(numero.strip()) - 1
        horarios_escolhidos.append(horarios[indice])

    return ",".join(horarios_escolhidos)

#Comentário: Função para cadastrar pacientes no sistema
def cadastrar_paciente():
    limpar_tela()

    print("=" * 60)
    print("CADASTRO DE PACIENTE")
    print("=" * 60)

    try:
        nome = input("\nNome: ").strip()

        cpf = formatar_cpf(input("CPF: "))
        idade = input("Idade: ").strip()
        data_nascimento = input("Data de nascimento (DD/MM/AAAA): ").strip()
        senha = str(random.randint(1000, 9999))

        try:
            pacientes = pd.read_csv(ARQUIVO_PACIENTES,dtype=str)

        except FileNotFoundError:
            pacientes = pd.DataFrame(columns=["ID","NOME","CPF","IDADE","DT_NASC","SENHA"])

        if not pacientes.empty:
            pacientes["CPF"] = pacientes["CPF"].apply(formatar_cpf)
            if cpf in pacientes["CPF"].values:
                print("\nPaciente já cadastrado.")
                input("\nPressione ENTER para continuar...")
                return

            novo_id = (pacientes["ID"].astype(int).max()) + 1

        else:
            novo_id = 1

        novo_paciente = pd.DataFrame([
            {
                "ID": novo_id,
                "NOME": nome,
                "CPF": cpf,
                "IDADE": idade,
                "DT_NASC": data_nascimento,
                "SENHA": senha
            }
        ])

        pacientes = pd.concat([pacientes,novo_paciente],ignore_index=True)
        pacientes.to_csv(ARQUIVO_PACIENTES,index=False)
        print("\nPaciente cadastrado com sucesso!")
        print(f"Senha gerada: {senha}")
        input("\nPressione ENTER para continuar...")

    except Exception as erro:
        print(f"\nErro: {erro}")
        input("\nPressione ENTER para continuar...")

#Comentário: Função para alterar pacientes no sistema
def alterar_paciente():
    limpar_tela()

    print("=" * 60)
    print("ALTERAÇÃO DE PACIENTE")
    print("=" * 60)

    try:
        cpf = formatar_cpf(input("\nCPF do paciente: "))
        pacientes = pd.read_csv(ARQUIVO_PACIENTES,dtype=str)
        pacientes["CPF"] = pacientes["CPF"].apply(formatar_cpf)
        paciente = pacientes[pacientes["CPF"] == cpf]

        if paciente.empty:
            print("\nPaciente não encontrado.")
            input("\nPressione ENTER para continuar...")
            return

        indice = paciente.index[0]
        nome_atual = pacientes.loc[indice,"NOME"]
        idade_atual = pacientes.loc[indice,"IDADE"]
        data_atual = pacientes.loc[indice,"DT_NASC"]
        
        print("\nDeixe em branco e pressione ENTER para manter o valor atual.")

        print("\nDados atuais:")
        print(f"Nome: {nome_atual}")
        print(f"Idade: {idade_atual}")
        print(f"Data de nascimento: {data_atual}")

        novo_nome = input(f"\nNome [{nome_atual}]: ").strip()
        nova_idade = input(f"Idade [{idade_atual}]: ").strip()
        nova_data = input(f"Data de nascimento [{data_atual}]: ").strip()

        if novo_nome == "":
            novo_nome = nome_atual

        if nova_idade == "":
            nova_idade = idade_atual

        if nova_data == "":
            nova_data = data_atual

        pacientes.loc[indice,"NOME"] = novo_nome
        pacientes.loc[indice,"IDADE"] = nova_idade
        pacientes.loc[indice,"DT_NASC"] = nova_data

        pacientes.to_csv(ARQUIVO_PACIENTES,index=False)

        print("\nPaciente alterado com sucesso!")
        input("\nPressione ENTER para continuar...")

    except FileNotFoundError:
        print("\nArquivo de pacientes não encontrado.")
        input("\nPressione ENTER para continuar...")

    except Exception as erro:
        print(f"\nErro: {erro}")
        input("\nPressione ENTER para continuar...")

#Comentário: Função para deletar pacientes no sistema
def deletar_paciente():
    limpar_tela()

    print("=" * 60)
    print("EXCLUSÃO DE PACIENTE")
    print("=" * 60)

    try:
        cpf = formatar_cpf(input("\nCPF do paciente: "))
        pacientes = pd.read_csv(ARQUIVO_PACIENTES,dtype=str)
        
        pacientes["CPF"] = pacientes["CPF"].apply(formatar_cpf)
        paciente = pacientes[pacientes["CPF"] == cpf]

        if paciente.empty:
            print("\nPaciente não encontrado.")
            input("\nPressione ENTER para continuar...")
            return

        nome = paciente.iloc[0]["NOME"]

        print(f"\nPaciente encontrado:")

        print(f"Nome: {nome}")

        confirmacao = input("\nDeseja realmente excluir? (S/N): ").upper()

        if confirmacao != "S":
            print("\nOperação cancelada.")
            input("\nPressione ENTER para continuar...")
            return

        pacientes = pacientes[pacientes["CPF"] != cpf]

        pacientes.to_csv(ARQUIVO_PACIENTES,index=False)

        print("\nPaciente removido com sucesso!")
        input("\nPressione ENTER para continuar...")

    except Exception as erro:
        print(f"\nErro: {erro}")
        input("\nPressione ENTER para continuar...")

#Comentário: Função para cadastrar médicos no sistema
def cadastrar_medico():
    limpar_tela()

    print("=" * 60)
    print("CADASTRO DE MÉDICO")
    print("=" * 60)

    try:
        especialidade = input("\nEspecialidade: ").strip()
        nome = input("Nome do médico: ").strip()
        crm_numero = input("CRM (5 dígitos): ").strip()

        nome = f"Dr(a). {nome}"
        crm = f"CRM/CE {crm_numero}"
        dias = selecionar_dias()
        horarios = selecionar_horarios()

        novo_medico = pd.DataFrame([
            {
                "ESPECIALIDADE": especialidade,
                "NOME": nome,
                "CRM": crm,
                "DIAS_DISPO": dias,
                "HORA_DISPO": horarios
            }
        ])

        try:
            medicos = pd.read_csv(ARQUIVO_MEDICOS)
            medicos = pd.concat([medicos,novo_medico],ignore_index=True)

        except FileNotFoundError:
            medicos = novo_medico

        medicos.to_csv(ARQUIVO_MEDICOS,index=False)

        print("\nMédico cadastrado com sucesso!")
        input("\nPressione ENTER para continuar...")

    except Exception as erro:
        print(f"\nErro: {erro}")
        input("\nPressione ENTER para continuar...")

#Comentário: Função para alterar médicos no sistema
def alterar_medico():
    limpar_tela()

    print("=" * 60)
    print("ALTERAÇÃO DE MÉDICO")
    print("=" * 60)

    try:
        crm_numero = input("\nCRM (5 dígitos): ").strip()

        crm = f"CRM/CE {crm_numero}"

        medicos = pd.read_csv(ARQUIVO_MEDICOS)
        medico = medicos[medicos["CRM"] == crm]

        if medico.empty:
            print("\nMédico não encontrado.")
            input("\nPressione ENTER para continuar...")
            return

        indice = medico.index[0]

        print(f"\nMédico: "f"{medicos.loc[indice,'NOME']}")
        print(f"Especialidade: "f"{medicos.loc[indice,'ESPECIALIDADE']}")
        
        print("\nSelecione os novos dias:")
        novos_dias = selecionar_dias()

        print("\nSelecione os novos horários:")
        novos_horarios = (selecionar_horarios())

        medicos.loc[indice,"DIAS_DISPO"] = novos_dias
        medicos.loc[indice,"HORA_DISPO"] = novos_horarios

        medicos.to_csv(ARQUIVO_MEDICOS,index=False)

        print("\nMédico alterado com sucesso!")
        input("\nPressione ENTER para continuar...")

    except Exception as erro:
        print(f"\nErro: {erro}")
        input("\nPressione ENTER para continuar...")

#Comentário: Função para deletar médicos no sistema
def deletar_medico():
    limpar_tela()

    print("=" * 60)
    print("EXCLUSÃO DE MÉDICO")
    print("=" * 60)

    try:
        crm_numero = input("\nCRM (5 dígitos): ").strip()
        crm = f"CRM/CE {crm_numero}"

        medicos = pd.read_csv(ARQUIVO_MEDICOS)
        medico = medicos[medicos["CRM"] == crm]

        if medico.empty:
            print("\nMédico não encontrado.")
            input("\nPressione ENTER para continuar...")
            return

        nome = medico.iloc[0]["NOME"]

        print(f"\nMédico encontrado:")
        print(f"Nome: {nome}")

        confirmacao = input("\nDeseja realmente excluir? (S/N): ").upper()

        if confirmacao != "S":
            print("\nOperação cancelada.")
            input("\nPressione ENTER para continuar...")
            return

        medicos = medicos[medicos["CRM"] != crm]
        medicos.to_csv(ARQUIVO_MEDICOS,index=False)

        print("\nMédico removido com sucesso!")
        input( "\nPressione ENTER para continuar...")

    except Exception as erro:
        print(f"\nErro: {erro}")
        input("\nPressione ENTER para continuar...")

#Comentário: Função para consultar histórico de consultas
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

#Comentário: Função para cancelar uma consulta
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
        agendamento_cancelado = (historico.loc[indice_real])
        
        nome_medico = (agendamento_cancelado["MEDICO"])
        horario_cancelado = (agendamento_cancelado["HORARIO"])
        medicos = pd.read_csv(ARQUIVO_MEDICOS)
        medico = medicos[medicos["NOME"] ==nome_medico]

        if not medico.empty:
            indice_medico = medico.index[0]
            horarios_atuais = str(medicos.loc[indice_medico,"HORA_DISPO"])

            if (horarios_atuais == "nan"or horarios_atuais.strip() == ""):
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

        print("\nAgendamento cancelado com sucesso.")
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

#Comentário: Função principal que chama o menu do admin e as devidas funções dos módulos
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
        print("[3] Alterar paciente")
        print("[4] Alterar médico")
        print("[5] Deletar paciente")
        print("[6] Deletar médico")
        print("[7] Histórico de agendamentos")
        print("[8] Cancelar agendamento")
        print("[0] Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            cadastrar_paciente()

        elif opcao == "2":
            cadastrar_medico()

        elif opcao == "3":
            alterar_paciente()

        elif opcao == "4":
            alterar_medico()

        elif opcao == "5":
            deletar_paciente()

        elif opcao == "6":
            deletar_medico()
        
        elif opcao == "7":
            historico_agendamentos()
            
        elif opcao == "8":
            cancelar_agendamento()

        elif opcao == "0":
            print("\nSaindo da área administrativa...")
            break

        else:
            print("\nOpção inválida.")
            input("\nPressione ENTER para continuar...")