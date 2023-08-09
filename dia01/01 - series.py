# %%
import pandas as pd

# %%

# Isso é uma lista!!!!
idade = [31, 33, 2, 29, 60, 58, 31, 45, 24]
idade

# %%

# Isso é uma Série
S_idade = pd.Series(idade)
S_idade

# %%

# Métodos das Séries
medio = S_idade.mean()
variancia = S_idade.var()
desvio_pd = S_idade.std()
describe = S_idade.describe()
describe

# %%

filtro = S_idade >=30
S_idade[filtro]

# %%
