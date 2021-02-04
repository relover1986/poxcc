#%%
from pyforest import *
import datetime
from openpyxl import load_workbook

#----------------------------------------------------

time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
path=os.getcwd()
file=path+'/asin-变动.xlsx'
name=path.split('\\')[1]


df=pd.read_excel(file)
df['日期']=df['日期'].astype('datetime64[ns]')
df['日期']=df['日期'].fillna(time)
#df.loc[pd.isna(df['日期']),'日期']=time
df['操作人']=path.split('\\')[1]

df.to_excel(file,index=False)


wb = load_workbook(file)
ws = wb.worksheets[0]
ws.auto_filter.ref = ws.dimensions  # 筛选

ws.freeze_panes = 'A2'   # 同时冻结第一行和第一列
ws.column_dimensions['c'].width = 21.3


wb.save(file)
wb.save('c:/out/asin-变动-'+name+'.xlsx')
print("-----------------",file)
# %%
