#AUTOR: Vinicius Nunes de Bona
#DATA: 30/05/2023


#DESAFIO:
#Realizar 3 saques diarios
#limite 500 reais
#caso nao haja saldo, deve informar que que nao é possível sacar o dinheiro por falta de saldo
#Todos os saques devem ser armazenados em uma variavel e exibidos na operação extrato

# Operação Extrato: 
#Deve listar todos os depósitos e saques realizados na conta. 
#No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estivar em Branco, exibir a mensagem: Não foram realizadas movientações.

#Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo: 1500.45 = R$ 1500.45

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
# #Função depositar
def depositar(valor):
        global saldo
        global limite
        global LIMITE_SAQUES
        global numero_saques
        global extrato
        if valor > 0:
           saldo += valor
           extrato += f"Depósito: R$ {valor:.2f}\n"
           print(f"Deposito {valor:.2f} realizado com sucesso...\n")
        else:
          print(f"Operação falhou! O Valor informado é inválido")
#Função sacar
def sacar(valor):

    global saldo
    global limite
    global LIMITE_SAQUES
    global numero_saques
    global extrato

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques > LIMITE_SAQUES

    if excedeu_saldo:
        print(f"Operação Falhou! Saldo insuficiente: R${saldo:.2f}")
    elif excedeu_limite:
        print(f"Operação Falhou!! O valor do saque excede o limite de R$ {limite:.2f} ")
    elif excedeu_saques:
        print(f"Operação Falhou!! O número maximo de {LIMITE_SAQUES} excedeu")
    elif valor > 0:
        saldo -= valor
        extrato =  extrato + f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informando é inválido")

#Fução extrato
def mostrar_extrato():
     global saldo
     global extrato
     print("\n================ EXTRATO ================")
     print("Não foram realizadas movimentações." if not extrato else extrato)
     print(f"\nSaldo: R$ {saldo:.2f}")
     print("==========================================")




while True:

    opcao = input(menu)
    #depositar
    if opcao == "d":
        valor = float(input("Informe o valor do deposito:"))
        depositar(valor)
    #sacar
    elif opcao == "s":
        valor = float(input("Informe o valor do saque:\n"))
        sacar(valor)
    #extrato
    elif opcao == "e":
         mostrar_extrato()
    elif opcao == "q":
         print(f"Atendimento finalizado. Obrigado por utilizar nosso sistema")
         break
    #opcao invalida
    else:
        print("Operação inválida, por favor selecione novamente a opração desejada.")
        
        
