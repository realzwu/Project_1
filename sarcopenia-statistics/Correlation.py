
import pandas as pd
import seaborn as sn
import scipy.stats as ss
import matplotlib.pyplot as plt

df = pd.read_csv('./xlsx_csv/df_merge.csv',index_col=0,header=0)
df_male = pd.read_csv('./xlsx_csv/df_male.csv',index_col=0,header=0)
df_female = pd.read_csv('./xlsx_csv/df_female.csv',index_col=0,header=0)

## input all muscles for both gender
S_3, M_3, S_12, M_12, S_Major, S_Minor, M_Major, M_Minor = df['SMA_L3'], df['MHU_L3'], df['SMA_T12'], df['MHU_T12'], df['SMA_Major'], df['SMA_Minor'], df['MHU_Major'], df['MHU_Minor']
S_4 = S_Major + S_Minor
M_4 = (M_Major*S_Major+M_Minor*S_Minor) / S_4

S_3_M, M_3_M, S_12_M, M_12_M, S_Major_M, S_Minor_M, M_Major_M, M_Minor_M = df_male['SMA_L3'], df_male['MHU_L3'], df_male['SMA_T12'], df_male['MHU_T12'], df_male['SMA_Major'], df_male['SMA_Minor'], df_male['MHU_Major'], df_male['MHU_Minor']
S_4_M = S_Major_M + S_Minor_M
M_4_M = (M_Major_M*S_Major_M+M_Minor_M*S_Minor_M) / S_4_M

S_3_F, M_3_F, S_12_F, M_12_F, S_Major_F, S_Minor_F, M_Major_F, M_Minor_F = df_female['SMA_L3'], df_female['MHU_L3'], df_female['SMA_T12'], df_female['MHU_T12'], df_female['SMA_Major'], df_female['SMA_Minor'], df_female['MHU_Major'], df_female['MHU_Minor']
S_4_F = S_Major_F + S_Minor_F
M_4_F = (M_Major_F*S_Major_F + M_Minor_F*S_Minor_F) / S_4_F

##  Draw pearson correlation heatmaps
df_corr = df[['SMA_L3','SMA_T12','SMA_T4','SMA_Major','SMA_Minor']]
df_corr.rename(columns={'SMA_L3':'L3','SMA_T12':'T12','SMA_T4':'Pectoralis','SMA_Major':'Pec Major','SMA_Minor':'Pec Minor'},inplace=True)
corr_matrix = df_corr.corr(method='pearson')

heatmap = sn.heatmap(corr_matrix, vmin=0, vmax=1, annot=True, cmap='PuBu')
heatmap.set_title('Correlation Heatmap (Muscle area)', fontdict={'fontsize':12}, pad=16)
plt.tight_layout()
plt.savefig('./output/figure/heatmap_SMA.png',dpi=600)
plt.clf()

df_male_corr = df_male[['SMA_L3','SMA_T12','SMA_T4','SMA_Major','SMA_Minor']]
df_male_corr.rename(columns={'SMA_L3':'L3','SMA_T12':'T12','SMA_T4':'Pectoralis','SMA_Major':'Pec Major', 'SMA_Minor':'Pec Minor'},inplace=True)
corr_male_matrix = df_male_corr.corr(method='pearson')

heatmap = sn.heatmap(corr_male_matrix, vmin=0, vmax=1, annot=True, cmap='PuBu')
heatmap.set_title('Correlation Heatmap (Muscle area)', fontdict={'fontsize':12}, pad=16)
plt.tight_layout()
plt.savefig('./output/figure/heatmap_SMA_male.png',dpi=600)
plt.clf()

df_female_corr = df_female[['SMA_L3','SMA_T12','SMA_T4','SMA_Major','SMA_Minor']]
df_female_corr.rename(columns={'SMA_L3':'L3','SMA_T12':'T12','SMA_T4':'Pectoralis','SMA_Major':'Pec Major', 'SMA_Minor':'Pec Minor'},inplace=True)
corr_female_matrix = df_female_corr.corr(method='pearson')

heatmap = sn.heatmap(corr_female_matrix, vmin=0, vmax=1, annot=True, cmap='Oranges')
heatmap.set_title('Correlation Heatmap (Muscle area)', fontdict={'fontsize':12}, pad=16)
plt.tight_layout()
plt.savefig('./output/figure/heatmap_SMA_female.png',dpi=600)
plt.clf()


df_corr = df[['MHU_L3','MHU_T12','MHU_T4','MHU_Major','MHU_Minor']]
df_corr.rename(columns={'MHU_L3':'L3','MHU_T12':'T12','MHU_T4':'Pectoralis','MHU_Major':'Pec Major','MHU_Minor':'Pec Minor'},inplace=True)
corr_matrix = df_corr.corr(method='pearson')

heatmap = sn.heatmap(corr_matrix, vmin=0, vmax=1, annot=True, cmap='PuBu')
heatmap.set_title('Correlation Heatmap (Mean HU)', fontdict={'fontsize':12}, pad=16)
plt.tight_layout()
plt.savefig('./output/figure/heatmap_MHU.png',dpi=600)
plt.clf()

df_male_corr = df_male[['MHU_L3','MHU_T12','MHU_T4','MHU_Major','MHU_Minor']]
df_male_corr.rename(columns={'MHU_L3':'L3','MHU_T12':'T12','MHU_T4':'Pectoralis','MHU_Major':'Pec Major','MHU_Minor':'Pec Minor'},inplace=True)
corr_male_matrix = df_male_corr.corr(method='pearson')

heatmap = sn.heatmap(corr_matrix, vmin=0, vmax=1, annot=True, cmap='PuBu')
heatmap.set_title('Correlation Heatmap (Mean HU)', fontdict={'fontsize':12}, pad=16)
plt.tight_layout()
plt.savefig('./output/figure/heatmap_male_MHU.png',dpi=600)
plt.clf()

df_female_corr = df_female[['MHU_L3','MHU_T12','MHU_T4','MHU_Major','MHU_Minor']]
df_female_corr.rename(columns={'MHU_L3':'L3','MHU_T12':'T12','MHU_T4':'Pectoralis','MHU_Major':'Pec Major','MHU_Minor':'Pec Minor'},inplace=True)
corr_female_matrix = df_female_corr.corr(method='pearson')

heatmap = sn.heatmap(corr_female_matrix, vmin=0, vmax=1, annot=True, cmap='Oranges')
heatmap.set_title('Correlation Heatmap (Mean HU)', fontdict={'fontsize':12}, pad=16)
plt.tight_layout()
plt.savefig('./output/figure/heatmap_female_MHU.png',dpi=600)
plt.clf()

#  set seaborn themes
sn.set_theme(color_codes=True)

## MHU L3_T12
# calculate r2 and p-value for male
R2_and_p_value = ss.pearsonr(M_3_M,M_12_M)
(r,p) = R2_and_p_value
r2, p2 = format(r, '.4f') , format(p, '.4f')
text1 = '( {} = {}, p-value = {})'.format('${r^2}$',r2,p2).replace('= 0.0000','< 0.0001')

# calculate r2 and p-value for female
R2_and_p_value = ss.pearsonr(M_3_F,M_12_F)
(r,p) = R2_and_p_value
r2, p2 = format(r, '.4f') , format(p, '.4f')
text2 = '( {} = {}, p-value = {})'.format('${r^2}$',r2,p2).replace('= 0.0000','< 0.0001')

# regression plot
sn.regplot(x=M_3_M, y=M_12_M, color="#2040BB", line_kws={"color":"#2040BB","alpha":0.9,"lw":5})
plt.text(13,53, text1, fontdict={'size':14,'color':'#2040BB'})

sn.regplot(x=M_3_F, y=M_12_F, color="#FF7026", line_kws={"color":"#FF7026","alpha":0.9,"lw":5})
plt.text(13,50, text2, fontdict={'size':14,'color':'#FF7026'})

# label and save
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('Mean HU (L3)', fontdict={'size': 14})
plt.ylabel('Mean HU (T12)', fontdict={'size': 14})
plt.tight_layout()
plt.savefig('./output/figure/L3_T12_MHU_MF.png',dpi=600)
plt.clf()

# calculate r2 and p-value for both gender
R2_and_p_value = ss.pearsonr(M_3,M_12)
(r,p) = R2_and_p_value
r2, p2 = format(r, '.4f') , format(p, '.4f')
text = '( {} = {}, p-value = {})'.format('${r^2}$',r2,p2).replace('= 0.0000','< 0.0001')

# regression plot
sn.regplot(x=M_3, y=M_12, color="#2040BB", line_kws={"color":"#2040BB","alpha":0.9,"lw":5})
plt.text(13,54, text, fontdict={'size':14,'color':'#2040BB'})

# label and save
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('Mean HU (L3)', fontdict={'size': 14})
plt.ylabel('Mean HU (T12)', fontdict={'size': 14})
plt.tight_layout()
plt.tight_layout()
plt.savefig('./output/figure/L3_T12_MHU.png',dpi=600)
plt.clf()


## SMA L3_T12
# calculate r2 and p-value for male
R2_and_p_value = ss.pearsonr(S_3_M,S_12_M)
(r,p) = R2_and_p_value
r2, p2 = format(r, '.4f') , format(p, '.4f')
text1 = '( {} = {}, p-value = {})'.format('${r^2}$',r2,p2).replace('= 0.0000','< 0.0001')

# calculate r2 and p-value for female
R2_and_p_value = ss.pearsonr(S_3_F,S_12_F)
(r,p) = R2_and_p_value
r2, p2 = format(r, '.4f') , format(p, '.4f')
text2 = '( {} = {}, p-value = {})'.format('${r^2}$',r2,p2).replace('= 0.0000','< 0.0001')

# regression plot
sn.regplot(x=S_3_M, y=S_12_M, color="#2040BB", line_kws={"color":"#2040BB","alpha":0.9,"lw":5})
plt.text(3500,11500, text1, fontdict={'size':14,'color':'#2040BB'})

sn.regplot(x=S_3_F, y=S_12_F, color="#FF7026", line_kws={"color":"#FF7026","alpha":0.9,"lw":5})
plt.text(3500,10900, text2, fontdict={'size':14,'color':'#FF7026'})

# label and save
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('L3 muscle area ($\mathregular{mm^2}$)', fontdict={'size': 14})
plt.ylabel('T12 muscle area ($\mathregular{mm^2}$)', fontdict={'size': 14})
plt.tight_layout()
plt.savefig('./output/figure/L3_T12_SMA_MF.png',dpi=600)
plt.clf()

# calculate r2 and p-value for both gender
R2_and_p_value = ss.pearsonr(S_3,S_12)
(r,p) = R2_and_p_value
r2, p2 = format(r, '.4f') , format(p, '.4f')
text = '( {} = {}, p-value = {})'.format('${r^2}$',r2,p2).replace('= 0.0000','< 0.0001')

# regression plot
sn.regplot(x=S_3, y=S_12, color="#2040BB", line_kws={"color":"#2040BB","alpha":0.9,"lw":5})
plt.text(3500,11700, text, fontdict={'size':14,'color':'#2040BB'})

# label and save
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('L3 SMA ($\mathregular{mm^2}$)', fontdict={'size': 14})
plt.ylabel('T12 SMA ($\mathregular{mm^2}$)', fontdict={'size': 14})
plt.tight_layout()
plt.savefig('./output/figure/L3_T12_SMA.png',dpi=600)
plt.clf()



## MHU L3_T4
# calculate r2 and p-value for male
R2_and_p_value = ss.pearsonr(M_3_M,M_4_M)
(r,p) = R2_and_p_value
r2, p2 = format(r, '.4f') , format(p, '.4f')
text1 = '( {} = {}, p-value = {})'.format('${r^2}$',r2,p2).replace('= 0.0000','< 0.0001')

# calculate r2 and p-value for female
R2_and_p_value = ss.pearsonr(M_3_F,M_4_F)
(r,p) = R2_and_p_value
r2, p2 = format(r, '.4f') , format(p, '.4f')
text2 = '( {} = {}, p-value = {})'.format('${r^2}$',r2,p2).replace('= 0.0000','< 0.0001')

# regression plot
sn.regplot(x=M_3_M, y=M_4_M, color="#2040BB", line_kws={"color":"#2040BB","alpha":0.9,"lw":5}) #, ax=ax1
plt.text(13,65, text1, fontdict={'size':14,'color':'#2040BB'})

sn.regplot(x=M_3_F, y=M_4_F, color="#FF7026", line_kws={"color":"#FF7026","alpha":0.9,"lw":5})
plt.text(13,61.5, text2, fontdict={'size':14,'color':'#FF7026'})

# label and save
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('Mean HU (L3)', fontdict={'size': 14})
plt.ylabel('Mean HU (Pectoralis)', fontdict={'size': 14})
plt.tight_layout()
plt.savefig('./output/figure/L3_T4_MHU_MF.png',dpi=600)
plt.clf()

# calculate r2 and p-value for both gender
R2_and_p_value = ss.pearsonr(M_3,M_4)
(r,p) = R2_and_p_value
r2, p2 = format(r, '.4f') , format(p, '.4f')
text = '( {} = {}, p-value = {})'.format('${r^2}$',r2,p2).replace('= 0.0000','< 0.0001')

# regression plot
sn.regplot(x=M_3, y=M_4, color="#2040BB", line_kws={"color":"#2040BB","alpha":0.9,"lw":5})
plt.text(13,65, text, fontdict={'size':14,'color':'#2040BB'})

# label and save
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('Mean HU (L3)', fontdict={'size': 14})
plt.ylabel('Mean HU (Pectoralis)', fontdict={'size': 14})
plt.tight_layout()
plt.savefig('./output/figure/L3_T4_MHU.png',dpi=600)
plt.clf()



## SMA L3_T4
# calculate r2 and p-value for male
R2_and_p_value = ss.pearsonr(S_3_M,S_4_M)
(r,p) = R2_and_p_value
r2, p2 = format(r, '.4f') , format(p, '.4f')
text1 = '( {} = {}, p-value = {})'.format('${r^2}$',r2,p2).replace('= 0.0000','< 0.0001')

# calculate r2 and p-value for female
R2_and_p_value = ss.pearsonr(S_3_F,S_4_F)
(r,p) = R2_and_p_value
r2, p2 = format(r, '.4f') , format(p, '.4f')
text2 = '( {} = {}, p-value = {})'.format('${r^2}$',r2,p2).replace('= 0.0000','< 0.0001')

# regression plot
sn.regplot(x=S_3_M, y=S_4_M, color="#2040BB", line_kws={"color":"#2040BB","alpha":0.9,"lw":5})
plt.text(3500,6550, text1, fontdict={'size':14,'color':'#2040BB'})

sn.regplot(x=S_3_F, y=S_4_F, color="#FF7026", line_kws={"color":"#FF7026","alpha":0.9,"lw":5})
plt.text(3500,6150, text2, fontdict={'size':14,'color':'#FF7026'})

# label and save
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('L3 SMA ($\mathregular{mm^2}$)', fontdict={'size': 14})
plt.ylabel('Pectoralis muscle area ($\mathregular{mm^2}$)', fontdict={'size': 14})
plt.tight_layout()
plt.savefig('./output/figure/L3_T4_SMA_MF.png',dpi=600)
plt.clf()

# calculate r2 and p-value for both gender
R2_and_p_value = ss.pearsonr(S_3,S_4)
(r,p) = R2_and_p_value
r2, p2 = format(r, '.4f') , format(p, '.4f')
text = '( {} = {}, p-value = {})'.format('${r^2}$',r2,p2).replace('= 0.0000','< 0.0001')

# regression plot
sn.regplot(x=S_3, y=S_4, color="#2040BB", line_kws={"color":"#2040BB","alpha":0.9,"lw":5})
plt.text(3500,6550, text, fontdict={'size':14,'color':'#2040BB'})

# label and save
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('L3 SMA ($\mathregular{mm^2}$)', fontdict={'size': 14})
plt.ylabel('Pectoralis muscle area ($\mathregular{mm^2}$)', fontdict={'size': 14})
plt.tight_layout()
plt.savefig('./output/figure/L3_T4_SMA.png',dpi=600)
plt.clf()



## MHU L3_Major
# calculate r2 and p-value for male
R2_and_p_value = ss.pearsonr(M_3_M,M_Major_M)
(r,p) = R2_and_p_value
r2, p2 = format(r, '.4f') , format(p, '.4f')
text1 = '( {} = {}, p-value = {})'.format('${r^2}$',r2,p2).replace('= 0.0000','< 0.0001')

# calculate r2 and p-value for female
R2_and_p_value = ss.pearsonr(M_3_F,M_Major_F)
(r,p) = R2_and_p_value
r2, p2 = format(r, '.4f') , format(p, '.4f')
text2 = '( {} = {}, p-value = {})'.format('${r^2}$',r2,p2).replace('= 0.0000','< 0.0001')

# regression plot
sn.set_theme()
sn.regplot(x=M_3_M, y=M_Major_M, color="#2040BB", line_kws={"color":"#2040BB","alpha":0.9,"lw":5}) #, ax=ax1
plt.text(13,65.5, text1, fontdict={'size':14,'color':'#2040BB'})

sn.regplot(x=M_3_F, y=M_Major_F, color="#FF7026", line_kws={"color":"#FF7026","alpha":0.9,"lw":5})
plt.text(13,62.5, text2, fontdict={'size':14,'color':'#FF7026'})

# label and save
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('Mean HU (L3)', fontdict={'size': 14})
plt.ylabel('Mean HU (Pectoralis major)', fontdict={'size': 14})
plt.tight_layout()
plt.savefig('./output/figure/L3_Major_MHU_MF.png',dpi=600)
plt.clf()

# calculate r2 and p-value for both gender
R2_and_p_value = ss.pearsonr(M_3,M_Major)
(r,p) = R2_and_p_value
r2, p2 = format(r, '.4f') , format(p, '.4f')
text = '( {} = {}, p-value = {})'.format('${r^2}$',r2,p2).replace('= 0.0000','< 0.0001')

# regression plot

sn.regplot(x=M_3, y=M_Major, color="#2040BB", line_kws={"color":"#2040BB","alpha":0.9,"lw":5})
plt.text(13,65.5, text, fontdict={'size':14,'color':"#2040BB"})

# label and save
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('Mean HU (L3)', fontdict={'size': 14})
plt.ylabel('Mean HU (Pectoralis major)', fontdict={'size': 14})
plt.tight_layout()
plt.savefig('./output/figure/L3_Major_MHU.png',dpi=600)
plt.clf()



## SMA L3_Major
# calculate r2 and p-value for male
R2_and_p_value = ss.pearsonr(S_3_M,S_Major_M)
(r,p) = R2_and_p_value
r2, p2 = format(r, '.4f') , format(p, '.4f')
text1 = '( {} = {}, p-value = {})'.format('${r^2}$',r2,p2).replace('= 0.0000','< 0.0001')

# calculate r2 and p-value for female
R2_and_p_value = ss.pearsonr(S_3_F,S_Major_F)
(r,p) = R2_and_p_value
r2, p2 = format(r, '.4f') , format(p, '.4f')
text2 = '( {} = {}, p-value = {})'.format('${r^2}$',r2,p2).replace('= 0.0000','< 0.0001')

# regression plot
sn.regplot(x=S_3_M, y=S_Major_M, color="#2040BB", line_kws={"color":"#2040BB","alpha":0.9,"lw":5})
plt.text(3600,5100, text1, fontdict={'size':14,'color':'#2040BB'})

sn.regplot(x=S_3_F, y=S_Major_F, color="#FF7026", line_kws={"color":"#FF7026","alpha":0.9,"lw":5})
plt.text(3600,4775, text2, fontdict={'size':14,'color':'#FF7026'})

# label and save
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('L3 muscle area ($\mathregular{mm^2}$)', fontdict={'size': 14})
plt.ylabel('Pectoralis major muscle area ($\mathregular{mm^2}$)', fontdict={'size': 14})
plt.tight_layout()
plt.savefig('./output/figure/L3_Major_SMA_MF.png',dpi=600)
plt.clf()

# calculate r2 and p-value for both gender
R2_and_p_value = ss.pearsonr(S_3,S_Major)
(r,p) = R2_and_p_value
r2, p2 = format(r, '.4f') , format(p, '.4f')
text = '( {} = {}, p-value = {})'.format('${r^2}$',r2,p2).replace('= 0.0000','< 0.0001')

# regression plot
sn.regplot(x=S_3, y=S_Major, color="#2040BB", line_kws={"color":"#2040BB","alpha":0.9,"lw":5})
plt.text(3600,5100, text, fontdict={'size':14,'color':'#2040BB'})

# label and save
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('L3 muscle area ($\mathregular{mm^2}$)', fontdict={'size': 14})
plt.ylabel('Pectoralis major muscle area ($\mathregular{mm^2}$)', fontdict={'size': 14})
plt.tight_layout()
plt.savefig('./output/figure/L3_Major_SMA.png',dpi=600)
plt.clf()



## MHU L3_Minor
# calculate r2 and p-value for male
R2_and_p_value = ss.pearsonr(M_3_M,M_Minor_M)
(r,p) = R2_and_p_value
r2, p2 = format(r, '.4f') , format(p, '.4f')
text1 = '( {} = {}, p-value = {})'.format('${r^2}$',r2,p2).replace('= 0.0000','< 0.0001')

# calculate r2 and p-value for female
R2_and_p_value = ss.pearsonr(M_3_F,M_Minor_F)
(r,p) = R2_and_p_value
r2, p2 = format(r, '.4f') , format(p, '.4f')
text2 = '( {} = {}, p-value = {})'.format('${r^2}$',r2,p2).replace('= 0.0000','< 0.0001')

# regression plot
sn.regplot(x=M_3_M, y=M_Minor_M, color="#2040BB", line_kws={"color":"#2040BB","alpha":0.9,"lw":5}) #, ax=ax1
plt.text(13,64.5, text1, fontdict={'size':14,'color':'#2040BB'})

sn.regplot(x=M_3_F, y=M_Minor_F, color="#FF7026", line_kws={"color":"#FF7026","alpha":0.9,"lw":5})
plt.text(13,61.5, text2, fontdict={'size':14,'color':'#FF7026'})

# label and save
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('Mean HU (L3)', fontdict={'size': 14})
plt.ylabel('Mean HU (Pectoralis minor)', fontdict={'size': 14})
plt.tight_layout()
plt.savefig('./output/figure/L3_Minor_MHU_MF.png',dpi=600)
plt.clf()

# calculate r2 and p-value for both gender
R2_and_p_value = ss.pearsonr(M_3,M_Minor)
(r,p) = R2_and_p_value
r2, p2 = format(r, '.4f') , format(p, '.4f')
text = '( {} = {}, p-value = {})'.format('${r^2}$',r2,p2).replace('= 0.0000','< 0.0001')

# regression plot
sn.regplot(x=M_3, y=M_Minor, color="#2040BB", line_kws={"color":"#2040BB","alpha":0.9,"lw":5})
plt.text(13,64.5, text, fontdict={'size':14,'color':'#2040BB'})

# label and save
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('Mean HU (L3)', fontdict={'size': 14})
plt.ylabel('Mean HU (Pectoralis minor)', fontdict={'size': 14})
plt.tight_layout()
plt.savefig('./output/figure/L3_Minor_MHU.png',dpi=600)
plt.clf()



## SMA L3_Minor
# calculate r2 and p-value for male
R2_and_p_value = ss.pearsonr(S_3_M,S_Minor_M)
(r,p) = R2_and_p_value
r2, p2 = format(r, '.4f') , format(p, '.4f')
text1 = '( {} = {}, p-value = {})'.format('${r^2}$',r2,p2).replace('= 0.0000','< 0.0001')

# calculate r2 and p-value for female
R2_and_p_value = ss.pearsonr(S_3_F,S_Minor_F)
(r,p) = R2_and_p_value
r2, p2 = format(r, '.4f') , format(p, '.4f')
text2 = '( {} = {}, p-value = {})'.format('${r^2}$',r2,p2).replace('= 0.0000','< 0.0001')

# regression plot
sn.regplot(x=S_3_M, y=S_Minor_M, color="#2040BB", line_kws={"color":"#2040BB","alpha":0.9,"lw":5})
plt.text(3600,1670, text1, fontdict={'size':14,'color':'#2040BB'})

sn.regplot(x=S_3_F, y=S_Minor_F, color="#FF7026", line_kws={"color":"#FF7026","alpha":0.9,"lw":5})
plt.text(3600,1570, text2, fontdict={'size':14,'color':'#FF7026'})

# label and save
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('L3 muscle area ($\mathregular{mm^2}$)', fontdict={'size': 14})
plt.ylabel('Pectoralis minor muscle area ($\mathregular{mm^2}$)', fontdict={'size': 14})
plt.tight_layout()
plt.savefig('./output/figure/L3_Minor_SMA_MF.png',dpi=600)
plt.clf()

# calculate r2 and p-value for both gender
R2_and_p_value = ss.pearsonr(S_3,S_Minor)
(r,p) = R2_and_p_value
r2, p2 = format(r, '.4f') , format(p, '.4f')
text = '( {} = {}, p-value = {})'.format('${r^2}$',r2,p2).replace('= 0.0000','< 0.0001')

# regression plot
sn.regplot(x=S_3, y=S_Minor, color="#2040BB", line_kws={"color":"#2040BB","alpha":0.9,"lw":5})
plt.text(3600,1670, text, fontdict={'size':14,'color':'#2040BB'})

# label and save
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('L3 muscle area ($\mathregular{mm^2}$)', fontdict={'size': 14})
plt.ylabel('Pectoralis minor muscle area ($\mathregular{mm^2}$)', fontdict={'size': 14})
plt.tight_layout()
plt.savefig('./output/figure/L3_Minor_SMA.png',dpi=600)
plt.clf()
