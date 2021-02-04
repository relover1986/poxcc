#%%import datetime
from pyforest import *
from tkinter import messagebox
import datetime

s = datetime.datetime.now()  #当前时间
date=s.strftime("%Y-%m-%d")

#-------------------------------------------------------------------    
data=[]
for file in os.listdir("d:/美仓日期"):  # 遍历文件夹

    df = pd.read_excel('d:/美仓日期/' + file)  #展开每个文件sheets
    df=df[['SKU','Total']]
    df.columns=['sku','Total']
    df=df[~(df['sku'].isnull())] #删掉空行
    riqi=datetime.date(2020, int(file.split('.')[0]), int(file.split('.')[1]))
    df['日期']=riqi
    data.append(df)

df=pd.concat(data)

df.to_excel('c:/out/美仓汇总.xlsx',index=False)  #d写入文件名加sheet

#------------------------------------------------------------------- 

e = datetime.datetime.now()  #当前时间

messagebox.showinfo("提示", "用时:" + str(e - s) + '秒')
# %%
from pyforest import *
from tkinter import messagebox
import datetime

s = datetime.datetime.now() 
df=pd.read_excel('c:/out/美仓汇总.xlsx')
df_pp=pd.read_excel('//nas/信息开发部/信息部/匹配库/sku-spu匹配库.xlsx')
df_pp=df_pp[['sku','spu','包装形式']]
df=pd.merge(df,df_pp,on='sku',how='left')
df['数量']=df['Total']*df['包装形式']
df['日期']=df['日期'].astype('str')
df=pd.pivot_table(df,values=["数量"],index=['spu'],columns=['日期'],aggfunc=('sum')).reset_index()
df = df.droplevel(0, 1)
df=df.fillna(0)

df.to_excel('c:/out/美仓汇总-spu.xlsx',index=False)
e = datetime.datetime.now()  #当前时间

messagebox.showinfo("提示", "用时:" +str(e - s) + '秒')
# %%
