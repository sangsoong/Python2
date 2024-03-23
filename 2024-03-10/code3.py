import matplotlib.pyplot as plt
import pandas as pd

dataframe = pd.read_excel(r'C:\baejunwoo\Financial Sample.csv')
df_dict = dict(dataframe)

x_segment = list(df_dict['Segment'])
y_price = list(dict(df_dict['Sale Price']))

plt.plot(x_segment, y_price, linestyle="--", marker="^")
plt.show()