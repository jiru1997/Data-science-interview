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
data.mean(axis = 0) #列数量不变，行发生改变, 每一个传入的参数都是一列

data.to_excel('', index = False)

#------------------------------------------------------------------------------------------------------------------------------------#
#dataframe(二维字典，column的名字作为key) / series(一维字典)
series1 = pandas.Series([1, 2]);
series1 = pandas.Series([1, 2], index = ['row1', 'row2']);
series1 = pandas.Series(dict);

series1['row1']

data = {
	'col1' : [],
	'col2' : []
}
dataframe1 = pandas.Dataframe(data)

#iloc是按照行数取值，而loc按着index名取值
dataframe1['col1'] 	 #col
dataframe1.loc[1:2]  #row
dataframe1.loc[:, 'col1']

dataframe1.iloc[x, y]
dataframe1.iloc[x:y]
dataframe1.iat[x, y]

#------------------------------------------------------------------------------------------------------------------------------------#
#data search
dataframe1.loc['row1', 'col1']
dataframe1.loc[('row1', 'row2'), :]      #多级索引
dataframe1.loc['row1', ['col1', 'col2']] #同级索引
dataframe1.loc['row1':'row2', 'col1']
dataframe1.loc[dataframe1['row1'] < 2, :] #返回符合条件的行的所有列
dataframe1.loc[(dataframe1['row1'] < 2) & (dataframe1['row1'] > 3), :]
dataframe1.loc[lambda rows: rows['row1'] > 1, :]

dataframe1.loc[('qualcomm', ['10-02', '10-03']), 'stock']
                    |                ｜             ｜
                一级索引值          二级索引值        对应列

#------------------------------------------------------------------------------------------------------------------------------------#
#data modify
def func(x):
	if x['col1'] > 1:
		return 1
	else:
		return 0

dataframe1['col1'] = 1
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
#merge
dataframe3 = pandas.merge(dataframe1, dataframe2, on = 'col1') 
dataframe3 = pandas.merge(dataframe1, dataframe2, left_on = 'col1', right_on = 'col2', how = "inner/left/right/outer")

#------------------------------------------------------------------------------------------------------------------------------------#
#concat / append
pandas.concat([dataframe1, dataframe2], ignore_index = True)
dataframe1.append(dataframe2, ignore_index = True)

pandas.concat(
	[pandas.Dataframe([i], columns = 'A') for i in range(5)],
	ignore_index = True
)

#------------------------------------------------------------------------------------------------------------------------------------#
#groupby
dataframe1.groupby('col1', as_index = False).sum()
dataframe1.groupby('col1').agg([numpy.sum, numpy.mean])

group = dataframe1.groupby('col1')
for name, gro in group:
	print(name)
	print(gro)

group.get_group('col1')

#------------------------------------------------------------------------------------------------------------------------------------#
#map / apply
dataframe1['col2'] = dataframe1['col1'].map(dict)
dataframe1['col2'] = dataframe1['col1'].map(lambda x : dict[x])
dataframe1['col2'] = dataframe1['col1'].apply(lambda x : dict[x])
dataframe1['col2'] = dataframe1.apply(lambda x : dict[x['col1']], axis = 1)
dataframe1.applymap(lambda x : int(x))



