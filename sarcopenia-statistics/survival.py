from lifelines.statistics import logrank_test
from lifelines import KaplanMeierFitter
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sn

##  set seaborn themes
sn.set_theme(color_codes=True)

'''
The main idea is to divide the range between min SMA and max SMA into 100 section, 
calculate p-value of peto's logrank test using the middle 91 SMA area as cut-offs. 
the p-value with < 0.05 will be selected for drawing survival plot .
'''

##  read files
df = pd.read_csv(r'./xlsx_csv/df_merge.csv',index_col=0, header=0)

kmf = KaplanMeierFitter()

T = df['Survival Time (up to 3 years)']
E = df['Death']

arr = np.zeros([91])

df_SMA = df['SMA_Major']

min_SMA = df_SMA.min()
max_SMA = df_SMA.max()

cutoff_EWGSOP = df_SMA.mean() - 2 * df_SMA.std()
print(cutoff_EWGSOP > min_SMA)

for i in range(91):
    cut_off = min_SMA + (max_SMA - min_SMA) / 100 * (i + 5)
    ix = df_SMA > cut_off
    results = logrank_test(T[ix], T[~ix], E[ix], E[~ix], weightings='peto')
    # results.print_summary(3)
    arr[i] = results.p_value

arr[np.isnan(arr)] = 1.
p_value = np.min(arr)
if p_value < 0.01:
    index = np.argwhere(arr < 0.01)
else:
    index = np.argwhere(arr == p_value)

cutoff = min_SMA + (max_SMA - min_SMA) / 100 * (max(sum(index)/len(index)) + 5)

if cutoff < 0.5 * (max_SMA + min_SMA):
    final_cutoff = min_SMA + (max_SMA - min_SMA) / 100 * (max(index)[0] + 5)
else:
    final_cutoff = min_SMA + (max_SMA - min_SMA) / 100 * (min(index)[0] + 5)

print(final_cutoff)
print(p_value)

x = np.arange(91)
x = min_SMA + (max_SMA - min_SMA) / 100 * (x + 5)

plt.plot(x,arr,linestyle='-')

plt.plot([min_SMA, final_cutoff], [p_value, p_value], c='#FF7026', linestyle='--')
plt.plot([final_cutoff, final_cutoff], [-0.05, p_value], c='#FF7026', linestyle='--')
final_cutoff = int(final_cutoff)
p_value = round(p_value,3)

plt.text(final_cutoff + 100, p_value -0.005, 'cutoff = {} {}, p = {}'.format(final_cutoff, '${mm^2}$', p_value), fontdict={'size':14,'color':'#EE5012','style':'italic'})
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.title('Pectoralis Major', fontsize=14)
plt.ylabel('Significance (p-value)', fontsize=14)
plt.xlabel('Cutoff value (${mm^2}$)', fontsize=14)
plt.ylim(-0.05, 1)
plt.xlim(min_SMA, max_SMA)

plt.tight_layout()
plt.savefig('./output/figure2/SMA_T12_cutoff.png',dpi=600)
plt.clf()

ix = df_SMA > final_cutoff

for name, df in df.groupby(ix):
    kmf.fit(df["Survival Time (up to 3 years)"], df["Death"], label='area > {}{}'.format(int(final_cutoff),'${mm^2}$') if name == 1 else 'area < {}{}'.format(int(final_cutoff),'${mm^2}$'))
    kmf.plot_survival_function(at_risk_counts=False)

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.ylabel('Survival probability', fontsize=14)
plt.xlabel('Follow up time (days)', fontsize=14)
plt.xlim(0, 1095)
plt.ylim(0, 1)

plt.tight_layout()
plt.savefig('./output/figure2/SMA_T12_survival.png',dpi=600)
plt.clf()


## and the same for SMA

'''
df_MHU = df['MHU_T4']

min_MHU = df_MHU.min()
max_MHU = df_MHU.max()

for i in range(91):
    cut_off = min_MHU + (max_MHU - min_MHU) / 100 * (i + 5)
    ix = df_MHU > cut_off
    results = logrank_test(T[ix], T[~ix], E[ix], E[~ix], weightings='peto')
    # results.print_summary(3)
    arr[i] = results.p_value

arr[np.isnan(arr)] = 1.
final_p = np.min(arr)

if final_p < 0.05:
    index = np.argwhere(arr < 0.05)
else:
    index = np.argwhere(arr == final_p)

cutoff = min_MHU + (max_MHU - min_MHU) / 100 * (max(sum(index)/len(index)) + 5)
print(cutoff)
print(0.5 * (max_MHU + min_MHU))

if cutoff < 0.5 * (max_MHU + min_MHU):
    final_cutoff = min_MHU + (max_MHU - min_MHU) / 100 * (max(index)[0] + 5)
else:
    final_cutoff = min_MHU + (max_MHU - min_MHU) / 100 * (min(index)[0] + 5)

print(final_cutoff)
print(p_value)

ix = df_MHU < final_cutoff
final_cutoff = format(final_cutoff, '.2f')
print(ix)
x = np.arange(91)
x = min_MHU + (max_MHU - min_MHU) / 100 * (x + 5)

plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.ylabel('p value', fontsize=10)
plt.xlabel('cutoff value', fontsize=10)
plt.ylim(0, 1)

plt.plot(x,arr,linestyle='-')

plt.show()

for name, df in df.groupby(ix):
    kmf.fit(df["Survival Time (up to 3 years)"], df["Death"], label='MHU < {}'.format(final_cutoff) if name == 1 else 'MHU > {}'.format(final_cutoff))
    kmf.plot_survival_function(at_risk_counts=False)

plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.ylabel('Survival probability', fontsize=10)
plt.xlabel('Follow up time(days)', fontsize=10)
plt.xlim(0, 1095)
plt.ylim(0, 1)

plt.tight_layout()

plt.show()
'''