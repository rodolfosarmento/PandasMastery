# %%

# Importando o pandas
import pandas as pd

# %%

# Importando o sqlalchemy

import sqlalchemy 

# %%

# Criando um funação para facilitar as importações

def import_query(patch):
    with open(patch, "r") as open_file:
        query = open_file.read()
    return query

# Criando a conexão Engine

engine = sqlalchemy.create_engine("sqlite:///../data/database.db")

# %%

# Extraindo a informação com SQl (Desta forma o processamento não acontece na máquina local)

query_preco_maior_10 = "SELECT * FROM produto WHERE vlPreco > 10"

# Fazendo a leitura das infromações extraídas da Query

df_prod_10 = pd.read_sql_query(query_preco_maior_10, engine)
df_prod_10

# %%

# Importando a query feita em arquivo SQL

query_pedido_preco = import_query("pedido_item_preco.sql")
print(query_pedido_preco)

# %%

# Criando um DataFrame a partir de uma consulta Query

df_item_pedido = pd.read_sql_query(query_pedido_preco, engine)
df_item_pedido

# %%

query_uf_pedido = import_query("quantidade_pedidos_estado.sql")
print(query_uf_pedido)

# %%

# Criando um DataFrame a partir da segunda consulta query

df_pedido_estado = pd.read_sql_query(query_uf_pedido, engine)
df_pedido_estado

# %%

# Enviando resultados para o SQL

top_uf_5 = (df_pedido_estado.sort_values("qtdePedido", ascending=False)
            .head(5))
top_uf_5

# %%

top_uf_5.to_sql("top_uf_pedido", engine)