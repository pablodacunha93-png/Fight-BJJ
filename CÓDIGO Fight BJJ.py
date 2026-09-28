from datetime import date

print("Sejam bem-vindos ao Fight BJJ!")

alunos = []
presencas = []


# ==============================
# FUNÇÕES DE VALIDAÇÃO
# ==============================

def pedir_texto(mensagem):
    while True:
        valor = input(mensagem).strip()

        if valor == "":
            print("Campo obrigatório! Não pode ficar vazio.")
        else:
            return valor


def pedir_numero(mensagem):
    while True:
        valor = input(mensagem).strip()

        if valor.isdigit():
            return int(valor)

        print("Digite apenas números!")


def pedir_peso(mensagem):
    while True:
        valor = input(mensagem).strip().replace(",", ".")

        try:
            peso = float(valor)

            if peso > 0:
                return peso

            print("O peso deve ser maior que zero.")

        except ValueError:
            print("Digite apenas números! Exemplo: 80 ou 80.5")


# ==============================
# MENU PRINCIPAL
# ==============================

while True:

    print("\n==============================")
    print("         FIGHT BJJ")
    print("==============================")

    print("1 - Já tenho cadastro")
    print("2 - Cadastrar aluno")
    print("3 - Registrar presença")
    print("4 - Lista de presença")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    # ==============================
    # LOGIN
    # ==============================

    if opcao == "1":

        login = pedir_texto("Digite seu login: ")
        senha = pedir_texto("Digite sua senha: ")

        encontrou = False

        for aluno in alunos:

            if aluno[4].lower() == login.lower() and aluno[5] == senha:

                print("\nSeja bem-vindo,", aluno[0])

                if aluno[6] != "":
                    print("Apelido:", aluno[6])

                encontrou = True
                break

        if not encontrou:
            print("\nLogin ou senha incorretos!")

    # ==============================
    # CADASTRO
    # ==============================

    elif opcao == "2":

        print("\n===== CADASTRO DE ALUNO =====")

        nome = pedir_texto("Digite o nome do aluno: ")

        # Verifica nome repetido
        nome_repetido = False

        for aluno in alunos:

            if aluno[0].lower() == nome.lower():

                nome_repetido = True
                break

        if nome_repetido:

            print("\nEsse nome já está cadastrado.")

            apelido = pedir_texto(
                "Digite um apelido para diferenciar o aluno: "
            )

        else:

            apelido = ""

        # IDADE
        idade = pedir_numero("Digite a idade: ")

        if idade <= 0 or idade > 120:

            print("Idade inválida!")

            continue

        # FAIXA
        print("\n===== FAIXA =====")
        print("1 - Branca")
        print("2 - Azul")
        print("3 - Roxa")
        print("4 - Marrom")
        print("5 - Preta")

        while True:

            opcao_faixa = input("Escolha a faixa: ").strip()

            if opcao_faixa == "1":
                faixa = "Branca"
                break

            elif opcao_faixa == "2":
                faixa = "Azul"
                break

            elif opcao_faixa == "3":
                faixa = "Roxa"
                break

            elif opcao_faixa == "4":
                faixa = "Marrom"
                break

            elif opcao_faixa == "5":
                faixa = "Preta"
                break

            else:
                print("Opção inválida! Escolha de 1 a 5.")

        # PESO
        peso = pedir_peso("Digite o seu peso: ")

        # LOGIN
        while True:

            login = pedir_texto("Crie seu login: ")

            login_existe = False

            for aluno in alunos:

                if aluno[4].lower() == login.lower():

                    login_existe = True
                    break

            if login_existe:

                print("Esse login já está sendo usado.")

            else:

                break

        # SENHA
        senha = pedir_texto("Crie sua senha: ")

        # CADASTRA ALUNO
        alunos.append(
            (nome, idade, faixa, peso, login, senha, apelido)
        )

        print("\nAluno cadastrado com sucesso!")

        if apelido != "":
            print("Identificação:", nome, "-", apelido)

    # ==============================
    # REGISTRAR PRESENÇA
    # ==============================

    elif opcao == "3":

        print("\n===== REGISTRAR PRESENÇA =====")

        login = pedir_texto("Digite seu login: ")

        encontrou = False

        for aluno in alunos:

            if aluno[4].lower() == login.lower():

                encontrou = True

                hoje = date.today()

                ja_presente = False

                for presenca in presencas:

                    if (
                        presenca[0].lower() == login.lower()
                        and presenca[1] == hoje
                    ):

                        ja_presente = True
                        break

                if ja_presente:

                    print("\nPresença já registrada hoje!")

                else:

                    presencas.append((login, hoje))

                    print(
                        "\nPresença registrada com sucesso!"
                    )

                    print("Aluno:", aluno[0])

                break

        if not encontrou:

            print("\nAluno não encontrado!")

    # ==============================
    # LISTA DE PRESENÇA
    # ==============================

    elif opcao == "4":

        print("\n===== LISTA DE PRESENÇA =====")

        if len(presencas) == 0:

            print("Nenhuma presença registrada.")

        else:

            for presenca in presencas:

                login = presenca[0]
                data = presenca[1]

                for aluno in alunos:

                    if aluno[4].lower() == login.lower():

                        print("------------------------------")

                        if aluno[6] != "":

                            print(
                                "Aluno:",
                                aluno[0],
                                "(" + aluno[6] + ")"
                            )

                        else:

                            print("Aluno:", aluno[0])

                        print(
                            "Faixa:",
                            aluno[2]
                        )

                        print(
                            "Data:",
                            data.strftime("%d/%m/%Y")
                        )

                        break

    # ==============================
    # SAIR
    # ==============================

    elif opcao == "5":

        print("\nEncerrando sistema...")
        break

    else:

        print("\nOpção inválida! Escolha de 1 a 5.")