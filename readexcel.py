import pandas as pd
df=pd.read_excel('book1.xlsx')
# print(df)
# df['json'] = df.apply(lambda x: x.to_json(), axis=1)
# df['json'] = df.to_json(orient='records', lines=True).splitlines()nn
for i in df.index:
	df.loc[i].to_json("row{}.json".format(i))

