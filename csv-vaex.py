#%%
import pandas as pd
import os
import vaex 

os.chdir(r'\\NAS\WDbackup\备份\Yaf')
path = '//Nas/市场营销部/X销售数据留档/2020/2020-销售数据留档/'
data = []

for file in os.listdir(path):
    df = pd.read_csv(path + file, encoding="gbk",thousands=",")
    df['date'] = file.split(".")[0].split("-")[1]
    df['date'] = df['date'].astype('datetime64[ns]')
    df['Ordered Product Sales'] = df['Ordered Product Sales'].str[1:]
    data.append(df)
df = pd.concat(data)

df.to_csv('FBA.csv')

dv = vaex.from_csv('FBA.csv', convert=True, chunk_size=5_000_000) 


dv = vaex.open('FBA.csv.hdf5') 

print(dv.shape)
print('------------------------------')

# %%
