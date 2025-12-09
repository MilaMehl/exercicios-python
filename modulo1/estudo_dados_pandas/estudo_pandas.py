#importar a biblioteca 
import pandas as pd
#criando um data frame
# dados = {
#     'nome': ['Ana', 'Bruno', 'Carlos', 'Diana'],
#     'idade': [23, 35, 45, 29],
#     'cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba']
# }
df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

# raio x da tabela
# df.head()      # mostra as 5 primeiras linhas
# df.tail()      # mostra as 5 últimas linhas
# df.shape       # mostra quantas linhas e colunas existem
# df.info()      # mostra o que tem dentro (tipos e se tem valores faltando)
# df.describe()  # faz estatísticas rápidas (média, min, max...)
# #olhando só uma coluna
# df['nome']  # mostra a coluna 'nome', se colocar , e outra coluna, mostra as duas
# df[['nome', 'idade']]  # mostra as colunas 'nome' e 'idade'
# #olhando só uma linha
# df.loc[0]  # mostra a primeira linha
# df.loc[0:2]  # mostra as linhas de 0 a 2 (inclusive)
# #filtrando dados
# df[df['idade'] > 30]  # mostra linhas onde a idade é maior que 30
# print(pd.__version__)  # mostra a versão do pandas
# #ver so quem tem mais de 30 anos
# df[df['idade'] > 30].head()
# df[df['Idade'] > 20]
# df[df['Cidade'] == 'SP'] # qm é so de SP
# df[(df['Idade'] > 20) & (df['Cidade'] == 'SP')] # quem tem mais de 20 anos e é de SP
# #adicionando uma nova coluna
# df['salario'] = [3000, 4500, 5000, 4000]  # adiciona a coluna 'salario'
# #ordenando os dados
# df.sort_values(by='idade', ascending=False)  # ordena por idade, do maior para o menor
# #saber a idade média
# idade_media = df['idade'].mean()  # calcula a média das idades
# #idade maxima
# idade_maxima = df['idade'].max()
# #quantidade de pessoas por cidade
# quantidade_por_cidade = df['cidade'].value_counts()
# #somar e fazer media por grupos, como a idade media por cidade
# idade_media_por_cidade = df.groupby('cidade')['idade'].mean()
# #limpando dados
# df.isna().sum()        # vê se tem valores vazios
# df.fillna(0)           # preenche valores vazios com zero
# df.drop_duplicates()   # remove linhas repetidas
# #salvando o DataFrame em um arquivo CSV
# df.to_csv('dados.csv', index=False)

linhas, colunas = df.shape[0], df.shape[1]
#print(f'linhas: {linhas} e colunas: {colunas}')
novos_nomes = {      #esse é tipo um dicionario com os novos nomes 
    'work_year': 'ano',
    'experience_level': 'experiencia',
    'employment_type': 'emprego',
    'job_title': 'cargo',
    'salary': 'salario',
    'salary_currency': 'moeda',
    'salary_in_usd': 'usd',
    'employee_residence': 'residencia',
    'remote_ratio': 'remoto',
    'company_location': 'empresa',
    'company_size': 'tamanho_empresa'
}
df.rename(columns = novos_nomes, inplace = True)
df.head()
df['remoto'].value_counts() # mostra a quantidade de pessoas que trabalham remoto
#print(df['remoto'].value_counts())
remoto = {
    0 : 'presencial',
    50 : 'hibrido',
    100 : 'remoto'   #nos nº nao vai aspas pq são strings, se fosse texto teria que ter as aspas pq sao int
}
df['remoto'] = df['remoto'].replace(remoto)  # substitui os valores da coluna 'remoto'
df['remoto'].value_counts()  # mostra a quantidade de pessoas que trabalham remoto
#print(df['remoto'].value_counts())
#renomeando os niveis de experiencia
experiencia = {
    'EN': 'Estagiário',
    'EX': 'Executivo',
    'MI': 'Pleno',
    'SE': 'Sênior'
}
df['experiencia'] = df['experiencia'].replace(experiencia)
df['experiencia'].value_counts()
#renomeando os tipos de emprego
emprego = {
    'PT': 'Parcial',
    'FT': 'Integral',
    'CT': 'Contrato',
    'FL': 'Freelancer'
}
df['emprego'] = df['emprego'].replace(emprego)
df['emprego'].value_counts()
#renomeando os tamanhos de empresa
tamanho_empresa = {
    'S': 'Pequena',
    'M': 'Média',
    'L': 'Grande'
}
df['tamanho_empresa'] = df['tamanho_empresa'].replace(tamanho_empresa)
df['tamanho_empresa'].value_counts()
#renomeando o cargo
df['cargo'].value_counts()
#agrupando cargos semelhantes
df['cargo'] = df['cargo'].replace({
    'Data Scientist': 'Cientista de Dados',
    'Data Engineer': 'Engenheiro de Dados',
    'Data Analyst': 'Analista de Dados',
    'Machine Learning Engineer': 'Engenheiro de Machine Learning',
    'Research Scientist': 'Cientista de Pesquisa',
    'Big Data Engineer': 'Engenheiro de Big Data',
    'Data Science Manager': 'Gerente de Ciência de Dados',
    'AI Scientist': 'Cientista de IA',
    'Data Architect': 'Arquiteto de Dados',
    'Business Intelligence Developer': 'Desenvolvedor de BI'
})
df['cargo'].value_counts()
#print(df.head())
df.to_csv('salarios.csv', index = False)  #salva o arquivo com os novos nomes
#verificar os valores que são nulos
#print(df.isna().sum())#aqui ele mostra quantos valores nulos somados(.sum) tem em cada coluna
#
df['ano'].unique()  #mostra os anos que tem no dataset
#print(df['ano'].unique()) #no terminal ele mostrou um valor "nan" que é um valor nulo, ou seja, não tem valor (em ingles "not a number")
#trazer tudo que é nulo da base de dados
df[df.isnull().any(axis=1)]  #mostra todas as linhas que tem valores nulos
#print(df[df.isnull().any(axis=1)])  #mostra todas as linhas que tem valores nulos
#outra forma de ver os nulos
df[df.isna().any(axis=1)]  #mostra todas as linhas que tem valores nulos

#criando um grafico 
df['experiencia'].value_counts().plot(kind='bar')  
print(df['experiencia'].value_counts())  #mostra a quantidade de pessoas por nível de experiência
#parei em 9 min aula 3