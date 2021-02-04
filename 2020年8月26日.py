#%%
import datetime
from pyforest import *

s = datetime.datetime.now()  #当前时间
date=s.strftime("%Y%m%d")
#-------------------------------------------------------------------     

path = ('C:/美仓/')
#os.chdir='C:/in/广告报表'


data=[]   
for root, dirs, files in os.walk(path):# root 本身的地址# dirs 是一个 list，# files 同样是 list, 
    
    for file in files:
        file=os.path.join(root, file)
        df=pd.read_excel(file)
        riqi='2020'+root.split('/')[2].split('.')[0]+root.split('/')[2].split('.')[1]
        print(riqi)
        

# %%
