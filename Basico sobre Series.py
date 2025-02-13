import pandas as pd

# Criação da Serie ( Matriz unidirecional - Coluna )
a = [1, 2, 3, 4]

# Transforma a Serie em uma variavel
varseries = pd.Series(a)

# Print da Serie
print(varseries)

# Saida:
#
#   indice  Valor
#        0   1
#        1   2
#        2   3
#        3   4

# É impresso na tela o valor cujo indice é igual a 2
print(varseries[2])

# NOMEAR O INDEX DA SERIES:
# Criação de uma Series
a = ["andre", "lucas", "pedro"]

# transformação da series em variavel
# o index[0] recebe o nome aluno1...
varseries = pd.Series(a, index=["aluno1", "aluno2", "aluno3"])

# o valor cujo indice é igual a "aluno1" é impresso na tela
print(varseries["aluno1"])
