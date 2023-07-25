def menu():
	menu = """
        =========BANCO DIO=========
        
BEM-VINDO AO BANCO DIO, DIGITE A OPÇÃO DESEJADA:

(D) DEPÓSITO
(S) SAQUE
(E) EXTRATO
(NC) NOVA CONTA
(LC) LISTAR CONTA
(NU) NOVO USUÁRIO
(SS) SAIR

        ===========================
"""
	return input(menu)

def deposito(saldo, valor, extrato, /):
	if valor > 0:
		saldo += valor
		extrato += f"Depósito: R$ {valor:.2f}\n"
		print (f"Valor de R$ {valor:.2f} depositado com sucesso!")
	else:
		print("Valor informado é invalido para esta operação")
	return saldo, extrato

def saque(*, saldo, valor, extrato, limite, numero_saque, limite_saque):

	excedeu_saldo = valor > saldo
	excedeu_limite = valor > limite
	excedeu_saque = numero_saque >= limite_saque

	if excedeu_saldo:
		print("Você excedeu o limite de saldo")

	elif excedeu_limite:
		print(f"Você excedeu o seu limite de R$ {limite} diários")

	elif excedeu_saque:
		print("Você excedeu o limite de 3 saques diários")
	
	elif valor > 0:
		print("Saque realizado com sucesso!")
		saldo -= valor
		extrato += f"Saque: R$ {valor:.2f}\n"
		numero_saque += 1

	else:
		print("O valor informado não é aceito para esta operação")

	return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
	print("\n===============EXTRATO==============")
	print("Nenhuma operação realizada até este momento" if not extrato else extrato)
	print(f"\nSaldo: R$ {saldo:.2f}\n")
	print("======================================")
	
def criar_usuario(usuarios):
	cpf = input("Informe seu CPF - somente número: ")
	usuario = filtrar_usuario(cpf, usuarios)

	if usuario:
		print("Já existe um usuário cadastrado com este CPF")
		return
	
	nome = input("Informe o seu nome completo: ")
	data_nascimento = input("Informe sua data de nascimento - dd-mm-aaaa: ")
	endereco = input("Informe seu endereço completo: ")

	usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
	print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
	usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
	return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
	cpf = input("Informe o seu CPF")
	usuario = filtrar_usuario(cpf, usuarios)

	if usuario:
		print("Conta criada com sucesso!")
		return{"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
	
	print("Usuário não encontrado")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)

def principal():
	
	saldo = 0
	limite = 500
	extrato = ""
	numero_saque = 0
	usuarios = []
	contas = []

	Agencia = "0001"
	Limite_saque = 3

	while True:
        
		opção = menu()

		if opção == "D":
			valor = float(input("Qual o valor do depósito? \n"))
			saldo, extrato = deposito(saldo, valor, extrato)

	
		elif opção == "S":
			valor = float(input("Qual o valor do saque? \n"))
			saldo, extrato = saque(
				saldo=saldo,
				valor=valor,
				extrato=extrato,
				limite=limite,
				numero_saque=numero_saque,
				limite_saque=Limite_saque,
			)

		
		elif opção == "E":
			exibir_extrato(saldo, extrato=extrato)


		elif opção == "NU":
			criar_usuario(usuarios)

	
		elif opção == "NC":
			numero_conta = len(contas) + 1
			conta = criar_conta(Agencia, numero_conta, usuarios)

			if conta:
				contas.append(conta)

		elif opção == "LC":
			listar_contas(contas)

		elif opção == "SS":
			break

		else:
			print("Opção inválida: digite os valores informados no MENU")


principal()