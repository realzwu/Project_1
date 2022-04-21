
import pandas as pd
from lifelines.utils import to_episodic_format
from lifelines import CoxTimeVaryingFitter

##  import data
df_cox11 = pd.read_csv(r"./xlsx_csv/df_multivariable_others_male.csv",index_col=0, header=0)
df_cox12 = pd.read_csv(r"./xlsx_csv/df_BMI_male.csv",index_col=0, header=0)
df_cox13 = pd.read_csv(r"./xlsx_csv/df_BMI_male.csv",index_col=0, header=0)

df_cox21 = pd.read_csv(r"./xlsx_csv/df_multivariable_others_female.csv",index_col=0, header=0)
df_cox22 = pd.read_csv(r"./xlsx_csv/df_BMI_female.csv",index_col=0, header=0)
df_cox23 = pd.read_csv(r"./xlsx_csv/df_BMI_female.csv",index_col=0, header=0)

##  change string to numerals
for i,v in df_cox12['SMI'].items():
    if v < 38.7:
        df_cox12.loc[i, ('SMI')] = 1.
    else:
        df_cox12.loc[i, ('SMI')] = 0.

for i,v in df_cox13['SMI'].items():
    if v < 38.7:
        df_cox13.loc[i, ('SMI')] = 1.
    else:
        df_cox13.loc[i, ('SMI')] = 0.


for i,v in df_cox22['SMI'].items():
    if v < 27.8:
        df_cox22.loc[i, ('SMI')] = 1.
    else:
        df_cox22.loc[i, ('SMI')] = 0.

for i,v in df_cox23['SMI'].items():
    if v < 27.8:
        df_cox23.loc[i, ('SMI')] = 1.
    else:
        df_cox23.loc[i, ('SMI')] = 0.

# multivariable 1
df_cox11.drop(['Gender','Height (cm)','Weight (kg)','Performance Status'],axis=1, inplace=True)
df_cox21.drop(['Gender','Height (cm)','Weight (kg)','Performance Status'],axis=1, inplace=True)

# multivariable 2
df_cox12.drop(['Gender','Height (cm)','Weight (kg)','Performance Status','BMI','AA'],axis=1, inplace=True)
df_cox22.drop(['Gender','Height (cm)','Weight (kg)','Performance Status','BMI','AA'],axis=1, inplace=True)

# multivariable 3
df_cox13.drop(['Gender','Height (cm)','Weight (kg)','Performance Status','SMI'],axis=1, inplace=True)
df_cox23.drop(['Gender','Height (cm)','Weight (kg)','Performance Status','SMI'],axis=1, inplace=True)


df_long11 = to_episodic_format(df_cox11, duration_col='Survival Time (up to 3 years)', event_col='Death within 3 years', time_gaps=5.)
df_long12 = to_episodic_format(df_cox12, duration_col='Survival Time (up to 3 years)', event_col='Death within 3 years', time_gaps=5.)
df_long13 = to_episodic_format(df_cox13, duration_col='Survival Time (up to 3 years)', event_col='Death within 3 years', time_gaps=5.)

df_long21 = to_episodic_format(df_cox21, duration_col='Survival Time (up to 3 years)', event_col='Death within 3 years', time_gaps=5.)
df_long22 = to_episodic_format(df_cox22, duration_col='Survival Time (up to 3 years)', event_col='Death within 3 years', time_gaps=5.)
df_long23 = to_episodic_format(df_cox23, duration_col='Survival Time (up to 3 years)', event_col='Death within 3 years', time_gaps=5.)

ctv = CoxTimeVaryingFitter()

# multivariate
ctv.fit(df_long11,id_col='id',event_col='Death within 3 years',start_col='start',stop_col='stop')
ctv.print_summary(3)

ctv.fit(df_long12,id_col='id',event_col='Death within 3 years',start_col='start',stop_col='stop')
ctv.print_summary(3)

ctv.fit(df_long13,id_col='id',event_col='Death within 3 years',start_col='start',stop_col='stop')
ctv.print_summary(3)

ctv.fit(df_long21,id_col='id',event_col='Death within 3 years',start_col='start',stop_col='stop')
ctv.print_summary(3)

ctv.fit(df_long22,id_col='id',event_col='Death within 3 years',start_col='start',stop_col='stop')
ctv.print_summary(3)

ctv.fit(df_long23, id_col='id', event_col='Death within 3 years', start_col='start', stop_col='stop')
ctv.print_summary(3)




