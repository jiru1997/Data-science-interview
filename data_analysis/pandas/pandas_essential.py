#------------------------------------------------------------------------------------------------------------------------------------#
#data input
data = pandas.read_csv('path', 
	skiprows = 1,
	sep = "\t",
	header = None,
	names = ['col1', 'col2'])

data = pandas.read_excel('path')

data.head()
data.tail()
data.shape
data.columns
data.index
data.dtypes
data.set_index('col1', inplace = True)
data.reset_index()
data.drop('col1', axis = 1)
data.drop(1, axis = 0)
data.mean(axis = 0) #列数量不变，行发生改变

data.to_excel('', index = False)

#------------------------------------------------------------------------------------------------------------------------------------#
#dataframe / series
series1 = pandas.Series([1, 2]);
series1 = pandas.Series([1, 2], index = ['row1', 'row2']);
series1 = pandas.Series(dict);

series1['row1']

data = {
	'col1' : [],
	'col2' : []
}
dataframe1 = pandas.Dataframe(data)

dataframe1['col1'] 	 #col
dataframe1.loc[1:2]  #row
dataframe1.loc[:, 'col1']

dataframe1.iloc[x, y]
dataframe1.iat[x, y]

#------------------------------------------------------------------------------------------------------------------------------------#
#data search
dataframe1.loc['row1', 'col1']
dataframe1.loc['row1', ['col1', 'col2']]
dataframe1.loc['row1':'row2', 'col1']
dataframe1.loc[dataframe1['row1'] < 2, :] #返回符合条件的行的所有列
dataframe1.loc[(dataframe1['row1'] < 2) & (dataframe1['row1'] > 3), :]
dataframe1.loc[lambda rows: rows['row1'] > 1, :]

#------------------------------------------------------------------------------------------------------------------------------------#
#data modify
dataframe1.loc[:, 'col3'] = dataframe1['col1']
dataframe1.loc[:, 'col3'] = dataframe1.apply(func, axis = 1)

dataframe2 = dataframe1.assign(col4 = func)

dataframe1['col4'] = ' '
dataframe1[dataframe1['row1'] < 2, 'col'] = 1

#------------------------------------------------------------------------------------------------------------------------------------#
#method
dataframe1.describe()
dataframe1.sort_values(by = 'col1')
dataframe1['col1'].max()
dataframe1['col1'].unique()
dataframe1['col1'].value_counts(ascending=True)
dataframe1['col1'].sort_values()

#------------------------------------------------------------------------------------------------------------------------------------#
#null value
dataframe1.isnull()
dataframe1.notnull()

dataframe1.dropna(axis = 'columns', how = 'all', inplace = True)
dataframe1.dropna(axis = 'rows', how = 'all', inplace = True)

dataframe1.fillna({'col1' : 0})
dataframe1.loc[:, 'col1'] = dataframe1['col1'].fillna(0)
dataframe1.loc[:, 'col1'] = dataframe1['col1'].fillna(method = 'ffill')

#------------------------------------------------------------------------------------------------------------------------------------#
#string series.str
dataframe1['col1'].str.replace('a', '')

str.len()
str.startswith('')
str.contains('')

#------------------------------------------------------------------------------------------------------------------------------------#
#plot
import matplotlib.pyplot as plt 
%matplotlib inline

data.col.value_counts().plot(kind='line', color='maroon', figsize=(1, 2));
