import pandas as pd


try:
    df = pd.read_csv('DataFrameFun.csv')
    # print(df[pd.isnull(df.price)])
    # print(df.fillna('DT-Unknown'))
    col_names = df.columns
    # print(col_names)
    modified_col_names_df = df.rename(columns={'country': 'Country', 'points': 'Points'})
    # print(modified_col_names_df)
    modified_ind_names_df = df.rename(index={0: 'EEEE'})
    # print(modified_ind_names_df)
    modified_axis_names_df = df.rename_axis("my_rows",axis="rows").rename_axis("my_cols", axis="columns")
    print(modified_axis_names_df)

except Exception as ex:
    print("exception encountered "+ str(ex))




'''

csv_files_list = ['DataFrameFun.csv']
for i in csv_files_list:
    df = pd.read_csv(i)
    sub_df = df['country'][0]
    # print(sub_df)

# Write CSV from DataFrame
my_df = pd.DataFrame([[12,23], [13,24]], columns=['Cats', 'Dogs'], index=['India', 'USA'])
my_df.to_csv('CatsAndDogs.csv')

# Read CSV
my_df = pd.read_csv('CatsAndDogs.csv')
# print(my_df.head(1))

# Write CSV from Series
my_routine = ['wake up', 'brush & bath', 'tiffin', 'read & write', 'lunch', 'read & write', 'play', 'sleep']
my_timings = ['7','7.15','8','8.15', '12.30','1.15', '4', '9']
my_series = pd.Series(my_routine, index=my_timings, name='Daily Routine')
my_series.to_csv('DailyRoutine.csv')


# Read CSV
my_routine = pd.read_csv('DailyRoutine.csv')
# print(my_routine)

# Both loc and iloc are row-first, column-second. 
# LOC fetches rows mentioned in range where as ILOC fetches in excluding the last one as OLD PYTHON 
try:
    df = pd.read_csv('DataFrameFun.csv')
    sliced_rows = df.iloc[:1, 0:2]
    # print(sliced_rows)
    # print("----------------------------")
    sliced_rows_1 = df.loc[:1, df.columns[0:2]]
    # print(sliced_rows_1)
except Exception as ex:
    # print("exception encountered "+ str(ex))
    
try:
    df = pd.read_csv('DataFrameFun.csv')
    sliced_rows = df.iloc[:1, 0:2]
    # print(sliced_rows)
    # print("----------------------------")
    sliced_rows_1 = df.loc[:1, df.columns[0:2]]
    # print(sliced_rows_1)
    # print("----------------------------")
    sliced_rows_1 = df.loc[(df.country == 'France') ]
    # print(sliced_rows_1)
    # print("----------------------------")
    sliced_rows_1 = df.loc[(df.country == 'France') & (df.variety == 'Pinot Gris')]
    # print(sliced_rows_1)
    # print("----------------------------")
    sliced_rows_1 = df.loc[(df.country == 'France') | (df.variety == 'Pinot Gris')]
    # print(sliced_rows_1)
    # print("----------------------------")
    sliced_rows_1 = df.loc[(df.country.isin(['India', 'France'])) ]
    # print(sliced_rows_1)
    # print("----------------------------")
    sliced_rows_1 = df.loc[df.price.notnull()]
    # print(sliced_rows_1)
    # print("----------------------------")
    sliced_rows_1 = df.loc[df.price.isnull()]
    # print(sliced_rows_1)
    # print("----------------------------")
    indexes = [0,1]
    cols = ['Country'.lower(), 'Price'.lower()]
    sliced_rows_1 = df.loc[indexes, cols]
    # print(sliced_rows_1)
    # print("----------------------------")
    df = pd.read_csv('wines.csv')
    top_oceania_wines = df.loc[(df.points >= 95) & (df.country.isin(['Germany']))]
    # print(top_oceania_wines)
except Exception as ex:
    # print("exception encountered "+ str(ex))

try:
    df = pd.read_csv('DataFrameFun.csv')
    # print(df.price.describe().index)
    # print("----------------------------")
    # print(df.price.mean())
    # print("----------------------------")
    # print(df.country)
    # print("----------------------------")
    # print(df.country.unique())
    # print("----------------------------")
    # print(df.country.value_counts())
    # print("----------------------------")
    df_price_mean = df.price.mean()
    my_df_map = df.price.map(lambda p: p - df_price_mean)
    # print(my_df_map)
    # print("----------------------------")
    df = pd.read_csv('wines.csv')
    bargain_idx = (df.points / df.price).idxmax()
    bargain_wine = df.loc[bargain_idx, 'title']
    # print(bargain_wine)
    # print("----------------------------")
    tropical = df.description.map(lambda desc: 'tropical' in desc).sum()
    fruity = df.description.map(lambda d: 'fruity' in d).sum()
    is_ = df.description.map(lambda d: 'is' in d).sum()
    descriptor_counts = pd.Series([tropical, fruity, is_], index=['tropical', 'fruity', 'is'])
    # print(descriptor_counts)
    print("----------------------------")
    country_group = df.groupby(['country']).price.agg([len, min, max])
    # print(country_group)
    print("----------------------------")
    country_group = df.groupby(['country', 'points', 'province']).price.min()
    # print(country_group)
    countries_reviewed = df.groupby(['country', 'province']).description.agg([len])
    # print(countries_reviewed)
    a = countries_reviewed.sort_values(by='len', ascending=False)
    print(a)
    countries_reviewed = countries_reviewed.reset_index()
    a = countries_reviewed.sort_values(by='len')
    print(a)
except Exception as ex:
    print("exception encountered "+ str(ex))
'''

