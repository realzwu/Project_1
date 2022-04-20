import seaborn as sn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kstest


#  set seaborn themes
sn.set_theme(color_codes=True)

df1 = pd.read_csv(r'./xlsx_csv/df_merge.csv',index_col=0, header=0)
df2 = pd.read_csv(r'./xlsx_csv/df_male.csv',index_col=0, header=0)
df3 = pd.read_csv(r'./xlsx_csv/df_female.csv',index_col=0, header=0)

l3_mean1 = df1['SMA_L3'].mean()
l3_std1 = df1['SMA_L3'].std()
l3_mean2 = df2['SMA_L3'].mean()
l3_std2 = df2['SMA_L3'].std()
l3_mean3 = df3['SMA_L3'].mean()
l3_std3 = df3['SMA_L3'].std()

t12_mean1 = df1['SMA_T12'].mean()
t12_std1 = df1['SMA_T12'].std()
t12_mean2 = df2['SMA_T12'].mean()
t12_std2 = df2['SMA_T12'].std()
t12_mean3 = df3['SMA_T12'].mean()
t12_std3 = df3['SMA_T12'].std()

t4_mean1 = df1['SMA_T4'].mean()
t4_std1 = df1['SMA_T4'].std()
t4_mean2 = df2['SMA_T4'].mean()
t4_std2 = df2['SMA_T4'].std()
t4_mean3 = df3['SMA_T4'].mean()
t4_std3 = df3['SMA_T4'].std()

major_mean1 = df1['SMA_Major'].mean()
major_std1 = df1['SMA_Major'].std()
major_mean2 = df2['SMA_Major'].mean()
major_std2 = df2['SMA_Major'].std()
major_mean3 = df3['SMA_Major'].mean()
major_std3 = df3['SMA_Major'].std()

minor_mean1 = df1['SMA_Minor'].mean()
minor_std1 = df1['SMA_Minor'].std()
minor_mean2 = df2['SMA_Minor'].mean()
minor_std2 = df2['SMA_Minor'].std()
minor_mean3 = df3['SMA_Minor'].mean()
minor_std3 = df3['SMA_Minor'].std()

print(round(l3_mean1))
print(round(t12_mean1))
print(round(t4_mean1))
print(round(major_mean1))
print(round(minor_mean1))

print(round(l3_std1))
print(round(t12_std1))
print(round(t4_std1))
print(round(major_std1))
print(round(minor_std1))
print(30*'=')

# The x position of bars
r1 = [0,1.6,3.2,4.8,5.8]
r2 = [x + 0.3 for x in r1]
r3 = [x + 0.6 for x in r1]
r4 = [0.9,2.5,4.1]
r5 = [x + 0.3 for x in r4]

plt.figure(figsize=(11,5))

## calculate the group difference using K-S test
p1 = kstest(df2['SMA_L3'], df3['SMA_L3'], alternative='two-sided', mode='auto')
p2 = kstest(df2['SMA_T12'], df3['SMA_T12'], alternative='two-sided', mode='auto')
p3 = kstest(df2['SMA_T4'], df3['SMA_T4'], alternative='two-sided', mode='auto')
p4 = kstest(df2['SMA_Major'], df3['SMA_Major'], alternative='two-sided', mode='auto')
p5 = kstest(df2['SMA_Minor'], df3['SMA_Minor'], alternative='two-sided', mode='auto')
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
print(30*'-')

p1 = kstest(df2['MHU_L3'], df3['MHU_L3'], alternative='two-sided', mode='auto')
p2 = kstest(df2['MHU_T12'], df3['MHU_T12'], alternative='two-sided', mode='auto')
p3 = kstest(df2['MHU_T4'], df3['MHU_T4'], alternative='two-sided', mode='auto')
p4 = kstest(df2['MHU_Major'], df3['MHU_Major'], alternative='two-sided', mode='auto')
p5 = kstest(df2['MHU_Minor'], df3['MHU_Minor'], alternative='two-sided', mode='auto')
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)

# Create bars
plt.bar(r1, [l3_mean1,t12_mean1,t4_mean1,major_mean1,minor_mean1], width=0.3, color='#85E585', yerr=[l3_std1,t12_std1,t4_std1,major_std1,minor_std1], capsize=7, label='Male and female')

plt.bar(r2, [l3_mean2,t12_mean2,t4_mean2,major_mean2,minor_mean2], width=0.3, color='#8585E5', yerr=[l3_std2,t12_std2,t4_std2,major_std2,minor_std2], capsize=7, label='Male')

plt.bar(r3, [l3_mean3,t12_mean3,t4_mean3,major_mean3,minor_mean3], width=0.3, color='#E58585', yerr=[l3_std3,t12_std3,t4_std3,major_std3,minor_std3], capsize=7, label='Female')

plt.bar(r4, [18992,13911,3900], width=0.3, color='#C5C5E5', yerr=[2418,2279,1000], capsize=7, label='Healthy male')

plt.bar(r5, [12551,9144,2800], width=0.3, color='#E5C5C5', yerr=[1691,1614,900], capsize=7, label='Healthy female')


# general layout
plt.xticks([0.6,2.2,3.8,5.1,6.1], ['L3', 'T12', 'Pectoralis','Pectoralis\nmajor', 'Pectoralis\nminor'])
plt.ylabel('Muscle area (${mm^2}$)')
plt.legend()

# Show graphic
plt.tight_layout()

plt.savefig('./output/figure2/SMA.png',dpi=600)
plt.clf()


l3_mean1 = df1['MHU_L3'].mean()
l3_std1 = df1['MHU_L3'].std()
l3_mean2 = df2['MHU_L3'].mean()
l3_std2 = df2['MHU_L3'].std()
l3_mean3 = df3['MHU_L3'].mean()
l3_std3 = df3['MHU_L3'].std()

t12_mean1 = df1['MHU_T12'].mean()
t12_std1 = df1['MHU_T12'].std()
t12_mean2 = df2['MHU_T12'].mean()
t12_std2 = df2['MHU_T12'].std()
t12_mean3 = df3['MHU_T12'].mean()
t12_std3 = df3['MHU_T12'].std()

t4_mean1 = df1['MHU_T4'].mean()
t4_std1 = df1['MHU_T4'].std()
t4_mean2 = df2['MHU_T4'].mean()
t4_std2 = df2['MHU_T4'].std()
t4_mean3 = df3['MHU_T4'].mean()
t4_std3 = df3['MHU_T4'].std()

major_mean1 = df1['MHU_Major'].mean()
major_std1 = df1['MHU_Major'].std()
major_mean2 = df2['MHU_Major'].mean()
major_std2 = df2['MHU_Major'].std()
major_mean3 = df3['MHU_Major'].mean()
major_std3 = df3['MHU_Major'].std()

minor_mean1 = df1['MHU_Minor'].mean()
minor_std1 = df1['MHU_Minor'].std()
minor_mean2 = df2['MHU_Minor'].mean()
minor_std2 = df2['MHU_Minor'].std()
minor_mean3 = df3['MHU_Minor'].mean()
minor_std3 = df3['MHU_Minor'].std()

print(round(l3_mean1,1))
print(round(t12_mean1,1))
print(round(t4_mean1,1))
print(round(major_mean1,1))
print(round(minor_mean1,1))

print(round(l3_std1,1))
print(round(t12_std1,1))
print(round(t4_std1,1))
print(round(major_std1,1))
print(round(minor_std1,1))

# The x position of bars
r1 = np.arange(5)
r2 = [x + 0.3 for x in r1]
r3 = [x + 0.6 for x in r1]
# r4 = [x + 0.6 for x in r1]

# Create blue bars
plt.bar(r1, [l3_mean1,t12_mean1,t4_mean1,major_mean1,minor_mean1], width=0.3, color='#85E585', yerr=[l3_std1,t12_std1,t4_std1,major_std1,minor_std1], capsize=7, label='Male and female')

# Create cyan bars
plt.bar(r2, [l3_mean2,t12_mean2,t4_mean2,major_mean2,minor_mean2], width=0.3, color='#8585E5', yerr=[l3_std2,t12_std2,t4_std2,major_std2,minor_std2], capsize=7, label='Male')

# Create cyan bars
plt.bar(r3, [l3_mean3,t12_mean3,t4_mean3,major_mean3,minor_mean3], width=0.3, color='#E58585', yerr=[l3_std3,t12_std3,t4_std3,major_std3,minor_std3], capsize=7, label='Female')

# general layout
plt.xticks([r + 0.3 for r in range(5)], ['L3', 'T12', 'Pectoralis','Pectoralis\nmajor', 'Pectoralis\nminor'])
plt.ylabel('Mean HU')
plt.legend()

# Show graphic
plt.tight_layout()
plt.savefig('./output/figure2/MHU.png',dpi=600)
