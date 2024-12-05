import pandas as pd
df = pd.read_csv("./coffee.csv")
# print(df.head(6))
# print(df.tail())
# print(df["Day"])


# print(df.loc[1:3,["Day","Units Sold" ]])
# print(df.loc[[1,5],["Day","Units Sold" ]])

# # :
# print(df.loc[:, ["Day"]])
# print(df.loc[: ,["Units Sold"]])


print(df.loc[[1,5,8],['Day',"Coffee Type"]])

