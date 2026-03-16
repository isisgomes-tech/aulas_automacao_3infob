#Condição IF

#Entrada
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

#Processamento 
if (idade < 18):
    autorizacao = input("Os pais autorizaram a viagem? (Sim/Não)")


print(f"Realizando o Embarque de {nome}")