#criando uma base nova e vamos preencher os valores nulos com a media do salario
import numpy as np
import pandas as pd

df_salarios = pd.DataFrame({
    "nome": ['João', 'Maria', 'Pedro', 'Ana'],
    'salario': [4000, np.nan, 5000, np.nan]
})

df_salarios['salario_media'] = df_salarios['salario'].fillna(df_salarios['salario'].mean().round(2))  # preenche os valores nulos com a média do salário, arredondado para 2 casas decimais
print(df_salarios)
#se trocar o mean e roud para median, ele vai pegar a mediana dos valores

#preencher com valores fixos
df_salarios['salario_media'] = df_salarios['salario'].fillna(3000)