#%%
import os
import shutil

source_path = os.path.abspath('C:/Users/shc')#源地址
target_path = os.path.abspath('D:/out')#目标地址
if not os.path.exists(target_path):# 如不存在目标地址
    os.makedirs(target_path)#建立
if os.path.exists(source_path):#存在源地址
    
    for root, dirs, files in os.walk(source_path):# root 本身的地址# dirs 是一个 list，# files 同样是 list, 
        
        for file in files:
            print(file)
         
            if file.find('ipynb') > -1 :
                src_file = os.path.join(root, file)
                shutil.copy(src_file, target_path)
