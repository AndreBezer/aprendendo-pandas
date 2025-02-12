import pandas as pd

# Criação de um dataset
dataset = {
    "carros": ["BMW", "Volvo", "Toyota"],
    "placa": [1, 3, 7]
}

# Transformação do dataset para uma variavel
info = pd.DataFrame(dataset)

# Impressão da variavel
print(info)