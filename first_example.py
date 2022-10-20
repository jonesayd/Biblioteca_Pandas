import pandas as pd

#Primeiro exemplo:

x = [1, 2, 3, 4]
y = ['a', 'b', 'c', 'd']

df = pd.DataFrame(x, y)
print(df)

#Segundo exemplo:

nome_tabvar = {
    
    "col1": [1,2], "col2": [3,4]
    
    }
df = pd.DataFrame(data=nome_tabvar)
print(df)