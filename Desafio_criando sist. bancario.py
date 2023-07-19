
menu = """
        =========BANCO DIO=========
        
BEM-VINDO AO BANCO DIO, DIGITE A OPÇÃO DESEJADA:

(D) DEPÓSITO
(S) SAQUE
(E) EXTRATO
(SS) SAIR

        ===========================
"""
#print(menu)

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
limite_saque = 3

while True:
        
	opção = input(menu)

	if opção == "D":
		valor = float(input("Qual o valor do depósito? \n"))

		if valor > 0:
			saldo += valor
			print (f"Valor de R$ {valor:.2f} depositado com sucesso!")
			extrato += f"Depósito: R$ {valor:.2f}\n"

		else:
			print("Valor informado é invalido para esta operação")
		
	elif opção == "S":
		valor = float(input("Qual o valor do saque? \n"))

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

	elif opção == "E":
		print("\n===============EXTRATO==============")
		print("Nenhuma operação realizada até este momento" if not extrato else extrato)
		print(f"\nSaldo: R$ {saldo:.2f}\n")
		print("======================================")

	elif opção == "SS":
		break

	else:
		print("Opção inválida: digite os valores informados no MENU")