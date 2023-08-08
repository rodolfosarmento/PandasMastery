# %%

import pandas as pd

df = pd.read_csv("../data/pedido.csv")
df

# %%

# SELECT IdPedido, flKetchup from oedido

df[["idPedido","flKetchup"]]

# %%

# Movimentação entre as colunas com base em um filtro

colunas = [
    "idPedido",
    "descUF",
    "flKetchup",
    "txtRecado",
    "dtPedido"
    ]

df = df[colunas]
df

# %%

# Cria um dataframe novo com 100 dados do anterior

df_sample = df.sample(100)

# %%

# iloc trabalha com a posição

df_sample.iloc[0:4][["idPedido", "dtPedido"]]

# %%

# loc trabalha com o índice

df_sample.loc[[1064,837]]
# %%
