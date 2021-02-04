#%%
src_file='d:/OneDrive/python/工作-库存.py'


f = open(src_file,'r') # 以只读方式打开
libs = f.readlines() 

newfile=open('D:/out/x.txt','w')
for a in libs:
    if '#' in a:
        newfile.write(str(a).split('#')[1]+"\n")
newfile.close()


# %%
