#%%
import os,datetime
os.chdir(r'c:\Users\Administrator\AppData\Local\Programs\Python\Python38\Scripts')
date=datetime.datetime.now().strftime("%Y-%m-%d")
file_name = 'D:/OneDrive/data/pip'+date+'.csv'
f = open(file_name,'r') # 以只读方式打开
libs = f.readlines() # 读取文本文档中的每一行
f.close
web = "https://pypi.tuna.tsinghua.edu.cn/simple "  # 清华大学镜像源。
# web = "http://mirrors.aliyun.com/pypi/simple "  # 阿里云镜像源。
# web = "https://pypi.mirrors.ustc.edu.cn/simple "  # 中国科技大学镜像源。
# web = "http://pypi.douban.com/simple "  # 豆瓣镜像源。
n=int(len(libs))
for lib in libs:
    lib=lib.rstrip("\n") # 去掉换行符 "\n"
    os.system("pip install -i "+ web + lib) # 选择其中一个镜像源，下载安装库。
    print(lib,n)
    n=n-1
print('---------------------------------------')

