#%%
import os
import shutil

source_path = os.path.abspath('C:/Users/Administrator')#源地址
target_path = os.path.abspath('D:/ipynb')#目标地址

    
for file in os.listdir('C:/Users/Administrator'):# 遍历文件夹   
    
    try:
        if file.split('.')[1]==str('ipynb'):
            src_file = os.path.join(source_path, file)
            shutil.copy(src_file, target_path)
            print(file)
    except Exception :       
        pass