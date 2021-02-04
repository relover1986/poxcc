#%%
from pip._internal.utils.misc import get_installed_distributions
import datetime
import pandas as pd  
s = datetime.datetime.now()  #当前时间
date=s.strftime("%Y-%m-%d")

packages = get_installed_distributions()
file_name = 'D:/OneDrive/data/pip.csv'
file=open(file_name,mode='w')
file.close()
for i in packages:
    text=str(i).split()[0]
    print(text)
    file=open(file_name,mode='a+')
    file.write(text+"\n")
file.close()

df=pd.read_csv(file_name)
df=df.sort_values(by=df.columns[0])
df.to_csv(file_name,index=False)
e = datetime.datetime.now()  #当前时间

print("提示", "用时:" + str(e - s) + '秒')
#-------------------------------------------------------------------------------------


# %%
