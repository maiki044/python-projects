import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")
print(df.head())
print(df.info())
print(df.describe())
print(df.shape)
linhas, colunas = df.shape[0], df.shape[1]
print(f"Linhas: {linhas}, Colunas: {colunas}")
print(df.columns)
renomear_colunas = {
    'work_year': 'ano',
    'experience_level': 'nivel_experiencia',
    'employment_type': 'tipo_contrato',
    'job_title': 'cargo',
    'salary': 'salario',
    'salary_currency': 'moeda_salario',
    'salary_in_usd': 'salario_em_usd',
    'employee_residence': 'residencia_funcionario',
    'remote_ratio': 'percentual_remoto',
    'company_location': 'local_empresa',
    'company_size': 'porte_empresa'
}
df.rename(columns=renomear_colunas, inplace=True)
print(df.columns)
print(df["nivel_experiencia"].value_counts())
print(df["porte_empresa"].value_counts())
substituir_senioridade = {
    'EN': 'Sênior',
    'MI': 'Médio',
    'SE': 'Júnior',
    'EX': 'Estágio'
}
print(df.head())
print(df.isnull().sum())
print(df['ano'].unique())
print(df[df.isnull().any(axis=1)])
df_limpo = df.dropna()
print(df_limpo.head())
print(df_limpo['nivel_experiencia'].value_counts().plot(kind='bar', title="Distribuição de nível de experiência"))
import seaborn as sns
sns.barplot(data=df_limpo, x='nivel_experiencia', y='salario_em_usd')
import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))
sns.barplot(data=df_limpo, x='senioridade', y='usd')
plt.title("Salário médio por senioridade")
plt.xlabel("Senioridade")
plt.ylabel("Salário médio anual (USD)")
plt.show()

df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=False)
ordem = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=True).index

plt.figure(figsize=(8,5))
sns.barplot(data=df_limpo, x='senioridade', y='usd', order=ordem)
plt.title("Salário médio por senioridade")
plt.xlabel("Senioridade")
plt.ylabel("Salário médio anual (USD)")
plt.show()

plt.figure(figsize=(10,5))
sns.histplot(df_limpo['usd'], bins = 50, kde=True)
plt.title("Distribuição dos salários anuais")
plt.xlabel("Salário em USD")
plt.ylabel("Frequência")
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(x=df_limpo['usd'])
plt.title("Boxplot Salário")
plt.xlabel("Salário em USD")
plt.show()

df_limpo.to_csv('dados-imersao-final.csv', index=False)
print(df_limpo.head())
