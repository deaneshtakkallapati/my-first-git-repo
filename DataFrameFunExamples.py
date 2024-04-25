import pandas as pd

try:
    df = pd.read_csv('DataFrameFun.csv')
    sliced_rows = df.iloc[:1, 0:2]
    print(sliced_rows)
    print("----------------------------")
    sliced_rows_1 = df.loc[:1, df.columns[0:2]]
    print(sliced_rows_1)
    print("----------------------------")
    sliced_rows_1 = df.loc[(df.country == 'France') ]
    print(sliced_rows_1)
    print("----------------------------")
    sliced_rows_1 = df.loc[(df.country == 'France') & (df.variety == 'Pinot Gris')]
    print(sliced_rows_1)
    print("----------------------------")
    sliced_rows_1 = df.loc[(df.country == 'France') | (df.variety == 'Pinot Gris')]
    print(sliced_rows_1)
    print("----------------------------")
    sliced_rows_1 = df.loc[(df.country.isin(['India', 'France'])) ]
    print(sliced_rows_1)
    print("----------------------------")
    sliced_rows_1 = df.loc[df.price.notnull()]
    print(sliced_rows_1)
    print("----------------------------")
    sliced_rows_1 = df.loc[df.price.isnull()]
    print(sliced_rows_1)
    print("----------------------------")
    indexes = [0,1]
    cols = ['Country'.lower(), 'Price'.lower()]
    sliced_rows_1 = df.loc[indexes, cols]
    print(sliced_rows_1)
    print("----------------------------")
    df = pd.read_csv('wines.csv')
    top_oceania_wines = df.loc[(df.points >= 95) & (df.country.isin(['Germany']))]
    print(top_oceania_wines)
except Exception as ex:
    print("exception encountered "+ str(ex))




'''

csv_files_list = ['DataFrameFun.csv']
for i in csv_files_list:
    df = pd.read_csv(i)
    sub_df = df['country'][0]
    print(sub_df)

# Write CSV from DataFrame
my_df = pd.DataFrame([[12,23], [13,24]], columns=['Cats', 'Dogs'], index=['India', 'USA'])
my_df.to_csv('CatsAndDogs.csv')

# Read CSV
my_df = pd.read_csv('CatsAndDogs.csv')
print(my_df.head(1))

# Write CSV from Series
my_routine = ['wake up', 'brush & bath', 'tiffin', 'read & write', 'lunch', 'read & write', 'play', 'sleep']
my_timings = ['7','7.15','8','8.15', '12.30','1.15', '4', '9']
my_series = pd.Series(my_routine, index=my_timings, name='Daily Routine')
my_series.to_csv('DailyRoutine.csv')


# Read CSV
my_routine = pd.read_csv('DailyRoutine.csv')
print(my_routine)

# Both loc and iloc are row-first, column-second. 
# LOC fetches rows mentioned in range where as ILOC fetches in excluding the last one as OLD PYTHON 
try:
    df = pd.read_csv('DataFrameFun.csv')
    sliced_rows = df.iloc[:1, 0:2]
    print(sliced_rows)
    print("----------------------------")
    sliced_rows_1 = df.loc[:1, df.columns[0:2]]
    print(sliced_rows_1)
except Exception as ex:
    print("exception encountered "+ str(ex))

'''

