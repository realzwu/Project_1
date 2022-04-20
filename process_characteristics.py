
import pandas as pd


df_yuxi = pd.read_excel(r"./xlsx_csv/cox_database.xlsx",index_col=0, header=0)
df_all = pd.read_excel(r"./xlsx_csv/WithStagingWeights.xlsx",index_col=0, header=0)
print(df_yuxi)
print(30*'-')  # 503
print(df_all)
print(30*'-')  # 918

for i,v in df_yuxi['AA'].items():
    if 0 < v < 1000:
        pass
    else:
        df_yuxi.drop([i], axis=0, inplace=True)

for i,v in df_yuxi['HU'].items():
    if 0 < v < 1000:
        pass
    else:
        df_yuxi.drop([i], axis=0, inplace=True)
print(df_yuxi)
print(30*'-')  # 495

df_cox = pd.merge(left=df_yuxi,right=df_all,how='inner',left_index=True,right_index=True)
print(df_cox)
print(30*'-')  # 495

for i,v in df_yuxi['AA'].items():
    if 0 < v < 1000:
        pass
    else:
        df_yuxi.drop([i], axis=0, inplace=True)

df_yuxi.to_csv('cox_database_updated.csv')


df_cox.drop(['Date of Birth','Date of Diagnostic CT','Dead'],axis=1, inplace=True)

for i,v in df_cox['Tumour Status'].items():
    if isinstance(v,str) is True:
        if v.find('Primary') != 0:
            df_cox.drop([i], axis=0, inplace=True)
print(df_cox)  # 491
print(30*'-')


for i,v in df_cox['Survival Time (up to 3 years)'].items():
    if v == 0:
        df_cox.drop([i], axis=0, inplace=True)
print(df_cox)  # 486
print(30*'-')

# df_cox.to_excel('cox_merge.xlsx')

df_cox.drop(['Tumour Status'],axis=1, inplace=True)

for i,v in df_cox['Gender'].items():
    if isinstance(v,str) is True:
        if v.find('Male') == 0:
            df_cox.loc[i, ('Gender')] = 1.
        elif v.find('Female') == 0:
            df_cox.loc[i, ('Gender')] = 0.
        else:
            df_cox.drop([i], axis=0, inplace=True)
print(df_cox)
print(30*'-')  # 486

df_male = df_cox[df_cox.Gender.isin([1])]
print(df_male)  # 295
print(30*'-')

df_male.to_csv("df_univariable_others_male.csv")

df_female = df_cox[df_cox.Gender.isin([0])]
print(df_female)  # 191
print(30*'-')

df_female.to_csv("df_univariable_others_female.csv")

for i,v in df_cox['Ethnicity'].items():
    if isinstance(v,str) is True:
        if v.find('White') == 0:
            df_cox.loc[i, ('Ethnicity')] = 1.
        elif v.find('Not') == 0:
            df_cox.drop([i], axis=0, inplace=True)
        else:
            df_cox.loc[i, ('Ethnicity')] = 0.
print(df_cox)  # 486
print(30*'-')

for i,v in df_cox['Histology Class'].items():
    if v.find('Adenocarcinoma') == 0:
        df_cox.loc[i, ('Histology Class')] = 1.
    elif v.find('Squamous cell carcinoma') == 0:
        df_cox.loc[i, ('Histology Class')] = 0.
    else:
        df_cox.drop([i], axis=0, inplace=True)
print(df_cox)  # 284
print(30*'-')

for i,v in df_cox['Stage Grouping - Numeral'].items():
    if v == 'IV':
        df_cox.loc[i,('Stage Grouping - Numeral')] = 4
    elif v == 'II':
        df_cox.loc[i,('Stage Grouping - Numeral')] = 2
    elif v == 'III':
        df_cox.loc[i,('Stage Grouping - Numeral')] = 3
    elif v == 'I':
        df_cox.loc[i,('Stage Grouping - Numeral')] = 1
    else:
        df_cox.drop([i] , axis=0 , inplace=True)
print(df_cox)  # 276
print(30*'-')

for i,v in df_cox['Performance Status'].items():
    if 0 <= v <= 4:
        pass
    else:
        df_cox.drop([i], axis=0, inplace=True)
print(df_cox)  # 271
print(30*'-')

df_male = df_cox[df_cox.Gender.isin([1])]
print(df_male)  # 169
print(30*'-')

df_male.to_csv("df_multivariable_others_male.csv")

df_female = df_cox[df_cox.Gender.isin([0])]
print(df_female)  # 102
print(30*'-')

df_female.to_csv("df_multivariable_others_female.csv")

for i,v in df_cox['Height (cm)'].items():
    if 100 < v < 200:
        pass
    else:
        df_cox.drop([i], axis=0, inplace=True)

for i,v in df_cox['Weight (kg)'].items():
    if 20 < v < 150:
        pass
    else:
        df_cox.drop([i], axis=0, inplace=True)
print(df_cox)  # 109
print(30*'-')

df_cox['BMI'] = 10000 * df_cox['Weight (kg)']/df_cox['Height (cm)'] ** 2
df_cox['SMI'] = 10000 * df_cox['AA']/df_cox['Height (cm)'] ** 2
print(df_cox)  # 109
print(30*'-')

df_male = df_cox[df_cox.Gender.isin([1])]
print(df_male)  # 74
print(30*'-')

df_male.to_csv("df_BMI_male.csv")

df_female = df_cox[df_cox.Gender.isin([0])]
print(df_female)  # 35
print(30*'-')

df_female.to_csv("df_BMI_female.csv")

