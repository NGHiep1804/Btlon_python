import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data=pd.read_csv('results.csv')
data=data.drop(columns=['Unnamed: 0',  'Nation', 'Position', 'Team'])
data_list=data.values.tolist()
header=list(data.columns)

def vitri(name):
    for i in range(len(data_list)):
        if name==data_list[i][0]:   return i
    return -1

i=-1
j=-1
while i==-1 or j==-1:
    print('Vui long nhap ten')
    i=vitri(input())
    j=vitri(input())
categories=header[9:16]
player1_stats=data_list[i][9:16]
player2_stats=data_list[j][9:16]

num_vars = len(categories)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
player1_stats += player1_stats[:1]
player2_stats += player2_stats[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.fill(angles, player1_stats, color='blue', alpha=0.25, label="Cầu thủ 1")
ax.fill(angles, player2_stats, color='red', alpha=0.25, label="Cầu thủ 2")
ax.plot(angles, player1_stats, color='blue', linewidth=2)
ax.plot(angles, player2_stats, color='red', linewidth=2)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)
plt.title("So sánh chỉ số của hai cầu thủ")
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))
plt.show()
