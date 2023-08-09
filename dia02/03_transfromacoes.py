# %%

# Importando o pandas
import pandas as pd
import numpy as np

# %%

# Extraindo dados do arquivo CSV
df = pd.read_csv("../data/produto.csv")
df

# %%

# Mostra as informações dos dados
df.info()

# %%

# Ajustando preços e colocando com somente duas casas deciamis usando round
df["Preco_Ajustado"] = (df["vlPreco"]*1.09).round(2)
df

# %%

# Adiciona uma coluna que mostra a taxa de reajuste
df["txtAjustado(%)"] = (100*((df["Preco_Ajustado"] / df["vlPreco"])-1)).round(2)
df

# %%

# Cálculo de logaritmo usando o Numpy
np.log(df["txtAjustado(%)"])

# %%

# Adiciona uma coluna que mostra o logaritmo do preço ajustado
df["txtLogAjustado"] = np.log(df["txtAjustado(%)"])
df

# %%

# Adiciona uma coluna que mostra o exponencial do preço ajustado
df["txtexpAjustado"] = np.exp(df["txtAjustado(%)"])
df

# %%

# Aplicando funções aos dados

#def rodolfinho(x):
    #total = 1
    #for i in range(2, int(x) + 1):
        #total = total*i
       # total *= i
       # return total

#df["Preco_Ajustado"].apply(np.)

# %%
