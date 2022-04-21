
import pandas as pd
from lifelines.utils import to_episodic_format
from lifelines import CoxTimeVaryingFitter

#  Read csv
df_cox11 = pd.read_csv(r"./xlsx_csv/df_BMI_male.csv",index_col=0, header=0)
df_cox12 = pd.read_csv(r"./xlsx_csv/df_univariate_others_male.csv",index_col=0, header=0)
df_cox21 = pd.read_csv(r"./xlsx_csv/df_BMI_female.csv",index_col=0, header=0)
df_cox22 = pd.read_csv(r"./xlsx_csv/df_univariate_others_female.csv",index_col=0, header=0)


#  sarcopenia cut-off
for i,v in df_cox11['SMI'].items():
    if v < 38.7:
        df_cox11.loc[i, ('SMI')] = 1.
    else:
        df_cox11.loc[i, ('SMI')] = 0.

for i,v in df_cox21['SMI'].items():
    if v < 27.8:
        df_cox21.loc[i, ('SMI')] = 1.
    else:
        df_cox21.loc[i, ('SMI')] = 0.

ctv = CoxTimeVaryingFitter()

##  select subgroups
df_cox12_Age = pd.concat([df_cox12['Age'],df_cox12['Death within 3 years'],df_cox12['Survival Time (up to 3 years)']],axis=1)
df_cox12_Race = pd.concat([df_cox12['Ethnicity'],df_cox12['Death within 3 years'],df_cox12['Survival Time (up to 3 years)']],axis=1)
df_cox12_Histology = pd.concat([df_cox12['Histology Class'],df_cox12['Death within 3 years'],df_cox12['Survival Time (up to 3 years)']],axis=1)
df_cox12_Performance = pd.concat([df_cox12['Performance Status'],df_cox12['Death within 3 years'],df_cox12['Survival Time (up to 3 years)']],axis=1)
df_cox12_Stage = pd.concat([df_cox12['Stage Grouping - Numeral'],df_cox12['Death within 3 years'],df_cox12['Survival Time (up to 3 years)']],axis=1)
df_cox12_SMA = pd.concat([df_cox12['AA'],df_cox12['Death within 3 years'],df_cox12['Survival Time (up to 3 years)']],axis=1)
df_cox12_MHU = pd.concat([df_cox12['HU'],df_cox12['Death within 3 years'],df_cox12['Survival Time (up to 3 years)']],axis=1)

df_cox11_BMI = pd.concat([df_cox11['BMI'],df_cox11['Death within 3 years'],df_cox11['Survival Time (up to 3 years)']],axis=1)
df_cox11_SMI = pd.concat([df_cox11['SMI'],df_cox11['Death within 3 years'],df_cox11['Survival Time (up to 3 years)']],axis=1)

df_cox22_Age = pd.concat([df_cox22['Age'],df_cox22['Death within 3 years'],df_cox22['Survival Time (up to 3 years)']],axis=1)
df_cox22_Race = pd.concat([df_cox22['Ethnicity'],df_cox22['Death within 3 years'],df_cox22['Survival Time (up to 3 years)']],axis=1)
df_cox22_Histology = pd.concat([df_cox22['Histology Class'],df_cox22['Death within 3 years'],df_cox22['Survival Time (up to 3 years)']],axis=1)
df_cox22_Performance = pd.concat([df_cox22['Performance Status'],df_cox22['Death within 3 years'],df_cox22['Survival Time (up to 3 years)']],axis=1)
df_cox22_Stage = pd.concat([df_cox22['Stage Grouping - Numeral'],df_cox22['Death within 3 years'],df_cox22['Survival Time (up to 3 years)']],axis=1)
df_cox22_SMA = pd.concat([df_cox22['AA'],df_cox22['Death within 3 years'],df_cox22['Survival Time (up to 3 years)']],axis=1)
df_cox22_MHU = pd.concat([df_cox22['HU'],df_cox22['Death within 3 years'],df_cox22['Survival Time (up to 3 years)']],axis=1)

df_cox21_BMI = pd.concat([df_cox21['BMI'],df_cox21['Death within 3 years'],df_cox21['Survival Time (up to 3 years)']],axis=1)
df_cox21_SMI = pd.concat([df_cox21['SMI'],df_cox21['Death within 3 years'],df_cox21['Survival Time (up to 3 years)']],axis=1)

##  processing string & numeral data
for i,v in df_cox12_Race['Ethnicity'].items():
        if v.find('White') == 0:
            df_cox12_Race.loc[i, ('Ethnicity')] = 1
        elif v.find('Not') == 0:
            df_cox12_Race.drop([i], axis=0, inplace=True)
        else:
            df_cox12_Race.loc[i, ('Ethnicity')] = 0

for i,v in df_cox22_Race['Ethnicity'].items():
    if isinstance(v,str) is True:
        if v.find('White') == 0:
            df_cox22_Race.loc[i, ('Ethnicity')] = 1.
        elif v.find('Not') == 0:
            df_cox22_Race.drop([i], axis=0, inplace=True)
        else:
            df_cox22_Race.loc[i, ('Ethnicity')] = 0.

for i,v in df_cox12_Histology['Histology Class'].items():
    if v.find('Adenocarcinoma') == 0:
        df_cox12_Histology.loc[i, ('Histology Class')] = 1.
    elif v.find('Squamous cell carcinoma') == 0:
        df_cox12_Histology.loc[i, ('Histology Class')] = 0.
    else:
        df_cox12_Histology.drop([i], axis=0, inplace=True)

for i,v in df_cox22_Histology['Histology Class'].items():
    if v.find('Adenocarcinoma') == 0:
        df_cox22_Histology.loc[i, ('Histology Class')] = 1.
    elif v.find('Squamous cell carcinoma') == 0:
        df_cox22_Histology.loc[i, ('Histology Class')] = 0.
    else:
        df_cox22_Histology.drop([i], axis=0, inplace=True)


for i,v in df_cox12_Stage['Stage Grouping - Numeral'].items():
    if v == 'IV':
        df_cox12_Stage.loc[i,('Stage Grouping - Numeral')] = 4
    elif v == 'II':
        df_cox12_Stage.loc[i,('Stage Grouping - Numeral')] = 2
    elif v == 'III':
        df_cox12_Stage.loc[i,('Stage Grouping - Numeral')] = 3
    elif v == 'I':
        df_cox12_Stage.loc[i,('Stage Grouping - Numeral')] = 1
    else:
        df_cox12_Stage.drop([i] , axis=0 , inplace=True)

for i,v in df_cox22_Stage['Stage Grouping - Numeral'].items():
    if v == 'IV':
        df_cox22_Stage.loc[i,('Stage Grouping - Numeral')] = 4
    elif v == 'II':
        df_cox22_Stage.loc[i,('Stage Grouping - Numeral')] = 2
    elif v == 'III':
        df_cox22_Stage.loc[i,('Stage Grouping - Numeral')] = 3
    elif v == 'I':
        df_cox22_Stage.loc[i,('Stage Grouping - Numeral')] = 1
    else:
        df_cox22_Stage.drop([i] , axis=0 , inplace=True)


for i,v in df_cox12_Performance['Performance Status'].items():
    if 0 <= v <= 4:
        pass
    else:
        df_cox12_Performance.drop([i], axis=0, inplace=True)

for i,v in df_cox22_Performance['Performance Status'].items():
    if 0 <= v <= 4:
        pass
    else:
        df_cox22_Performance.drop([i], axis=0, inplace=True)

# TimeVarying Cox Regression for male

df_long12_Age = to_episodic_format(df_cox12_Age, duration_col='Survival Time (up to 3 years)', event_col='Death within 3 years', time_gaps=5.)
df_long12_Race = to_episodic_format(df_cox12_Race, duration_col='Survival Time (up to 3 years)', event_col='Death within 3 years', time_gaps=5.)
df_long12_Histology = to_episodic_format(df_cox12_Histology, duration_col='Survival Time (up to 3 years)', event_col='Death within 3 years', time_gaps=5.)
df_long12_Performance = to_episodic_format(df_cox12_Performance, duration_col='Survival Time (up to 3 years)', event_col='Death within 3 years', time_gaps=5.)
df_long12_Stage = to_episodic_format(df_cox12_Stage, duration_col='Survival Time (up to 3 years)', event_col='Death within 3 years', time_gaps=5.)
df_long12_SMA = to_episodic_format(df_cox12_SMA, duration_col='Survival Time (up to 3 years)', event_col='Death within 3 years', time_gaps=5.)
df_long12_MHU = to_episodic_format(df_cox12_MHU, duration_col='Survival Time (up to 3 years)', event_col='Death within 3 years', time_gaps=5.)

df_long11_BMI = to_episodic_format(df_cox11_BMI, duration_col='Survival Time (up to 3 years)', event_col='Death within 3 years', time_gaps=5.)
df_long11_SMI = to_episodic_format(df_cox11_SMI, duration_col='Survival Time (up to 3 years)', event_col='Death within 3 years', time_gaps=5.)


ctv.fit(df_long12_Age,id_col='id',event_col='Death within 3 years',start_col='start',stop_col='stop')
ctv.print_summary(3)

df_long12_Race.to_excel('1.xlsx')
df_long12_Race = pd.read_excel("1.xlsx",index_col=0, header=0)

ctv.fit(df_long12_Race,id_col='id',event_col='Death within 3 years',start_col='start',stop_col='stop')
ctv.print_summary(3)

df_long12_Histology.to_excel('2.xlsx')
df_long12_Histology = pd.read_excel("2.xlsx",index_col=0, header=0)

ctv.fit(df_long12_Histology,id_col='id',event_col='Death within 3 years',start_col='start',stop_col='stop')
ctv.print_summary(3)

ctv.fit(df_long12_Performance,id_col='id',event_col='Death within 3 years',start_col='start',stop_col='stop')
ctv.print_summary(3)

df_long12_Stage.to_excel('3.xlsx')
df_long12_Stage = pd.read_excel("3.xlsx",index_col=0, header=0)

ctv.fit(df_long12_Stage,id_col='id',event_col='Death within 3 years',start_col='start',stop_col='stop')
ctv.print_summary(3)

ctv.fit(df_long12_SMA,id_col='id',event_col='Death within 3 years',start_col='start',stop_col='stop')
ctv.print_summary(3)

ctv.fit(df_long12_MHU,id_col='id',event_col='Death within 3 years',start_col='start',stop_col='stop')
ctv.print_summary(3)

ctv.fit(df_long11_BMI,id_col='id',event_col='Death within 3 years',start_col='start',stop_col='stop')
ctv.print_summary(3)

ctv.fit(df_long11_SMI,id_col='id',event_col='Death within 3 years',start_col='start',stop_col='stop')
ctv.print_summary(3)


# TimeVarying Cox Regression for female

df_long22_Age = to_episodic_format(df_cox22_Age, duration_col='Survival Time (up to 3 years)', event_col='Death within 3 years', time_gaps=5.)
df_long22_Race = to_episodic_format(df_cox22_Race, duration_col='Survival Time (up to 3 years)', event_col='Death within 3 years', time_gaps=5.)
df_long22_Histology = to_episodic_format(df_cox22_Histology, duration_col='Survival Time (up to 3 years)', event_col='Death within 3 years', time_gaps=5.)
df_long22_Performance = to_episodic_format(df_cox22_Performance, duration_col='Survival Time (up to 3 years)', event_col='Death within 3 years', time_gaps=5.)
df_long22_Stage = to_episodic_format(df_cox22_Stage, duration_col='Survival Time (up to 3 years)', event_col='Death within 3 years', time_gaps=5.)
df_long22_SMA = to_episodic_format(df_cox22_SMA, duration_col='Survival Time (up to 3 years)', event_col='Death within 3 years', time_gaps=5.)
df_long22_MHU = to_episodic_format(df_cox22_MHU, duration_col='Survival Time (up to 3 years)', event_col='Death within 3 years', time_gaps=5.)

df_long21_BMI = to_episodic_format(df_cox21_BMI, duration_col='Survival Time (up to 3 years)', event_col='Death within 3 years', time_gaps=5.)
df_long21_SMI = to_episodic_format(df_cox21_SMI, duration_col='Survival Time (up to 3 years)', event_col='Death within 3 years', time_gaps=5.)

ctv.fit(df_long22_Age,id_col='id',event_col='Death within 3 years',start_col='start',stop_col='stop')
ctv.print_summary(3)

df_long22_Race.to_excel('4.xlsx')
df_long22_Race = pd.read_excel("4.xlsx",index_col=0, header=0)

ctv.fit(df_long22_Race,id_col='id',event_col='Death within 3 years',start_col='start',stop_col='stop')
ctv.print_summary(3)

df_long22_Histology.to_excel('5.xlsx')
df_long22_Histology = pd.read_excel("5.xlsx",index_col=0, header=0)

ctv.fit(df_long22_Histology,id_col='id',event_col='Death within 3 years',start_col='start',stop_col='stop')
ctv.print_summary(3)

ctv.fit(df_long22_Performance,id_col='id',event_col='Death within 3 years',start_col='start',stop_col='stop')
ctv.print_summary(3)

df_long22_Stage.to_excel('6.xlsx')
df_long22_Stage = pd.read_excel("6.xlsx",index_col=0, header=0)

ctv.fit(df_long22_Stage,id_col='id',event_col='Death within 3 years',start_col='start',stop_col='stop')
ctv.print_summary(3)

ctv.fit(df_long22_SMA,id_col='id',event_col='Death within 3 years',start_col='start',stop_col='stop')
ctv.print_summary(3)

ctv.fit(df_long22_MHU,id_col='id',event_col='Death within 3 years',start_col='start',stop_col='stop')
ctv.print_summary(3)

ctv.fit(df_long21_BMI,id_col='id',event_col='Death within 3 years',start_col='start',stop_col='stop')
ctv.print_summary(3)

ctv.fit(df_long21_SMI,id_col='id',event_col='Death within 3 years',start_col='start',stop_col='stop')
ctv.print_summary(3)






