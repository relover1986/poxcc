#%%
import altair as alt
import pandas as pd
settle_data = pd.read_csv("D:/OneDrive/data/seattle-weather.csv")  # 导入数据集，数据见文末
settle_data.weather.unique()  # 定义比例：根据天气类型的分布来绘制数据
scale = alt.Scale(domain=['sun', 'fog', 'drizzle', 'rain', 'snow'],
                  range=['#e7ba52', '#a7a7a7', '#aec7e8', '#1f77b4', '#9467bd'])
color = alt.Color('weather:N', scale=scale)
brush = alt.selection_interval(encodings=['x'])  #添加互动功能
click = alt.selection_multi(encodings=['color'])
#顶部散射图：温度 Vs 日期
points = alt.Chart().mark_point().encode(
    alt.X('monthdate(date):T', title='Date'),
    alt.Y('temp_max:Q',
        title='Maximum Daily Temperature (C)',
        scale=alt.Scale(domain=[-5, 40])
    ),
    color=alt.condition(brush, color, alt.value('lightgray')),
    size=alt.Size('precipitation:Q', scale=alt.Scale(range=[5, 200]))
).properties(
    width=1080,
    height=500
).add_selection(
    brush
).transform_filter(
    click
)
##########################
# 2. 底部栏图：天气类型
bars = alt.Chart().mark_bar().encode(
    x='count()',
    y='weather:N',
    color=alt.condition(click, color, alt.value('lightgray')),
).transform_filter(
    brush
).properties(
    width=550,
).add_selection(
    click
)
##########################
#3. 构建复合图：垂直串联两个图表
tu=alt.vconcat(
    points,
    bars,
    data=settle_data,
    title="天气数据: 2012-2015"
)
tu.save('c:/in/4.html')
# %%
