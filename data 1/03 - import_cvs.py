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

tipo_colunas = df.dtypes
tipo_colunas

# %%

df

# %%

df.head(20)

# %%

df.tail(5)