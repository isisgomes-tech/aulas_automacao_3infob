import pandas as pd
ca = 'notas_estudantes.xlsx'

print("---------------------------------------------------------------")
print("1")

'''1. Leitura de Dados
Carregue o arquivo Excel chamado notas_estudantes.xlsx da seguinte forma:
- Armazene os dados da aba "Notas" em um DataFrame chamado df_notas.
- Armazene os dados da aba "Atividades" em um DataFrame chamado df_atividades.'''
df_notas = pd.read_excel(ca, sheet_name="Notas")
df_atividades = pd.read_excel(ca, sheet_name="Atividades")


print("---------------------------------------------------------------")
print("2")

'''2. Inserção de Registro
- Adicione um novo registro ao DataFrame df_notas com os seguintes dados:
Nome: 'Lucas Silva'
Atividade: 'Prova Final'
Nota: 8.5'''

print("---------------------------------------------------------------")
print("3")

'''3. Atualização de Dados
No DataFrame df_notas, atualize para 9.0 a nota da atividade 'Trabalho 1' da estudante 'Ana Souza'.'''

print("---------------------------------------------------------------")
print("4")

'''4. Exclusão de Registro
Exclua de df_notas o registro do estudante 'Pedro Santos' referente à atividade 'Prova 1'.'''

print("---------------------------------------------------------------")
print("5")

'''5. Filtragem Simples
Selecione todos os registros de df_notas em que a nota seja maior que 7.0.'''

print("---------------------------------------------------------------")
print("6")

'''6. Agrupamento e Agregação
Agrupe os dados de df_notas pelo nome dos estudantes e calcule a média das notas de cada um deles.'''

print("---------------------------------------------------------------")
print("7")

'''7. Projeção de Colunas
Selecione e exiba apenas as colunas 'Nome' e 'Nota' do DataFrame df_notas.'''

print("---------------------------------------------------------------")
print("8")

'''8. Filtragem por Texto
Selecione todos os registros do DataFrame df_notas em que a atividade seja exatamente 'Prova Final'.'''

print("---------------------------------------------------------------")
print("9")

'''9. Filtragem Composta e Projeção
Selecione apenas as colunas 'Nome' e 'Atividade' dos estudantes que obtiveram nota maior que 7.0.'''

print("---------------------------------------------------------------")
print("10")

'''10. Ordenação
Ordene o DataFrame df_notas pelo nome dos estudantes em ordem alfabética (A-Z).'''

print("---------------------------------------------------------------")
print("11")

'''11. Junção de DataFrames (Merge)
Combine os dados dos dois DataFrames (df_notas e df_atividades) utilizando a atividade como chave de ligação. 
O resultado deve exibir, para cada linha de nota, o valor total da atividade e o assunto abordado nela.'''

print("---------------------------------------------------------------")
print("12")

'''12. Exportação de Dados
Salve o DataFrame que foi ordenado na Questão 10 em um novo arquivo Excel chamado notas_estudantes_ordenado.xlsx, 
sem incluir o índice no arquivo final.'''

print("---------------------------------------------------------------")