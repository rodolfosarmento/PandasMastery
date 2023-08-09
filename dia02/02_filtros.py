# %%

import pandas as pd

# %%

df = pd.read_csv("../data/pedido.csv")
df

# %%

# Filtro pedidos de são paulo

filtro_UF = df["descUF"]=="São Paulo" 
df[filtro_UF]

# %%

# Filtro de são paulo e que pediram Ketchup

filtro_sp_ketchup = (df["descUF"]=="São Paulo") & (df["flKetchup"])
df[filtro_sp_ketchup]

# %%

# Filtro de São Paulo, Paraná e Rio de Janeiro que pediram ketchup (Maneira 01)

filtro_ufs_ketchup = ((df["descUF"]=="São Paulo") | (df["descUF"]=="Rio de Janeiro") | (df["descUF"]=="Paraná")) & (df["flKetchup"])
df[filtro_ufs_ketchup]

# %%

# Filtro de São Paulo, Paraná e Rio de Janeiro que pediram ketchup (Maneira 02 usando isin)

ufs =["São Paulo", "Rio de Janeiro", "Paraná"]
filtro_ufs_ketchup = df["descUF"].isin(ufs) & df["flKetchup"]
df[filtro_ufs_ketchup]

# %%

# Filtro de quem não deixou recado (Usando isna)

filtro_txt_na = df["txtRecado"].isna()
df[filtro_txt_na]

# %%
