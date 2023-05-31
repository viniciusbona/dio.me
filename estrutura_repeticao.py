texto = input("informe um texto: ")
VOGAIS= "AEIOU"


# exemplo utilizando um iteravel
for letra in  texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")


else:
    print() # adiciona uma quebra de linha
    print("Executa no final do laço")

# exemplo utilizando a função built-in range
for numero in range(0, 555555, 5):
    print(numero)