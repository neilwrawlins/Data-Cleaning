import pandas as pd
import numpy as np

#VALUES THAT ARE IN THE CSV FILE. ONLY 'NA' IS RECOGNIZED AT FIRST.
missing_values = ["n/a", "na", "--"]

df = pd.read_csv("/Users/neilrawlins/Desktop/Real Estate Data.csv", na_values = missing_values)

count = 0

#SINCE THERE IS A NUMBER IN THE OWN_OCCUPIED COLUMN, WE ARE CHANGING IT TO N/A VALUE
for row in df['OWN_OCCUPIED']:
    try:
        int(row)
        df.loc[count, 'OWN_OCCUPIED'] = np.nan
    except ValueError:
        pass
    count += 1

#FILLING ALL N/A VALUES
df.fillna(125, inplace=True)

#OR FILLING ONE N/A VALUE AT INDEX 2
df.loc[2, 'ST_NUM'] = 125

#FILLING N/A BEDROOMS WITH A MEDIAN VALUE OF ALL BEDROOMS
median = df['NUM_BEDROOMS'].median()
df['NUM_BEDROOMS'].fillna(median, inplace=True)