import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = pd.read_csv('persona.csv')

def general_information(df):
    print("_____ INFO _____")
    print(df.info(), end='\n\n')
    print("_____ DESCRIPTION _____")
    print(df.describe().T, end='\n\n')
    print("_____ SHAPE _____")
    print(df.shape,end ='\n\n')
    print("_____ MISSING _____")
    print(df.isnull().sum().sort_values(ascending=False), end='\n\n')
    print("_____ QUANTILE _____")
    print(df.quantile([0.01, 0.05, 0.10, 0.25, 0.50, 0.75, 0.90, 0.95, 0.99, 1]).T, end='\n\n')
    print("_____ UNIQUE _____")
    print(df.nunique(), end='\n\n')
    print("_____ HEAD _____")
    print(df.head(), end='\n\n')
    print("_____ TAIL _____")
    print(df.tail(), end='\n\n')
    print("_____ SAMPLE _____")
    print(df.sample(5), end='\n\n')

general_information(df)

df.SOURCE.unique()
df.SOURCE.value_counts()

df.PRICE.unique()

df.PRICE.value_counts()

df.COUNTRY.value_counts()

df.groupby('COUNTRY')['PRICE'].sum()

df.groupby('SOURCE')['PRICE'].count()

df.groupby('COUNTRY')['PRICE'].mean()

df.groupby('SOURCE')['PRICE'].mean()

df.groupby(['COUNTRY', 'SOURCE'])['PRICE'].mean()

df.groupby(['COUNTRY', 'SOURCE', 'SEX', 'AGE'])['PRICE'].mean()


agg_df = df.groupby(['COUNTRY', 'SOURCE', 'SEX', 'AGE'])['PRICE'].mean().sort_values(ascending=False)
agg_df.index

agg_df = agg_df.reset_index()

agg_df['AGE'] = pd.cut(agg_df['AGE'], bins=[0, 18, 23, 30, 40, 70], labels=['0_18', '19_23', '24_30', '31_40', '41_70'])
type(agg_df.AGE)

agg_df["customers_level_based"] = (agg_df.COUNTRY + "_" + agg_df.SOURCE + "_" + agg_df.SEX + "_" + agg_df.AGE.astype("str")).apply(lambda x: x.upper())
agg_df.customers_level_based.value_counts()
agg_df = agg_df.groupby("customers_level_based").agg({"PRICE": "mean"}).reset_index()

agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], 4, labels=["D", "C", "B", "A"])
agg_df.groupby("SEGMENT").agg({"PRICE": ["mean", "max", "sum"]})



customer1 = "TUR_ANDROID_FEMALE_31_40"
agg_df[agg_df.customers_level_based == customer1]

customer2 = "FRA_IOS_FEMALE_31_40"
agg_df[agg_df.customers_level_based == customer2]