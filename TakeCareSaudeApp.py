# Definindo variáveis e listas
pacientes = []
consultas_agendadas = []
teleconsultas = []  # Lista para armazenar informações de teleconsulta
exames = []  # Lista para armazenar informações de exames
# Definindo funções principais
def menu_principal():
    print("\n--- Take Care Saúde ---")
    print("1. Cadastrar Paciente")
    print("2. Agendar Consulta")
    print("3. Teleconsulta")
    print("4. Marcar Exame")
    print("5. Prontuário Eletrônico")
    print("6. Recursos Educacionais")
    print("0. Sair")
def cadastrar_paciente():
    nome = input("Digite o nome do paciente: ")
    idade = input("Digite a idade do paciente: ")
    pacientes.append({"Nome": nome, "Idade": idade})
    print("Paciente cadastrado com sucesso!")
def agendar_consulta():
    print("--- Agendar Consulta ---")
    paciente_nome = input("Digite o nome do paciente: ")
    data = input("Digite a data da consulta (dd/mm/aaaa): ")
    hora = input("Digite a hora da consulta (hh:mm): ")
    # Validar dados de entrada
    if not paciente_nome or not data or not hora:
        print("Erro: Todos os campos devem ser preenchidos.")
        return
    # Solicitar o especialista desejado
    especialista_desejado = input("Digite o especialista desejado: ")
    consulta = {"Paciente": paciente_nome, "Data": data, "Hora": hora, "Especialista": especialista_desejado}
    consultas_agendadas.append(consulta)
    print(f"Consulta agendada com sucesso para {paciente_nome} com o especialista {especialista_desejado}.")
def teleconsulta():
    print("--- Teleconsulta ---")
    paciente_nome = input("Digite o nome do paciente: ")
    # Procurar paciente na lista de pacientes
    paciente = next((p for p in pacientes if p["Nome"] == paciente_nome), None)
    if paciente:
        print(f"Realizando o agendamento da teleconsulta para {paciente_nome}.")
        # Perguntar pelo especialista desejado
        especialista_desejado = input("Qual o especialista desejado? ")
        # Perguntar pela data da consulta
        data_consulta = input("Digite a data da consulta (dd/mm/aaaa): ")
        # Perguntar pela hora da teleconsulta
        hora_teleconsulta = input("Digite a hora da teleconsulta (hh:mm): ")
        # Armazenar as informações da teleconsulta
        teleconsulta_info = {"Paciente": paciente_nome, "Data": data_consulta, "Hora": hora_teleconsulta, "Especialista": especialista_desejado}
        teleconsultas.append(teleconsulta_info)
        print(
            f"Consulta marcada para {data_consulta} às {hora_teleconsulta} com o especialista {especialista_desejado}.")
    else:
        print(f"Paciente {paciente_nome} não encontrado.")
def prontuario_eletronico():
    print("--- Prontuário Eletrônico ---")
    paciente_nome = input("Digite o nome do paciente: ")
    # Procurar paciente na lista de pacientes
    paciente = next((p for p in pacientes if p["Nome"] == paciente_nome), None)
    if paciente:
        print(f"Exibindo prontuário eletrônico de {paciente_nome}.")
        # Exibir consultas agendadas para o paciente
        consultas_paciente = [consulta for consulta in consultas_agendadas if consulta["Paciente"] == paciente_nome]
        if consultas_paciente:
            print("\nConsultas agendadas:")
            for consulta in consultas_paciente:
                print(f"Data: {consulta['Data']}, Hora: {consulta['Hora']}, Especialista: {consulta['Especialista']}")
        # Exibir teleconsultas para o paciente
        teleconsultas_paciente = [teleconsulta for teleconsulta in teleconsultas if teleconsulta["Paciente"] == paciente_nome]
        if teleconsultas_paciente:
            print("\nTeleconsultas agendadas:")
            for teleconsulta in teleconsultas_paciente:
                print(f"Data: {teleconsulta['Data']}, Hora: {teleconsulta['Hora']}, Especialista: {teleconsulta['Especialista']}")
        # Exibir exames agendados para o paciente
        exames_paciente = [exame for exame in exames if exame["Paciente"] == paciente_nome]
        if exames_paciente:
            print("\nExames agendados:")
            for exame in exames_paciente:
                print(f"Tipo: {exame['Tipo']}, Data: {exame['Data']}, Hora: {exame['Hora']}")
        # Adicione mais seções conforme necessário
    else:
        print(f"Paciente {paciente_nome} não encontrado.")
def recursos_educacionais(escolha):

    match escolha:
        case 0:
            print("   - Escolha a opção 'Sair' no menu principal.")
            print("   - O programa será encerrado.")
            print(
                "Lembre-se: Sempre preencha todas as informações solicitadas para garantir o correto funcionamento do sistema.")
        case 1:
            print("1. Como cadastrar um paciente?")
            print("   - Escolha a opção 'Cadastrar Paciente' no menu principal.")
            print("   - Digite o nome e a idade do paciente quando solicitado.")
        case 2:
            print("2. Como agendar uma consulta?")
            print("   - Selecione 'Agendar Consulta' no menu.")
            print("   - Forneça o nome do paciente, a data, a hora e o especialista desejado.")
        case 3:
            print("3. Como agendar uma teleconsulta?")
            print("   - Escolha 'Teleconsulta' no menu.")
            print("   - Informe o nome do paciente, especialista desejado, data e hora da teleconsulta.")
            print("   - As teleconsultas agendadas serão exibidas no prontuário eletrônico.")
        case 4:
            print("4. Como marcar um exame?")
            print("   - Opte por 'Marcar exame' no menu.")
            print("   - Insira o nome do paciente, tipo de exame, data e hora.")
            print("   - Os exames agendados também serão exibidos no prontuário eletrônico.")
        case 5:
            print("5. Como visualizar o prontuário eletrônico?")
            print("   - Selecione 'Prontuário Eletrônico' no menu.")
            print("   - Insira o nome do paciente para ver suas consultas, teleconsultas e exames agendados.")

def marcar_exame():
    print("--- Marcar Exame ---")
    paciente_nome = input("Digite o nome do paciente: ")
    # Procurar paciente na lista de pacientes
    paciente = next((p for p in pacientes if p["Nome"] == paciente_nome), None)
    if paciente:
        print(f"Marcando exame para {paciente_nome}.")
        # Perguntar pelo tipo de exame
        tipo_exame = input("Digite o tipo de exame: ")
        # Perguntar pela data do exame
        data_exame = input("Digite a data do exame (dd/mm/aaaa): ")
        # Perguntar pela hora do exame
        hora_exame = input("Digite a hora do exame (hh:mm): ")
        # Armazenar as informações do exame
        exame_info = {"Paciente": paciente_nome, "Tipo": tipo_exame, "Data": data_exame, "Hora": hora_exame}
        exames.append(exame_info)
        print(f"Exame marcado para {data_exame} às {hora_exame} do tipo {tipo_exame} para o paciente {paciente_nome}.")
    else:
        print(f"Paciente {paciente_nome} não encontrado.")
while True:
    menu_principal()  # Exibe o menu principal
    opcao = input("Escolha uma opção (0-6): ")

    # Validação da opção
    if not opcao.isdigit() or int(opcao) not in range(7):
        print("Opção inválida. Tente novamente.")
        continue
    opcao = int(opcao)


    match opcao:
        case 0:
            print("Saindo do programa. Até logo!")
            break
        case 1:
            cadastrar_paciente()
        case 2:
            agendar_consulta()
        case 3:
            teleconsulta()
        case 4:
            marcar_exame()
        case 5:
            prontuario_eletronico()
        case 6:
            escolha = int(input("Qual opção do menu você ficou com dúvida?\n1- Cadastrar paciente"
                                + "\n2- Agendar consulta\n3- Teleconsulta\n4- Marcar exame\n5- Prontuario eletrônico\n0- Sair do programa\n"))
            recursos_educacionais(escolha)
        case _:
            print("Opção inválida. Tente novamente.")