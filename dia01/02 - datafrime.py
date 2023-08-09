# %%
import pandas as pd

# %%

data = {
    "nome":["Téo","Nah","Maria","Marina","Jessica","InfoSlack","Rodolfo"],
    "idade":[30 ,33, 31 , 45, 52, 60, 56],
    "Cor":["Azul","Preto","Vermelho","Rosa","Verde","Amarelo","Marrom"],
    "renda":[1250, 1350, 4250, 6526, 5231, 9685, 13500]   
        }
data["idade"]

# %%

df = pd.DataFrame(data)
df

# %%

df[["idade","renda"]].describe()
# %%

df[["idade","renda"]].mean()
# %%
