import pandas as pd

# Criação do DataFrame
dataframe = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

# Conversão do DataFrame para variavel
df = pd.DataFrame(dataframe)

# Impressão da variavel
print(df)

# Para referenciar uma linha especifica usamos o atributo loc
#para retornar uma ou mais linhas
print(df.loc[0])
print(df.loc[[0, 1]]) # Caso precise especificar mais de uma linha
                      # Torna-se necessario o uso de []

df = pd.DataFrame(dataframe, index=["dia 1", "dia 2", "dia 3"])
print(df)