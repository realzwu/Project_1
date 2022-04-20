

import pandas as pd

# read sarcopenia_database
df_all = pd.read_excel('./xlsx_csv/WithStagingWeights.xlsx', index_col=0, header=0)

# read sma mhu
df_sma = pd.read_excel('./xlsx_csv/MHU_SMA.xlsx', index_col=0, header=0)
df_sma = df_sma.T

# inner join through index (patient's id)
df_merge = pd.merge(left=df_all,right=df_sma,how='inner',left_index=True,right_index=True)

# del useless attributes
df_merge.drop(['Date of Birth','Date of Diagnostic CT'],axis=1,inplace=True)

# select male and female subclass
df_male = df_merge[df_merge.Gender.isin(['Male'])]
df_female = df_merge[df_merge.Gender.isin(['Female'])]

#save
df_merge.to_csv("df_merge.csv")
df_male.to_csv("df_male.csv")
df_female.to_csv("df_female.csv")