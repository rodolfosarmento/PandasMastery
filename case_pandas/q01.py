# 1. Podemos remover algum tipo de massa do cardápio? 
# Qual o impacto dessa ação?

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

# Filtrando as massas

filtro_masaa = df_item_pedido["descTipoItem"] == "massa"

df_massa = (df_item_pedido[filtro_masaa]
            .merge(df_produto, # Merge para aquisição dos valaores de preços
                   how="left"))

df_massa

# %%

# Agrupando os valores pela descrição do item

df_group = (df_massa.groupby(by=["descItem"])
            .agg({"idPedido":["nunique"], # Contagem dos números de pedidos das massas
                   "vlPreco" :["sum"]})
            .reset_index())

# %%

# Somando os valores de receita de pedidos realizados

df_group.columns = df_group.columns.get_level_values(0)
df_group

# %%

# Verificando os percentuais

df_group["RepQuant (%)"] = (df_group["idPedido"] / df_group["idPedido"].sum()) * 100 # Percentual de representatividade dos pedidos
df_group["RepReceita (%)"] = (df_group["vlPreco"] / df_group["vlPreco"].sum()) * 100 # Percentual de representatividade dos valores
df_group

# %%

# Resposta: Uma boa prática seria a remoção das massas do tipo integral, as mesmas apresentam baixa representatividade na quantidade de pedidos e na aquisição de receita.
