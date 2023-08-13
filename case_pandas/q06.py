#6. A preferência do tipo de massa muda entre os estados?
# E os ingredientes prediletos?

# %% 

import pandas as pd

df_item_pedido = pd.read_csv("../data/item_pedido.csv")
df_item_pedido

# %%

df_pedido = pd.read_csv("../data/pedido.csv")
df_pedido

# %%

# Filtrando as massas

filtro_massa = df_item_pedido["descTipoItem"] == "massa"

# %%

# Usando merge para conectar os estados com os pedidos

df_massa = df_item_pedido[filtro_massa].merge(df_pedido[["idPedido", "descUF"]], how="left")
df_massa

# %%

# Agrupando os valores e usando pivot_table e analisando

df_analise = (df_massa.groupby(["descItem", "descUF"])["idPedido"]
                        .nunique()
                        .reset_index()
                        .sort_values(["descUF", "descItem"])
                        .pivot_table(values="idPedido",columns="descItem",index = "descUF")
                        .reset_index()
                        .fillna(0)
    )
df_analise

# %%

# Salvando a análise

df_analise.to_csv("analise_massa_estado.csv", sep=";", index=False, encoding= "utf8")
