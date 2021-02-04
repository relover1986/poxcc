#%%
# 计算每条数据离现在最近一次消费时间（R）
import datetime
import os
import warnings

import pandas as pd
# 绘制帕累托图
import pyecharts.options as opts
from pyecharts import options as opts
from pyecharts.charts import Bar, Funnel, Line, Radar,Page
from pyecharts.commons.utils import JsCode

import time

now = int(time.time())

a = "2021-01-10 23:40:00"

timeArray = time.strptime(a, "%Y-%m-%d %H:%M:%S")

time_stamp = int(time.mktime(timeArray))
if now <time_stamp :

    os.chdir(os.getcwd())


    warnings.filterwarnings('ignore')

    df = pd.read_excel('1.xlsx',sheet_name='1')
    df.head()

    # 计算每个阶段的人数
    loudou = df['行为阶段'].value_counts().reset_index()
    # 增加列，每个阶段对应上个阶段的人数
    jieduan0 = list(loudou['行为阶段'])
    jieduan1 = []
    for j in range(len(jieduan0)):
        if j == 0:
            jieduan1.append(jieduan0[j])
        else:
            jieduan1.append(jieduan0[j-1])
    loudou['行为阶段1'] = jieduan1
    # 增加列，每个阶段的转化率
    loudou['转化率'] = loudou['行为阶段'] / loudou['行为阶段1']
    loudou



    # 添加百分比显示
    xinwei = list(loudou['index'])
    zhuanhua = list(loudou['转化率'])
    label = []
    for i in range(len(xinwei)):
        l = xinwei[i] + str(round(zhuanhua[i]*100,2)) + '%'
        label.append(l)

    z = (
        Funnel()
        .add("行为", [list(z) for z in zip(label,
                                        list(loudou['行为阶段']))],
            label_opts=opts.LabelOpts(is_show=True, position="inside"),
            tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b} : {c}人"),
            )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="转化漏斗"
            )
        )
    )
    #z.render('转化漏斗.html')
    z.render_notebook()

    warnings.filterwarnings('ignore')
    df = pd.read_excel('1.xlsx',sheet_name='2')
    df.head()

    # 以商品种类进行分组计算销售额
    k_m = df.groupby('品类描述').sum()['销售额'].reset_index()
    # 按销售额降序排序
    k_m = k_m.sort_values(by=['销售额'],ascending=False)
    # 计算总销售额
    k_m['总销售额'] = k_m['销售额'].sum()
    # 计算销售额占比
    k_m['销售额占比'] = k_m['销售额'] / k_m['总销售额']
    # 累计销售额占比
    zhanbi = list(k_m['销售额占比'])
    neiji = []
    for i in range(len(zhanbi)):
        if i == 0:
            neiji.append(zhanbi[i])
        else:
            neiji.append(neiji[i-1]+zhanbi[i])
    k_m['累计占比'] = neiji
    # 判断累加值是否大于 80%
    k_m['flag'] = k_m['累计占比'].map(lambda x: 1 if x < 0.8 else 0)
    k_m


    # 选出占比达到 80% 的销售额
    m = list(k_m[k_m['flag'] == 1]['销售额'])[-1]

    x_data = list(k_m['品类描述'])

    color_function = """
            function (params) {
                if (params.value >= %s) {
                    return '#749f83';
                } else  {
                    return '#d48265';
                }
            }
            """ % str(m)
    bar = (
        Bar()
        .add_xaxis(xaxis_data=x_data)
        .add_yaxis(
            series_name="销售额",
            y_axis=list(k_m['销售额']),
            z=0,
            label_opts=opts.LabelOpts(is_show=False),
            itemstyle_opts=opts.ItemStyleOpts(color=JsCode(color_function))
        )
        .extend_axis(
            yaxis=opts.AxisOpts(
                name="销售额占比",
                type_="value",
                min_=0,
                max_=1.1,
                #interval=5,
                axislabel_opts=opts.LabelOpts(formatter="{value}"),
            )
        )
        .set_global_opts(
            tooltip_opts=opts.TooltipOpts(
                is_show=True, trigger="axis", axis_pointer_type="cross"
            ),
            xaxis_opts=opts.AxisOpts(
                type_="category",
                axispointer_opts=opts.AxisPointerOpts(is_show=True, type_="shadow"),
            ),
            yaxis_opts=opts.AxisOpts(
                name="销售额",
                type_="value",
                #min_=0,
                #max_=250,
                #interval=50,
                axislabel_opts=opts.LabelOpts(formatter="{value} 元"),
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
            legend_opts=opts.LegendOpts(
                type_="scroll",
            )
        )
    )

    line = (
        Line()
        .add_xaxis(xaxis_data=x_data)
        .add_yaxis(
            series_name="销售额累计占比",
            yaxis_index=1,
            y_axis=list(k_m['累计占比']),
            label_opts=opts.LabelOpts(is_show=False),
            z=1,
            markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(y=0.8)])
        )
    )

    #bar.overlap(line).render('帕累托图.html')
    bar.overlap(line).render_notebook()
    warnings.filterwarnings('ignore')


    df = pd.read_excel('1.xlsx',sheet_name='3')
    df.head()
    def R(s):
        s = datetime.datetime.strptime(s,'%Y-%m-%d')
        now = str(datetime.datetime.now()).split()[0]
        now = datetime.datetime.strptime(now,'%Y-%m-%d')
        r = now - s
        r = int(str(r).split()[0])
        return r
    df['R'] = df['DATE'].map(R)
    # 分组计算每个【COMPANY】，最小【R】，计数【AMOUNT】，合计【MONEY】
    rfm = df.groupby(['COMPANY','CUSTOMERNAME','CUSTOMERTYPE']).agg({'R':'min','AMOUNT':'count','MONEY':'sum'}).reset_index()
    rfm.rename(columns={'AMOUNT':'F','MONEY':'M'},inplace=True)
    # 计算平均 RFM
    rfm['avg_R'] = round(rfm['R'].mean(),0)
    rfm['avg_F'] = round(rfm['F'].mean(),0)
    rfm['avg_M'] = round(rfm['M'].mean(),0)
    # 大于平均值标记 1
    rfm['flag_R'] = rfm['R'] < rfm['avg_R']
    rfm['flag_R'] = rfm['flag_R'].map(lambda x: '1' if x else '0')
    rfm['flag_F'] = rfm['F'] > rfm['avg_F']
    rfm['flag_F'] = rfm['flag_F'].map(lambda x: '1' if x else '0')
    rfm['flag_M'] = rfm['M'] > rfm['avg_M']
    rfm['flag_M'] = rfm['flag_M'].map(lambda x: '1' if x else '0')
    # 合并 RFM 指标，分组计算每种类型平均值
    rfm['RFM'] = rfm['flag_R'] + rfm['flag_F'] + rfm['flag_M']
    rfm = round(rfm.groupby('RFM').mean()[['R','F','M']].reset_index(),0)
    rfm



    v1 = [[5533.0,3.0,273007.0]]
    v2 = [[5807.0,7.0,3549416.0]]
    v3 = [[5413.0,30.0,436867.0]]
    v4 = [[5445.0,45.0,12299335.0]]
    v5 = [[3470.0,6.0,205551.0]]
    v6 = [[3317.0,12.0,3831896.0]]
    v7 = [[3152.0,64.0,460734.0]]
    v8 = [[3177.0,69.0,10912394.0]]
    c = (
        Radar()
        .add_schema(
            schema=[
                opts.RadarIndicatorItem(name="R", max_=6000),
                opts.RadarIndicatorItem(name="F", max_=75),
                opts.RadarIndicatorItem(name="M", max_=12299335.0),
            ]
        )
        .add("一般挽留客户", v1,color="#ff4d4f")
        .add("重要挽留客户", v2,color="#ffc069")
        .add("一般保持客户", v3,color="#ffec3d")
        .add("重要保持客户", v4,color="#a0d911")
        .add("一般发展客户", v5,color="#13c2c2")
        .add("重要发展客户", v6,color="#2f54eb")
        .add("一般价值客户", v7,color="#531dab")
        .add("重要价值客户", v8,color="#c41d7f")
        .set_series_opts(
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            legend_opts=opts.LegendOpts(pos_left='0%')
        )
    )
    #c.render('RFM 雷达图.html')
    c.render_notebook()
    page = Page(layout=Page.SimplePageLayout)
    page.add(z,
        bar.overlap(line),
        c,

    )
    page.render("3个图.html")
    page.render_notebook()

# %%
