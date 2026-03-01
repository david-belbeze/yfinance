# -*- coding: utf-8 -*-

import pandas

print("Prepare data")

df = pandas.DataFrame({
    "date": ["2026-02-20", "2026-02-21", "2026-02-22", "2026-02-23"],
    'Close': [10.0, 10.5, 10.25, 9.5],
}).set_index("date")

dividends = pandas.DataFrame({
    "date": ["2026-02-21"],
    "Dividends": [1.0],
    "currency": ["USD"], 
}).set_index("date")

print(df)
print(dividends)


print("\nConcat dividends")

dividends['Dividends'] = dividends['Dividends'].astype(str) + ' ' + dividends['currency']
dividends = dividends.drop('currency', axis=1)

print(dividends)

print("\nMerge data frames")

df = pandas.concat([df, dividends], axis=1)

print(df)
print(df.dtypes)

print("Reproduce TypeError")

df.loc[df["Dividends"].isna(), "Dividends"] = 0
