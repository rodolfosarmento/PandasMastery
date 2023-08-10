# %%

import pandas as pd

# %%

df_produto = pd.read_csv("../data/produto.csv")
df_produto

# %%

# Ordenação de valores
df_produto.sort_values(by="vlPreco", ascending=False)

# %%

# Ordenação de valores com mais de um critério
df_produto.sort_values(by=["vlPreco", "descItem"], ascending=[False, True])

