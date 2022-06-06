#------------------------------------------------------------------------------------------------------------------------------------#
#numpy array
arr = numpy.array([1, 2])
arr.shape
arr.ndim
arr.dtype
arr.size
arr.sort()
arr.argsort()

numpy.arange(2, 10, 2) #[2,10)
numpy.arange(2).reshape(1, 1) #[2,10)
numpy.arange(2) * 2
numpy.ones((2, 3))
numpy.ones_like(arr)
numpy.zeros((2, 3))
numpy.zeros_like(arr)
numpy.empty((2, 3))
numpy.empty_like(arr)
numpy.full((2, 3), 0)
numpy.full_like(arr, 0)
numpy.random.randn(3) #shape

l = list(arr)

#------------------------------------------------------------------------------------------------------------------------------------#
#numpy search
arr[2] #row2
arr[:2, 2:4]     #连续取值 ：
arr[[2, 5], 2:4] #间断取值 []
arr[[index_arr]]
arr[arr > 4]

#------------------------------------------------------------------------------------------------------------------------------------#
#numpy random
numpy.random.rand(3)    #0 - 1
numpy.random.randn(3)   #-1 - 1
numpy.random.randint(3) #0 - 2
numpy.random.randint(1, 3, size = (5,))
numpy.random.choice(list, (1, 2)) #pick up data from list
numpy.random.shuffle()
numpy.random.permutation(10)

#------------------------------------------------------------------------------------------------------------------------------------#
#numpy math
numpy.sum(arr, axis = 1)
numpy.prod(arr)
numpy.cumsum(arr) #前缀和
numpy.cumprod(arr)
numpy.min(arr)
numpy.max(arr)

arr2 = arr - np.mean(arr, axis = 0)

#------------------------------------------------------------------------------------------------------------------------------------#
#numpy reshape
arr[numpy.newaxis, :] #添加行维度(一行五列)
arr[:, numpy.newaxis] #添加列维度(五行一列)

numpy.expand_dims(arr, axis = 0)

numpy.reshape(arr, (1, 2))
numpy.reshape(arr, (1, -1))

#------------------------------------------------------------------------------------------------------------------------------------#
#numpy concate
numpy.concatenate([arr1, arr2])
numpy.vstack([arr1, arr2])
numpy.row_stack([arr1, arr2])

numpy.concatenate([arr1, arr2], axis = 1)
numpy.hstack([arr1, arr2])
numpy.column_stack([arr1, arr2])

#------------------------------------------------------------------------------------------------------------------------------------#
#pandas
series.values
dataframe.to_numpy()
numpy.array(dataframe)

data = np.array([1, 2, 3])
ser = pd.Series(data.tolist())

data = np.array([['2019/08/02', 'zhansan', 1], ['2019/08/03', 'lisi', 2]])
df = pd.DataFrame(data)

data = np.array([['', 'Col1', 'Col2'], ['Row1', 1, 2], ['Row2', 3, 4]])
df = pd.DataFrame(data=data[1:, 1:],    # 从第2行开始并且第2列开始作为数据
                  index=data[1:, 0],    # 第1列做索引，从第2行开始
                  columns=data[0, 1:])  # 第1行作为列名，从第2列开始



