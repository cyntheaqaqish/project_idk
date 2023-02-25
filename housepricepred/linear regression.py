import pandas as pd
# import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
# from sklearn.model_selection import LinearRegression

df = pd.read_csv('kc_house_data.csv')
df = df[["price", "bedrooms", "bathrooms", "sqft_living", "sqft_lot", "floors", "waterfront"]]

# df.info()
# print(df.describe())
# df['bedrooms'].hist()
# plt.show()

# print(df[["sqft_living"]].describe())
# df['bedrooms'].hist()
# plt.show()
mixMAx = MinMaxScaler()

price = df[['price']] / 10000

beds = df['bedrooms'].values.reshape(-1, 1)
df['bedrooms'] = mixMAx.fit_transform(beds)

sqft_living = df['sqft_living'].values.reshape(-1, 1)
df['sqft_living'] =  mixMAx.fit_transform(sqft_living)

sqft_lot = df['sqft_lot'].values.reshape(-1, 1)
df['sqft_lot'] =  mixMAx.fit_transform(sqft_lot)

# print(df[["sqft_living"]].describe())
# print(df[["price"]].describe())
train, test = train_test_split(df, test_size=0.15)
train = pd.DataFrame(train)

x_train = train.drop(columns="price", axis=1)
y_train = train("price")
model =