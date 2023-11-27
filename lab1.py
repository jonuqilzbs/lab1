import numpy as np
import pandas as pd
import seaborn as sns
data = {
    "Хлеб": np.random.normal(60, 10, 12),
    "Молоко": np.random.normal(50, 9, 12),
    "Помидоры": np.random.normal(60, 20, 12),
    "Огурцы": np.random.normal(79, 8, 12),
    "Батон": np.random.normal(67, 4, 12),
    "Масло": np.random.normal(32, 2, 12),
    "Ручки": np.random.normal(105, 29, 12),
    "Сметана": np.random.normal(54, 7, 12),
    "Кетчуп": np.random.normal(40, 3, 12),
    "Майонез": np.random.normal(100, 9, 12),
}
df = pd.DataFrame(data)
df
ax = sns.lineplot(df)
sns.move_legend(ax, 'upper left', bbox_to_anchor=(1,1))
p0 = df.sum()/df.shape[0]
p0
std = ((df-p0)**2).sum()/(df.shape[0]-1)
std = std**(1/2)
x_extrapol = p0+np.random.normal(0, std,len(p0))
pd.concat([df,pd.DataFrame([x_extrapol], columns=x_extrapol.index)]).reset_index(drop=True)
reliability = std/p0
reliability
cond1 = ((df-p0)<2*std).all()
cond1
cond2 = p0>2*std
cond2
cond3 = (df>0).all()
cond3
product_color = pd.Series(dtype="string")
for name in df.columns:
    if (not cond3[name]):
        product_color[name] = "Красный"
    elif ( not cond1[name] and not cond2[name]):
        product_color[name]="Оранжевый"
    elif ( not cond1[name] or not cond2[name]):
        product_color[name]="Желтый"
    else:
         product_color[name]="Зеленый"
product_color