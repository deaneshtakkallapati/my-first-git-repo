import datetime

import pandas as pd
import numpy as np

import pandas as pd
reviews = pd.read_csv("wines.csv", index_col=0)
# print(reviews.columns)
# print(reviews['country'].head(1))
# print(reviews.loc[reviews.country == 'Italy'].head(1))
# print(reviews.loc[(reviews.country == 'Italy') & (reviews.price > 100)].head(1))
# df = reviews.loc[reviews.iloc[:, 0] == 'Italy']
# print(reviews.iloc[0:2, 0:3])
# print(reviews.iloc[-2:-1, 0])
# print(reviews.loc[reviews.price.isin([12, 13])])
# reviews['DT'] = np.arange(len(reviews))
# print(reviews.price.mean())
# print(reviews.country.unique())
# print(reviews.country.value_counts())
# review_points_mean = reviews.points.mean()
# print(reviews.points.map(lambda p: p - review_points_mean))
# print(reviews.groupby("points").price.mean())
# print(reviews.groupby(["country", "points"]).price.mean())
# reviews_points = reviews.groupby(["country", "price"]).points.agg([len, min, max])
# index_ = reviews_points.index
# print(reviews_points.index, type(index_))
# review_points_sorted = reviews_points.sort_values(by='len', ascending=False)
# print(review_points_sorted)
# print(reviews_points.sort_index())
# print(reviews)
# df1 = reviews[pd.isnull(reviews.country)]
# print(df)
# df2 = reviews[pd.notnull(reviews.country)]

# Merge df1 and df2, indicator=True will add a column '_merge' indicating the source of each row
# merged_df = df2.merge(df1, how='left', indicator=True)
# Filter out the entries that only exist in df1
# result_df = merged_df[merged_df['_merge'] == 'left_only'].drop('_merge', axis=1)
# print(result_df)

# df1 = pd.DataFrame({"a": [1,2,3,4]}, index=[0,1,2,3])
# df2 = pd.DataFrame({"a": [1,4]}, index=[0,1])

# merged_df = df1.merge(df2, how='left', indicator=True)
# result_df = merged_df[merged_df['_merge'] == 'left_only'].drop('_merge', axis=1)
# print(result_df)

# df1_ = df1.rename(columns={"a": "AAA"})
# df1_ = df1.rename(index={0: 11})
# df1_ = df1.rename_axis("rows", axis="rows").rename_axis("cols", axis="columns")
# print(df1_)

canadian_youtube = pd.read_csv("CAvideos.csv")
british_youtube = pd.read_csv("GBvideos.csv")

res = pd.concat([canadian_youtube, british_youtube])
print(res.columns)
print(type(res))

left = canadian_youtube.set_index(["title", "trending_date"])
right = british_youtube.set_index(["title", "trending_date"])

joined_df = left.join(right, lsuffix="_CAN", rsuffix="_GB")
print(joined_df.iloc[1])










