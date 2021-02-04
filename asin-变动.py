#%%
from pyforest import *

path='//Nas/市场营销部/B部门工作计划/【店铺整理】全平台/'

data=[]

for i in os.listdir(path):
    file=path+i

    if i.endswith('xlsx') and '~' not in i:

        df=pd.read_excel(file)
        print(file)
        df=df[['变更日期','任务编号','变更原因','Item SKU','产品统一名称','Marketplace']]
       
        df=df[df['Marketplace']=='Amazon']
        del df['Marketplace']
        data.append(df)

df=pd.concat(data)
df['变更日期']=df['变更日期'].astype('datetime64[ns]')
df=df.sort_values(by=['变更日期'],ascending=False)   
df.to_excel('//nas/信息开发部/asin变动.xlsx',index=False)     

# %%
