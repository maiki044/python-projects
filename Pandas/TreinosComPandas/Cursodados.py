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

