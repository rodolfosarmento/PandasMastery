# %%

import pandas as pd

# %%

df_produto = pd.read_csv("../data/produto.csv")
df_produto

# %%

# Separação de item por espaços (fins didáticos)
df_produto["primeiroNome"] = df_produto["descItem"].apply(lambda x: x.lower().split(" ")[0])
df_produto
# %%

# Ordenação dos valores

df_produto = df_produto.sort_values(
    by=["vlPreco", "descItem"],
    ascending=[False, True]
)

df_produto

# %%

# Removendo duplicatas dentro do dataframe

df_produto.drop_duplicates(subset=["primeiroNome", "vlPreco"], keep="first")

# %%

# Usando o comando dropna + how = "any", se pelo menos uma coluna for vazia a linha é excluída
# Usando o comando dropna + how = "all", se todas as colunas forem vazias a linha é excluída

df_produto = pd.read_csv("../data/pedido.csv")
df_produto.dropna(subset=["txtRecado", "flKetchup"],how="any")

# %%

