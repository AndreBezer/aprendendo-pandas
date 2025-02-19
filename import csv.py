import pandas as pd

# Importando planilha com valores separados por virgula (CSV)
df = pd.read_csv("primeiropandas/planilha.csv")

print(df)
#         Nome   Idade Sexo
#    0    lucas      20    M
#    1    andre      20    m
#    2    pedro    2398    m
#    3   algust  914281    m
#    4  pareira     814    m


# Como Adicionar valores a um arquivo .csv:
# Faça o input dos valores
nome = str(input("Digite seu nome: "))
idade = str(input("Digite sua idade: "))
sexo = str(input("Digite seu sexo [M/F]: "))

# Crie um Dicionario com estes valores
nova_linha = {
    "Nome": nome,
    "Idade": idade,
    "Sexo": sexo
}

# Transforme o Dicionario em um DataFrame
nova_linha_df = pd.DataFrame([nova_linha])

# Faça a concatenação entre os DataFrame
df = pd.concat([df, nova_linha_df], ignore_index=True)

print(df)

# Salve o aquivo
df.to_csv("primeiropandas/planilha_nova.csv", index=False)