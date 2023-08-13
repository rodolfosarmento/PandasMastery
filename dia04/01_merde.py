# %%

import pandas as pd

# %%

# Importando as Databases

df_item_pedido = pd.read_csv("../data/item_pedido.csv")

df_produto = pd.read_csv("../data/produto.csv")

df_pedido = pd.read_csv("../data/pedido.csv")

# %%

# Maneira 1

# Trazendo o preço dos itens através do comando Merge
df_join = df_item_pedido.merge(df_produto,
                     how="left",
                     on="descItem")

df_join.merge(df_pedido,
              how="left")


# %%

# Maneira 2

# Trazendo o preço dos itens através do comando Merge

df_join = (df_item_pedido.merge(right = df_produto, how= "left")
                         .merge(right = df_pedido, how= "left"))