from os import name
from lambdata_minh import helper_functions as hf
import pandas as pd

# df = pd.read_csv('data/test.csv')
data = {'column0':[1,2,3], 'column1':[1,4,7]}
df = pd.DataFrame(data, columns=['column0','column1'])
a = ['890 Jennifer Brooks\nNorth Janet, WY 24785','8394 Kim Meadow\nDarrenville, AK 27389',
'379 Cain Plaza\nJosephburgh, WY 06332 ']
b = pd.Series(a,name='address')
result_df = hf.addy_split(b)
print(result_df)
print(len(result_df))