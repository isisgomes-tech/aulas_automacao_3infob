"""
Função
"""
#def = define
def somar(n1, n2):
    return n1 + n2

def imprimir(texto):
    print(texto)

def pulaLinha():
    print('\n')

def ler():
    return int

imprimir("Digite o primeiro número: ")
n1 = ler()

imprimir("Digite o segundo número: ")
n2 = ler()

resposta = somar(n1, n2)

imprimir(f"O resultado é: {resposta}")