#%%
import os
import datetime

s = datetime.datetime.now() 
os.chdir(r'c:\Users\Administrator\AppData\Local\Programs\Python\Python38\Scripts')

os.system('pyinstaller -F -w -i python.ico  早会.py')
e = datetime.datetime.now() 
print(e-s,'--------------------------------------------------------------------')

# %%
import os
import datetime

s = datetime.datetime.now() 
os.chdir(r'c:\Users\Administrator')

os.system('pip install -i https://pypi.tuna.tsinghua.edu.cn/simple folium')
e = datetime.datetime.now() 
print(e-s,'-------------')

# %%


import os
import datetime

s = datetime.datetime.now() 
os.chdir(r'c:\Users\Administrator\AppData\Local\Programs\Python\Python38\Scripts')

os.system('pip install -i https://pypi.tuna.tsinghua.edu.cn/simple drymail')
e = datetime.datetime.now() 
print(e-s,'-------------')


# %%
