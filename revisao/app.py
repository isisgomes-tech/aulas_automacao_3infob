# 1) Importar a biblioteca do pandas                                               #serie = coluna         #linha = registro
import pandas as pd          

# 2) Carregar uma planilha do Excel
df = pd.read_excel('revisao/CopiaDeRevisao2_220626.xlsx')
#dataframe
print(df.head())                                              #head = parte de cima / dentro dos parênteses, colocar o número desejado de linhas
print(df.tail())                                              #tail = parte de baixo / dentro dos parênteses, colocar o número desejado de linhas

# 3) Compreender o funcionamento do LOC
print(df.loc[0]) #Imprime a primeira linha - [linha]
print(df.loc[0, "Nome"]) #Imprime a primeira linha da coluna "Nome" - [linha, coluna]
print(df.loc[4 : 6]) #Seleciona o intervalo de linhas dentre os números 4 e 6
print(df.loc[4 : 6, "Nome"]) #Seleciona o intervalo de linhas dentre os números 4 e 6, apenas da coluna "Nome"
print(df.loc[4 : 6, ["Nome", "Idade"]]) #Seleciona o intervalo de linhas dentre os números 4 e 6, apenas das colunas "Nome" e "Idade".
print(df.loc[ : , "Nome"]) #Localizar em uma coluna, todas as linhas
#print(df.loc[[True, False, False, True], ["Nome", "Sexo"]])

df2 = df.loc[3 : 6, ["Nome", "Sexo"]]
print(df2)

# 4) Inserir novos dados da planilha
df.loc[30] = ["Ísis Gomes", "Feminino", 18, "Técnico em Informática", "Automação", 10]
print(df)

# 5) Atualizar dados na planilha
df.loc[30, ["Curso", "Disciplina"]] = ["Artes", "Teatro"]
print(df)

# 6) Filtrar dados
condicao1 = df["Idade"] == 20
condicao2 = df["Sexo"] == 'Feminino' 
print(condicao1)                                #Printa "True" or "False"
print(df.loc[condicao1])                        #Printa apenas os verdadeiros (que se encaixam na condição)
print(df.loc[condicao1 & condicao2, "Nome"])    #Printa os nomes apenas dos verdadeiros (que se encaixam na condição)

# 7) Classificar dados
tabela_ordenada = df.sort_values("Nome", ascending = False)          #ascending = crescente
print(tabela_ordenada)

# 8) Contar dados
tabela_contagem = df.value_counts("Curso")
print(tabela_contagem)

# 9) Agrupar dados
tabela_agrupada = df.groupby("Sexo")["Sexo"].count()                      #count = contar / sum = somar / mean = média
print(tabela_agrupada)

# 10) Exportar dados
df.to_excel("revisao\\nova_planilha.xlsx")

