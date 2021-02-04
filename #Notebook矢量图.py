#In[]

import os
import warnings

import matplotlib
import matplotlib.pyplot as plt
from IPython import get_ipython

os.chdir('D:\OneDrive - edy\data')
warnings.filterwarnings("ignore")#忽视警告
get_ipython().run_line_magic('matplotlib', 'inline')#显示图
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'svg'")#矢量

matplotlib.rcParams['font.family']='sans-serif'#无衬线字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']#指定默认字体
matplotlib.rcParams['axes.unicode_minus'] = False#解决负号’-‘显示为方块的问题

%matplotlib inline
%config InlineBackend.figure_format = 'svg'
