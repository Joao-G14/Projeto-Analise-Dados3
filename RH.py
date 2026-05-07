import pandas as pd
import numpy as np

df = pd.read_csv('BaseFuncionarios.xlsx - Plan1.csv')

df['Data de Contratacao'] = pd.to_datetime(df['Data de Contratacao'])
df['Salario'] = df['Salario'].fillna(0)

total_funcionarios = len(df)
folha_salarial_total = df['Salario'].sum()
media_avaliacao = df['Avaliação do Funcionário'].mean()
total_horas_extras = df['Horas Extras'].sum()

funcionarios_por_area = df.groupby('Área')['ID RH'].count().sort_values(ascending=False)
salario_por_cargo = df.groupby('Cargo')['Salario'].mean().sort_values(ascending=False)

distribuicao_genero = df['Genero'].value_counts(normalize=True) * 100

print(f"Total de Funcionários: {total_funcionarios}")
print(f"Custo Total Mensal (Salários): R$ {folha_salarial_total:,.2f}")
print(f"Média de Avaliação Interna: {media_avaliacao:.2f}")
print("\nFuncionários por Área:")
print(funcionarios_por_area)