nome = "Guilherme Arthur de Carvalho"

print(nome[0])
print(nome[-1])
print(nome[:9])
print(nome[10:])
print(nome[10:10])
print(nome[10:10:2])
print(nome[:])
print(nome[:: -1])



name = "Vinicius"

mensagem = f'''
olá meu nome é {name}, Eu estou aprendendo Python.
    Essa mensagem tem diferente recuos.
'''

print(mensagem)


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
