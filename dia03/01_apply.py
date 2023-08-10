# %%

import pandas as pd

# %%

df_produto = pd.read_csv("../data/produto.csv")
df_produto

# %%

df_produto["descItem"].unique()

# %%

# Criação de um filtro para massas com apply, lower e startswith - Maneira 01

def is_massa(x):
    return x.lower() .startswith("massa") # o lower ajuda em deixar todo texto em caixa baixa

df_produto["flMassa"] = df_produto["descItem"].apply(is_massa)

df_produto[df_produto["flMassa"]]

# %%


# Usando função lambda dará o mesmo resultado  - Maneira 02

df_produto["flMassa"] = df_produto[df_produto["descItem"].apply(lambda x: x.lower() .startswith("massa"))]
df_produto[df_produto["flMassa"]]
# %%

# Usando a função str - Maneira 03

df_produto["flMassa"] = df_produto["descItem"].str.lower() .str.startswith("massa")
df_produto[df_produto["flMassa"]]
# %%
