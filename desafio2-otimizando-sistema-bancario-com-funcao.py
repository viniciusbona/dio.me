#AUTOR: Vinicius Nunes de Bona
#DATA: 09/06/2023

"""
#DESAFIO:
Precisamos deixar nosso código mais modularizado, para isso, vamos criar funções para as operações existentes:
-sacar
- depositar
- visualizar histórico.

2 novas funções:
- criar usuários (cliente do banco)
- criar conta corrente (vincular com usuário)

Descrição das funções:

-> SAQUE:
    deverá receber os argumentos (keyword only). 
    Argumentos: 
    - saldo 
    - valor
    - extrato
    - limite
    - numero_sques,
    Retorno:
    - saldo
    - extrato
=-=-=--=-=--=-=-=--==-=-=-=-    
->DEPOSITO:
    deverá receber os argumentos apenas por posição (positional only).
    Argumentos:
    - saldo
    - valor
    - extrato
    Retorno:
    - saldo
    - extrato
=-=-=-=-=-=-=-=-=-=-=-=--==-    
->EXTRATO:
  deve receber os argumentos por posição e nome (positional only e keyword only).
  Argumentos Posicionais:
  - saldo
  Argumentos nomeados:
  - extrato

=-=-=-=-=-=-=--=-=-=-=-
->CRIAR_USUARIO(cliente):
  deve armazenar usuarios em uma lista
    =>o usuario é composto por:
    - nome
    - data de nascimento
    - cpf
    - endereço: string
        formato: logradouro, nro - bairro - cidade/sigla estado.(não é necessário validar formato)
    RESTRIÇÕES:
     - Não podemos cadastar 2 usuários com o mesmo CPF.
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
->CRIAR_CONTA CORRENTE
  o programa deve armazenar contas em uma lista.
  =>conta é composto por:
   - agencia: numero fixo: "0001"
   - numero da conta: numero sequencial iniciando em 1
   - usuario:
   RESTRIÇÃO:
    - O usuario pode ter mais de uma conta, mas uma conta pertence a somente um usuário.
=--=-=-=-==-=-=-=-=-=-==-=-=-==-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
<!>dica<!>
para vincualr um usuario a uma conta, filtre a lista d e usuaŕio buscando o número do cpf informado
para cada usuário da lista.

"""

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[c] Criar Usuario
[n] Criar Conta
[l] Listar Usuarios
[v] Listar contas
[q] Sair
=>"""



# #Função depositar
def depositar(saldo, valor, extrato, /):
        
        if valor > 0:
           saldo += valor
           extrato += f"Depósito: R$ {valor:.2f}\n"
           print(f"Deposito {valor:.2f} realizado com sucesso...\n")
           return saldo, extrato
        else:
          print(f"Operação falhou! O Valor informado é inválido")
#Função sacar

def sacar(*,saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):

   
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques > LIMITE_SAQUES

    if excedeu_saldo:
        print(f"Operação Falhou! Saldo insuficiente: R${saldo:.2f}")
        return saldo, extrato, numero_saques
    elif excedeu_limite:
        print(f"Operação Falhou!! O valor do saque excede o limite de R$ {limite:.2f} ")
        return saldo, extrato, numero_saques
    elif excedeu_saques:
        print(f"Operação Falhou!! O número maximo de {LIMITE_SAQUES} excedeu")
        return saldo, extrato, numero_saques
    elif valor > 0:
        saldo -= valor
        extrato =  extrato + f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        return saldo, extrato, numero_saques
    else:
        print("Operação falhou! O valor informando é inválido")
        return saldo, extrato, numero_saques

#Fução extrato
def mostrar_extrato(saldo, /, *, extrato):
     
     print("\n================ EXTRATO ================")
     print("Não foram realizadas movimentações." if not extrato else extrato)
     print(f"\nSaldo: R$ {saldo:.2f}")
     print("==========================================")
     return saldo, extrato

def cpf_existe(cpf, lista_usuario):
    for elemento in lista_usuario:
        if cpf == elemento['cpf']:
            print("true")
            return True
        else:
            print("falso")
            return False

def filtrar_usuario(cpf, lista_usuarios):
    usuario_filtrado = [usuario for usuario in lista_usuarios if usuario["cpf"] == cpf]
    return usuario_filtrado[0]['nome'] if usuario_filtrado else  None

def criar_usuario(lista_usuarios):
    usuario = {}
    cpf = input(f"Informe o CPF: ")


    if cpf_existe(cpf, lista_usuarios) == True:
        print(f"Falha ! CPF {cpf}, ja cadastrado\n")
        return lista_usuarios
    else:
        usuario['nome'] = input("Digite o nome do usuario: ")
        usuario['data_nascimento'] = input("Informe a Data de Nascimento: ")
        usuario['cpf'] = cpf
        usuario['endereco'] = input("informe o endereço: ")
        lista_usuarios.append(usuario)
        print(f"usuario \n {usuario} \n\n crido com sucesso\n")

        return lista_usuarios

def criar_conta_corrente(lista_contas, lista_usuarios, AGENCIA):
    conta = {}
    cpf = input("informe cpf do usuario")
    nome = filtrar_usuario(cpf, lista_usuarios)
    if nome == 'None':
      print(f"Falha !! usuario com cpf {cpf}, não encontrado")
      return lista_contas
    else:
      conta['agencia'] = AGENCIA
      conta['numero'] = len(lista_contas) + 1
      conta['usuario'] = nome
      lista_contas.append(conta)
      return lista_contas
    print(f'Conta corrente crida com sucesso: \n {conta} \n')
    
def main():
     saldo = 0
     limite = 500
     extrato = ""
     numero_saques = 0
     LIMITE_SAQUES = 3
     AGENCIA = "0001"
     lista_contas = []
     lista_usuarios = []
    while True:

        opcao = input(menu)
        #depositar
        if opcao == "d":
            valor = float(input("Informe o valor do deposito:"))
            saldo, extrato = depositar(saldo, valor, extrato)
            
        #sacar
        elif opcao == "s":
            valor = float(input("Informe o valor do saque:\n"))
            saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)
        #extrato
        elif opcao == "e":
            saldo, extrato = mostrar_extrato(saldo,  extrato=extrato)
        #criar usuario        
        elif opcao == "c":
             lista_usuarios = criar_usuario(lista_usuarios)
        #listar usuarios
        elif opcao == "l":
             print(lista_usuarios)
        #criar novos usuarios
        elif opcao == "n":
             lista_contas = criar_conta_corrente(lista_contas, lista_usuarios, AGENCIA)
        #lista contas criadas
        elif opcao == "v":
             print(lista_contas)
        #sair da aplicao
        elif opcao == "q":
            print(f"Atendimento finalizado. Obrigado por utilizar nosso sistema")
            break
        #opcao invalida
        else:
            print("Operação inválida, por favor selecione novamente a opração desejada.")


main()
        
