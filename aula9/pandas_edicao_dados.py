#Pandas: Biblioteca em Python que permite a manipulação de arquivos em formato tabular. Ex.: Planilhas e Tabelas.

#Edição de Dados (Ler, Inserir, Atualizar e Excluir)

#Instalação: pip install pandas

#Importar biblioteca (as renomeia o pacote "abreviação")
import pandas as pd

#Ler uma planilha do Excel. Cria a variável planilha que vai guardar a planilha do Excel. Em pandas, chamamos a planilha de DataFrame
planilha = pd.read_excel("aula9\\Dados_3INFOB.xlsx")

#Imprime todos os dados da Planilha
#print(planilha)

#Imprime a cabeça da planilha: Quantas linhas da parte de cima desejado
#print(planilha.head(3))

#Imprime a cauda da planilha: Quantas linhas da parte de baixo desejado
#print(planilha.tail(3))

#Imprime o corpo da planilha: Quantas linhas da parte do meio desejado
nova = (planilha.head(4))
print(nova.tail(2))

#Imprime a quantidade de linhas na Planilha
print(len(planilha))

#Inserir um novo registro na Planilha
planilha.loc[len(planilha)] = ['Pablo', 52, 1.8, 'M']
print(planilha)

#Atualizar um registro, todas as colunas
#planilha.loc[linha] = ['Pablo', 52, 1.8, 'Masculino']
planilha.loc[16] = ['Pablo', 52, 1.8, 'Masculino']
print(planilha)

#Atualizar um registro, apenas uma coluna
#planilha.loc[linha, 'coluna'] = ['Pablo', 52, 1.8, 'Masculino']
planilha.loc[16, 'Nome'] = 'Pablo Sandi'
print(planilha)

#Atualizar um registro, duas ou mais colunas
#planilha.loc[linha, ['coluna', 'coluna']] = [x, x]
planilha.loc[16, ['Peso', 'Altura']] = [53, 1.81]
print(planilha)

#Remover um registro da planilha
planilha = planilha.drop(13)
#ou
planilha.drop(13, inplace=True)