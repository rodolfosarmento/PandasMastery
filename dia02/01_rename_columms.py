# %%

import pandas as pd

# %%

df = pd.read_csv("../data/pedido.csv")
df

# %%

# Maneira 1  - Retorna um resultado (Mais usado)
df.rename(columns={"descUF":"decEstado"})

# %%

# Maneira 2  - Altera o próprio DataFrame
df.rename(columns={"descUF":"decEstado"},inplace=True)


