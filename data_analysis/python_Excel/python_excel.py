#------------------------------------------------------------------------------------------------------------------------------------#
#pandas
dafaframe_excel = pandas.read_excel('')
dafaframe_csv = pandas.read_csv('', header=None)
dafaframe_txt = pandas.read_csv('')

dafaframe_csv.iloc[1, 2]
dafaframe_csv.loc[dafaframe_csv['name'] == 'n']
dafaframe_csv['newcol'] = dafaframe_csv['name'].apply(lambda x : x)

file = value.to_excel('', index=None)
