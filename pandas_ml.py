import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(991)
df = pd.DataFrame(randn(6, 6), ['A', 'B', 'C', 'D', 'E', 'F'], ['P', 'Q', 'R', 'S', 'T', 'U'])  # dataframe creation
print(df)

print(df['P'])  # grab column P
print(df.P)
print(df[['P', 'R', 'S']])  # grab column P,R,S

print(df.loc['A'])  # grab row "A" using name of row
print(df.iloc[0])  # grab row "A" using index of row

df['V'] = df['P'] * 0  # add new column "v"
print(df)

df.drop('V', axis=1, inplace=True)  # delete column "V"
print(df)

df.drop('F', axis=0, inplace=True)
print(df)  # delete row "F"

df1 = df < 0  # create a boolean Dataframe where values>0 will be true
print(df1)
print(df[df1])  # display only true value of df regarding df1

print(df[(df['Q'] > 0) & (df['R'] < 0)])  # conditioning

df2 = df[df1]
print(df2)
print(df2.dropna())  # drops all columns and rows containing NAN
print(df2.dropna(thresh=3))  # drops all columns and rows containing more than 3 non NAN values
print('')
print(df2.dropna(thresh=3, axis=0))  # drops all  rows containing more than 3 non NAN values
print('')
print(df2.dropna(thresh=3, axis=1))  # drops all columns containing more than 3 non NAN values

print(df2.fillna(value=1))  # fills value=1 in place of NAN

print(df2.fillna(value=df['P'].mean()))  # fills NAN with mean value of column "P"
df2['P'] = df2.fillna(value=df['P'].mean())  # fills NAN in "P" column with mean of "P" column values
print(df['P'])

df0 = pd.DataFrame(randn(3, 6), ['G', 'H', 'I'], ['P', 'Q', 'R', 'S', 'T', 'U'])
print(df0)

print(pd.concat([df, df0]))  # concatination of dataframes
