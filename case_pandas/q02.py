# 2. Podemos deixar a de Catupiry como borda padrão?

# %%

import pandas as pd

# Importando os dados e visualizando
df_item_pedido = pd.read_csv("../data/item_pedido.csv")
df_item_pedido

# %%

# Criando filtro

filtro_borda = df_item_pedido["descTipoItem"]  == "borda"
df_borda = df_item_pedido[filtro_borda]
df_borda

# %%

# Agrupando os dados

df_group_borda = (df_borda.groupby(["descItem"])["idPedido"]
            .nunique()
            .reset_index())
df_group_borda

# %%

# Verificando o percentual de representatividade de pedidos

df_group_borda["RepPedidos (%)"] = (df_group_borda["idPedido"] / df_group_borda["idPedido"].sum()) * 100
df_group_borda

# %%

# Não é possivel fazer a de catupiry ser de borda padrão, os percentuais de representatividade das mesmas são semelhantes.