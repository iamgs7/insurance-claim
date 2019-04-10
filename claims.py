import pandas as pd
import numpy as np
import re
import seaborn as sns
import matplotlib.pyplot as plt

# read excel workbook
xl = pd.read_excel('data.xls', sheet_name=None)
# print existing worksheets
#print(xl.keys())
# investigate 5 top rows to get an intuitation about the data
xl['claims'].head()

# print column names for easy access
#print(xl['claims'].columns)

# choose features and assign them to variable 'data' as pandas dataframe
data = xl['claims'][['KIDSDRIV', 'TRAVTIME', 'CAR_USE', 'MVR_PTS', 'BLUEBOOK', 'RETAINED', 'NPOLICY', 'CAR_TYPE', 'AGE', 'INCOME', 'GENDER', 'MARRIED', 'MAX_EDUC', 'DENSITY', 'CLM_FREQ']]

#print(data.head())

data = data.dropna()

# transform 'object' data type to 'category'

data['CAR_USE'] = data['CAR_USE'].astype('category')
data['CAR_TYPE'] = data['CAR_TYPE'].astype('category')
data['AGE'] = data['AGE'].astype('category')
data['GENDER'] = data['GENDER'].astype('category')
data['MARRIED'] = data['MARRIED'].astype('category')
data['MAX_EDUC'] = data['MAX_EDUC'].astype('category')
data['DENSITY'] = data['DENSITY'].astype('category')
cat_columns = data.select_dtypes(['category']).columns

# remove '$' sign 
data['BLUEBOOK'] = data['BLUEBOOK'].apply(lambda x: re.findall('\d+', x)[0])
data['INCOME'] = data['INCOME'].apply(lambda x: re.findall('\d+', x)[0])
# change datatype to 'integer'
data['BLUEBOOK'] = data['BLUEBOOK'].astype(int)
data['INCOME'] = data['INCOME'].astype(int)


print(data['CLM_FREQ'].value_counts())
sns.countplot(x='CLM_FREQ', data=data, palette='hls')
plt.show()
print("mean = " + str(data['CLM_FREQ'].mean()))
print("variance = " + str(data['CLM_FREQ'].var()))

