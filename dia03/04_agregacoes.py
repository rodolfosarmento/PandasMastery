# %%

import pandas as pd

# %%

df_produto = pd.read_csv("../data/produto.csv")
df_produto

# %%

df_produto["vlPreco"].describe()

# %%

# Inserindo a coluna de valor inflado

df_produto["vlPrecoInfaco"] = (df_produto["vlPreco"] * 1.09).round(2)
df_produto.describe()

# %%

# Separação de item por espaços para criação de um nova coluna, e comparação com a original usando describe

df_produto["descItemPrimeiro"] = df_produto["descItem"].apply(lambda x: x.lower().split(" ")[0])
df_produto[["descItem","descItemPrimeiro"]].describe()

# %%

# Realizando uma tabela de frequência 

freq_iten = pd.value_counts(df_produto["descItemPrimeiro"])
freq_iten

# %%

# Realizando agrupando de valores com base escItemPrimeiro e calculando a média dos valores dos preços

df_produto.groupby(by=["descItemPrimeiro"])[["vlPreco","vlPrecoInfaco"]].mean()

# %%

# Realizando agrupando de valores com base escItemPrimeiro e exibindo a descrição das métricas

df_produto.groupby(by=["descItemPrimeiro"])[["vlPreco","vlPrecoInfaco"]].describe()

# %%

# Realizando agrupando de valores com base escItemPrimeiro e exibindo somente as métricas desejadas

df_produto.groupby(by=["descItemPrimeiro"])[["vlPreco","vlPrecoInfaco"]].agg(["min", "mean", "max"])

# %%
