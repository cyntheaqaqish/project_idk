import pandas as pd

df = pd.read_csv('car data.csv') #dataframe
# print(df.head())
#
# print(df["Car_Name"].head()) # series
# print(df.tail())
# print(df.loc[0])
#
# dic = {
#          "column1" : [10, 20, 3000],
#         "column2" : [30, 10, 100]
# }
# df2 = pd.DataFrame(dic)
# print(df2.head(2))
# print(df.shape)
# df.info() #gives info about the data we have and if we have any missing data
# print(df.describe()) #non-null means it's not empty
#
# import matplotlib.pyplot as plt
# #df.plot() # we can add df.["Selling price"].plot() to show only the selling price on the graph
# #df["Year"].hist()
# df.plot.scatter(x="Year", y="Selling_Price")
# plt.show()
print(df[["Year", "Kms_Driven", "Fuel_Type"]].head())
df2 = df.dropna() #delete any data that is null
df2 = df.fillna() #we can add data in the parenthesis to print the data that is null
df.fillna("mohammed", inplace=True)
#df['selling_price'] = pd.to_numeric(df[])
