'''1) Considere uma planilha do Excel chamada "estudantes.xlsx". Importe a biblioteca pandas e leia a planilha para um DataFrame chamado "tabela".'''
import pandas as pd
tabela = pd.read_excel("aula10\\alunos.xlsx", sheet_name="alunos")

print("---------------------------------------------------------------------------------")

'''2) Crie o código para exibir os 5 primeiros registros do DataFrame.'''
print(tabela.head(5))

print("---------------------------------------------------------------------------------")

'''3) Crie o código para Inserir um novo aluno no DataFrame com os seguintes dados:
● RA: 0005
● Nome: Enzo Moreira
● Curso: Técnico em Jogos
● Turma: 1GMA'''
tabela.loc[len(tabela)] = [8, "Enzo Moreira", "Técnico em Jogos", "1GMA"]
print(tabela)

print("---------------------------------------------------------------------------------")

'''4) Crie o código para atualizar os dados do estudante Enzo Moreira para:
● Curso: Técnico em Informática
● Turma: 3TE'''
tabela.loc[tabela['Nome'] == 'Enzo Moreira'] = [8, "Enzo Moreira", "Técnico em Informática", "1TI"]
print(tabela)

print("---------------------------------------------------------------------------------")

'''5) Crie o código para excluir o estudante que está na linha de índice 1 do DataFrame.'''
tabela.drop(1, inplace=True)
print(tabela)

print("---------------------------------------------------------------------------------")

'''6) Exportar o DataFrame atualizado para uma nova planilha do Excel.'''
tabela.to_excel('nova_planilha.xlsx', index=False)

'''7) Exibir apenas os alunos matriculados no curso "Técnico em Informática".'''
tabela.loc[tabela['Curso'] == 'Técnico em Informática']
print(tabela)