'''
Crie um aplcativo que solicita o salário bruto de um funcionário. 
O app deverá descontar 11% de INSS e 7.5% deFGTS. 
Como saída o app deve mostrar o valor do salário líquido e o valor dos descontos.
'''
salario = input("Por favor, digite seu salário bruto: ")

inss = int(salario) * (11 / 100)
fgts = int(salario) * (7.5 / 100)
total = int(salario) - inss - fgts

print("Seu salário líquido é igual à: ", total)
print("Desconto INSS: ", inss)
print("Desconto FGTS: ", fgts)