# %%

import pandas as pd

df = pd.read_csv("../data/pedido.csv")


# %%

df.columns

# %%

df.shape

# %%

df.index

# %%

df.info(memory_usage="deep")

# %%

tipo_colunas = df.dtypes # Mostra os tipos de objetos
tipo_colunas

# %%

df

# %%

df.head(20) # Primeiras 20 linhas

# %%

df.tail(5) # ùltimas 5 linhas