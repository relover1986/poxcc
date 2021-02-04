#%%
import os
import printe

path = os.path.abspath('D:/word')#目标地址
if not os.path.exists(path):# 如不存在目标地址
    os.makedirs(path)#建立

for a,b,c in os.walk(path):
    print(c)
for i in c:
    f=os.path.join(path,i)
    if f.endswith("docx"):
        print(f)
        printe.printer_loading(f)

#%%
import printe
from pathlib2 import Path    

path = os.path.abspath('D:/word')#目标地址
if not os.path.exists(path):# 如不存在目标地址
    os.makedirs(path)#建立

path='d:/word'
p=Path(path)
file_name=p.glob('*.docx')
for i in file_name:
    print(i)
    printe.printer_loading(str(i))
# %%
