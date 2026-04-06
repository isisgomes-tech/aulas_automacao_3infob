'''
Crie um script que usa a função "quadrado" criada no arquivo exercicio_f1.py. 
Esse script deve pedir para o usuário digitar um número, depois deve calcular 
o quadrado usando a função e depois imprimir o resultado.
'''
from exercicio_f1 import quadrado

numero = int(input('Digite um número: '))
valor = quadrado(numero)
print(f"O quadrado de {numero} e {quadrado}")