# 3. Vários queijos estão estragando pela validade. Quais queijos juntos atendem 90% dos pedidos?

# %%

import pandas as pd

df_item_pedido = pd.read_csv("../data/item_pedido.csv")
df_item_pedido

# %%

# Criando filtro dos queijos

filtro_queijo = df_item_pedido["descTipoItem"].isin(["queijo 1", "queijo 2"])
df_queijo = df_item_pedido[filtro_queijo]
df_queijo

# %%

# Agrupando os valores

df_group_queijo = (df_queijo.groupby(["descItem"])["idPedido"]
                   .nunique()   
                   .reset_index()
                   .sort_values("idPedido", ascending=False))
df_group_queijo 

# %%

# Percentuais de representatividade unica e acumulada

df_group_queijo["RepPedidos (%)"] = (df_group_queijo["idPedido"] / df_group_queijo["idPedido"].sum()) * 100
df_group_queijo["RepPedidosAcum (%)"] = df_group_queijo["RepPedidos (%)"].cumsum()
df_group_queijo

# Resposta: os queijos mussarela, parmesçao, catupiry, gorgonzola, provolone e cheddar. 