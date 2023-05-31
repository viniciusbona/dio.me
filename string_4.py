nome = "Vinicius"

mensagem = f'''
olá meu nome é {nome}, Eu estou aprendendo Python.
    Essa mensagem tem diferente recuos.
'''

print(mensagem)


print("""
    ============MERNU============
    1 - Depositar
    2 - Sacar
    0 - Sair
    ==============================
        Obrigado por usar nosos sitema!!!!!!!!!

""")


# #old style
# print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))

# #método format
# print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))
# print("Olá, me chamo {0}. Eu tenho {1} anos de idade, trabalho como {2} e estou matriculado no curso de {3}.".format(nome, idade, profissao, linguagem))

# print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

# #print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(**pessoa))


# print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")


# PI = 3.14159
# print(f"Valor de PI: {PI: .2f}")

# print(f"Valor de PI: {PI:10.2f}")
