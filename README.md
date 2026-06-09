# 🏥 Sistema Hospitalar

Sistema de gerenciamento hospitalar desenvolvido em **Python** para a disciplina de **Introdução à Programação** do curso de **Ciências Atuariais**.

O projeto utiliza **programação modular**, armazenamento em arquivos **CSV** e a biblioteca **Pandas** para manipulação de dados.

---

# 📋 Funcionalidades

## 👤 Módulo do Paciente

* Login utilizando CPF e senha.
* Agendamento de consultas.
* Consulta de consultas agendadas.
* Cancelamento de consultas.
* Agendamento de exames.
* Consulta de exames agendados.
* Cancelamento de exames.

## 🔐 Módulo Administrativo

* Login de administradores.
* Cadastro de pacientes.
* Alteração de pacientes.
* Exclusão de pacientes.
* Cadastro de médicos.
* Alteração de médicos.
* Exclusão de médicos.
* Consulta de histórico de agendamentos.
* Cancelamento de consultas de pacientes.

---

# 🏗️ Estrutura do Projeto

```text
Hospital-System/
│
├── main.py
│
├── dados/
│   ├── pacientes.csv
│   ├── admins.csv
│   ├── medicos.csv
│   ├── agendamentos.csv
│   ├── exames.csv
│   └── agendas_exames.csv
│
└── modulos/
    ├── autenticacao.py
    ├── administrador.py
    ├── paciente.py
    ├── consultas.py
    ├── menus.py
    ├── utilitarios.py
    └── configuracoes.py
```

---

# 📂 Arquivos de Dados

## pacientes.csv

Armazena os pacientes cadastrados.

```csv
ID,NOME,CPF,IDADE,DT_NASC,SENHA
1,João Silva,12345678900,25,01/01/2000,1234
```

## admins.csv

Armazena os administradores do sistema.

```csv
ID,NOME,MATRICULA,SENHA
1,Administrador,12345,admin
```

## medicos.csv

Armazena os médicos cadastrados.

```csv
ESPECIALIDADE,NOME,CRM,DIAS_DISPO,HORA_DISPO
Cardiologia,Dr(a). Pedro Gomes,CRM/CE 54535,"Segunda-feira,Terça-feira","08:00,09:00"
```

## agendamentos.csv

Armazena as consultas agendadas.

```csv
PACIENTE,ESPECIALIDADE,MEDICO,DIA,HORARIO
João Silva,Cardiologia,Dr(a). Pedro Gomes,Segunda-feira,08:00
```

## exames.csv

Lista de exames disponíveis para agendamento.

## agendas_exames.csv

Armazena os exames agendados pelos pacientes.

---

# ⚙️ Tecnologias Utilizadas

* Python 3
* Pandas
* CSV
* Programação Modular

---

# 🚀 Como Executar

## 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/hospital-system.git
```

## 2. Acessar a pasta do projeto

```bash
cd hospital-system
```

## 3. Instalar as dependências

```bash
pip install pandas
```

## 4. Executar o sistema

```bash
python main.py
```

---

# 🔑 Regras de Negócio

### Pacientes

* O login é realizado através de CPF e senha.
* O CPF é automaticamente padronizado pelo sistema.
* A senha do paciente é gerada automaticamente com 4 dígitos numéricos durante o cadastro.

### Médicos

* O prefixo **"Dr(a)."** é adicionado automaticamente.
* O CRM recebe automaticamente o prefixo **"CRM/CE"**.
* O administrador seleciona os dias e horários de atendimento.

### Consultas

* Quando uma consulta é agendada, o horário deixa de estar disponível para outros pacientes.
* Quando uma consulta é cancelada, o horário retorna automaticamente para a agenda do médico.

### Exames

* Os exames são realizados por ordem de chegada.
* O paciente escolhe apenas o tipo de exame e a data disponível.

---

# 📚 Objetivo Acadêmico

Este projeto foi desenvolvido com o objetivo de praticar conceitos fundamentais de programação, incluindo:

* Funções
* Modularização
* Manipulação de arquivos
* Estruturas de decisão
* Estruturas de repetição
* Tratamento de exceções
* Manipulação de dados com Pandas
* Organização de projetos Python

---

# 👨‍💻 Autor

Projeto desenvolvido para fins acadêmicos na disciplina de **Introdução à Programação** do curso de **Ciências Atuariais**.
