from funcao import imprimir,ler,pulaLinha,somar

#Usando as funções
imprimir("Digite o primeiro número: ")
n1 = ler()
pulaLinha()

imprimir("Digite o segundo número: ")
n2 = ler()

resposta = somar(n1, n2)

imprimir(f"O resultado é: {resposta}")