# 4. Quais ingredientes podemos remover do cardápio para diminuir custo no estoque?

# %%

import pandas as pd

# %%

# Importando e visualizando os itens

df_item_pedido = pd.read_csv("../data/item_pedido.csv")
df_item_pedido

# %%

df_produto = pd.read_csv("../data/produto.csv")
df_produto

# %%

# Filtro de ingredientes

filtro_ingredientes = df_item_pedido["descTipoItem"].apply(lambda x: x.lower() .startswith("ingrediente"))

# %%

# Unindo com merge os dois dataframes

df_ingredientes = df_item_pedido[filtro_ingredientes].merge(df_produto, how="left")
df_ingredientes

# %%

# Agrupando os valores por tipo e composição em casa ingredientes

df_group_ingredientes = (df_ingredientes.groupby("descTipoItem")
                         .agg({"idPedido":["nunique"],
                               "vlPreco" :["sum"]})
                         .reset_index()
                         )
df_group_ingredientes.columns = df_group_ingredientes.columns.get_level_values(0)
df_group_ingredientes

# %%

# Alterando nome da coluna

df_group_ingredientes.rename(columns={"vlPreco":"Custo"}, inplace = True)
df_group_ingredientes

# %%

# Calculando o produto de custo total  

df_group_ingredientes["RepPedidos (%)"] = (df_group_ingredientes["Custo"] / df_group_ingredientes["Custo"].sum()) * 100
df_group_ingredientes["RepPedidosAcum (%)"] = df_group_ingredientes["RepPedidos (%)"].cumsum()
df_group_ingredientes 
           
# %%

# Exportando em arquivo csv
 
df_group_ingredientes.to_csv("analise_ingredientes_custo.csv", sep=";", index=False, encoding= "utf8")

# %%

# Resposta: O itens pertecentes a categoria de ingredientes 05 podem ser passiveis de remoção.