#------------------------------------------------------------------------------------------------------------------------------------#
#data input
data = pandas.read_csv('path', 
	skip_rows = 1,
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

#------------------------------------------------------------------------------------------------------------------------------------#
#method
data.col.value_counts(ascending=True)
data.col.sort_values(ascending=True)
data.sort_values(by=[])
data[data.col == ''] 
data[data.col.str.contains('')] 

#------------------------------------------------------------------------------------------------------------------------------------#
#plot
import matplotlib.pyplot as plt 
%matplotlib inline

data.col.value_counts().plot(kind='line', color='maroon', figsize=(1, 2));
