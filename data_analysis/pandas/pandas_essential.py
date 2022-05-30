#------------------------------------------------------------------------------------------------------------------------------------#
#data input
data = pandas.read_csv('path', skip_rows = 1)
data.head()
data.tail()

#------------------------------------------------------------------------------------------------------------------------------------#
#dataframe / series
data['col'] / data.col / data[['col', 'col1']] 

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
