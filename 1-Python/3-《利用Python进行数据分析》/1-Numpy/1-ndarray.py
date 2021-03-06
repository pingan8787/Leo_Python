import numpy as np

# 一、创建数组
## 1、np.array()  
d1 = [1,2.3,4,5,0,1]
a1 = np.array(d1)       # array([1,2.3,4,5,0,1] )
d2 = [[1,2,3],[4,5,6]]
a2 = np.array(d2)       # array([[1,2,3],[4,5,6]])

## 2、np.zeros()
### 返回给定形状和类型的新数组，用零填充
### 等同于np.zeros([3,6])
d3 = np.zeros((3,6))    # array([[ 0.,  0.,  0.,  0.,  0.,  0.],
                        #        [ 0.,  0.,  0.,  0.,  0.,  0.],
                        #        [ 0.,  0.,  0.,  0.,  0.,  0.]])
d4 = np.zeros([5,])     # array([ 0.,  0.,  0.,  0.,  0.])

## 2-1、np.ones()
### 返回给定形状和类型的新数组，用1填充。
d3 = np.ones((2,3)) 
### array([[ 1.,  1.,  1.],
###        [ 1.,  1.,  1.]])

## 3、np.arange()
### 创建后并按序号填充
d5 = np.arange(5)       # array([0,1,2,3,4])

# 二、数组和标量间的运算
b1 = np.array([[1. ,2. ,3.],[4. ,5. ,6. ]])
b1 * b1                 # array([[ 1., 4.,  9.],  [ 16., 25., 36.]])
b1 - b1                 # array([[ 0., 0.,  0.],  [ 0.,  0.,  0.]])
1 / b1                  # array([[ 1., 0.5, 0.33333333], [ 0.25 , 0.2 , 0.16666667]])
b1 ** 0.5               # array([[ 1., 1.41421356, 1.73205081], [ 2. , 2.23606798, 2.44948974]])

# 三、索引和切片
## 1、切片
c1 = np.arange(10)      # array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
c1[5]                   # 5
c1[5:8]                 # array([5, 6, 7])
c1[5:8] = 12            # array([ 0,  1,  2,  3,  4, 12, 12, 12,  8,  9])

c01    = c1[5:8]        # array([12, 12, 12])
c01[1] = 12345          # c1 输出  array([ 0, 1, 2, 3, 4, 12, 12345, 12, 8, 9])
c01[:] = 64             # c1 输出  array([ 0, 1, 2, 3, 4, 64, 64, 64, 8, 9])

## 2、索引
c2 = np.array( [ [1,2,3],[4,5,6],[7,8,9]] )
c2[2]                   # array[7,8,9]
c2[0][2]                # 3
c2[0,2]                 # 这种方式也可以只要中间加个逗号，  返回3
c3 = np.array([ [ [1,2,3],[4,5,6] ],[ [11,12,13],[14,15,16]]])
c3[0,1,2]               # 6

## 3、切片索引
c4 = np.array([1,2,3,4,64])
c4[:2]                  # array([1,2])
c5 = np.array( [ [1,2,3],[4,5,6],[7,8,9]] )
c5[:2]                  # array( [ [1,2,3],[4,5,6]] )
c5[:2,1:]               # array( [ [2,3],[5,6]] )

## 4、布尔型索引
n1 = np.array(['leo','joe','will','leo'])
n2 = np.random.randn(4,3)
n1 == 'leo'             # array([ True, False, False,  True], dtype=bool)
n2[n1 == 'leo']         # array([[ 0.21290226,  0.36681319, -0.17444623],
                        #        [-1.74872491,  0.38560779, -1.66968095]]) 
n2[n1=='leo',2:]        # array([[-0.17444623],
                        #        [-1.66968095]])
n2[n1=='leo',2]         # array([-0.17444623, -1.66968095])
n1 != 'leo'             # array([False,  True,  True, False], dtype=bool)
n2[~(n1 == 'leo')]      # array([[-1.13528941,  0.16400326,  0.69102992],
                        #        [- 0.84246446,  0.92204585,  0.75928527]])
n2[ (n1 != 'leo')]      # array([[-1.13528941,  0.16400326,  0.69102992],
                        #        [-0.84246446,  0.92204585,  0.75928527]])
### 还可以使用 & (和)、| (或)之类的布尔运算符
n3 = (n1 == 'leo') & (n1 == 'joe')  # array([ False,  False, False,  False], dtype=bool)
n3 = (n1 == 'leo') | (n1 == 'joe')  # array([ True,  True, False,  True], dtype=bool)

### 还可以通过布尔值设置值
n2[n1 == 'leo'] = 3     # array([[ 3.        ,  3.        ,  3.        ],
                        #        [-2.81166546, -0.82847677, -1.21673666],
                        #        [ 2.71631543,  0.35552634, -0.45955992],
                        #        [ 3.        ,  3.        ,  3.        ]])

# 三、一些常用方法API
## 中文API手册地址：http://python.usyiyi.cn/translate/NumPy_v111/genindex.html
s1 = [[1,2,3],[4,5,6]]
m1 = np.array(s1)       # array([[1,2,3],[4,5,6]])

## 1、shape
## 作用：表示数组维度/尺寸
m1.ndim                 # 2  两种写法一致
np.ndim(m1)             # 2

## 2、dtype
## 表示数组数据类型的对象
m1.detype               # dtype('int32')
np.detype(m1)           # dtype('int32')

## 3、shape
## 表示各维度大小的元组
m1.shape                # (2, 3)
np.shape(m1)            # (2, 3)

## 4、mean
## 沿指定轴计算算术平均值
## (@ a:数组 , axis:指定轴 , dtype:平均值类型 ....)
o1 = np.array([[1, 2], [3, 4]])
np.mean(o1)             # 2.5  (1+2+3+4)/4 = 2.5
np.mean(o1,axis=0)      # array([2.,3.])    0：指定纵轴
np.mean(o1,axis=1)      # array([1.5,3.5])  1：指定横轴


# 四、numpy数据类型
## 常见numpy数据类型，具体查看书本
###################################################################
##   类型       ##   类型代码   ##         说明                    ##
## int8、unit8  ##  i1、u1     ## 有符号和无符号的8位(1个字节)整型   ##
## int16、unit16##  i2、u2     ## 有符号和无符号的16位(2个字节)整型  ##
## int32、unit32##  i4、u4     ## 有符号和无符号的32位(4个字节)整型  ##
## float16      ##  f2         ## 半精度浮点数                    ##
## float32      ##  f4或f      ## 标准的单精度浮点数。与C的float兼容##
## bool         ##  ?          ## 存储True和False值的布尔类型      ##
## object       ##  O          ## Python对象类型                  ##
## string_      ##  S          ## 固定长度的字符串类型(每个字符1字节)##
##                                如创建长度10的字符串，使用S10     ##
## unicode_     ##  U          ## 固定长度的unicode类型(字节数由平台##
##                                决定),跟字符串定义一样(如U10  )   ##
###################################################################

# 五、转换类型
## 常常使用 astype 方法显式转换成其他类型
t1 = np.array([1,2,3,4,5])
t1.dtype                # dtype('int32')
t2 = t1.astype(np.float64)
t2.dtype                # dtype('float64')
t3 = np.array([3.1,-1.2,-2.6,0.5,12.9,10.1])
t4 = t3.astype(np.int32)# array([ 3, -1, -2,  0, 12, 10])
t3.dtype                # dtype('float64')
t4.dtype                # dtype('int32')
t5 = np.array(['1.25','-9.6','42'],dtype = np.string_)
t5.dtype                # dtype('S4')
t6 = t5.astype(float)
t6.dtype                # dtype('float64')

# 六、花式索引
## 指的是利用整数数组进行索引。
h1 = np.empty((8,4))
### array([[ 0.,  0.,  0.,  0.],
###       [ 0.,  0.,  0.,  0.],
###       [ 0.,  0.,  0.,  0.],
###       [ 0.,  0.,  0.,  0.],
###       [ 0.,  0.,  0.,  0.],
###       [ 0.,  0.,  0.,  0.],
###       [ 0.,  0.,  0.,  0.],
###       [ 0.,  0.,  0.,  0.]])
for i in range(8):
    h1[i] = i
h1 
### array([[ 0.,  0.,  0.,  0.],
###        [ 1.,  1.,  1.,  1.],
###        [ 2.,  2.,  2.,  2.],
###        [ 3.,  3.,  3.,  3.],
###        [ 4.,  4.,  4.,  4.],
###        [ 5.,  5.,  5.,  5.],
###        [ 6.,  6.,  6.,  6.],
###        [ 7.,  7.,  7.,  7.]])
## 通过传入一个制定顺寻的数组列表或者ndarray
h1[[4,3,0,6]]
### array([[ 4.,  4.,  4.,  4.],
###        [ 3.,  3.,  3.,  3.],
###        [ 0.,  0.,  0.,  0.],
###        [ 6.,  6.,  6.,  6.]])
h1[[-3,-5,-7]]           # 负数为从后开始
### array([[ 5.,  5.,  5.,  5.],
###        [ 3.,  3.,  3.,  3.],
###        [ 1.,  1.,  1.,  1.]])


# 七、数组转置和轴对称
## 转置是重塑的一种特殊形式，返回源数据的视图，不会进行任何复制操作
## 数组不仅有ranspose方法，还有特殊的T属性
i1 = np.arange(15).reshape((3,5))   # reshape 为数组提供新形状，而不更改其数据。
### array([[ 0,  1,  2,  3,  4],
###        [ 5,  6,  7,  8,  9],
###        [10, 11, 12, 13, 14]])
i1.T                   # 转置
### array([[ 0,  5, 10],
###        [ 1,  6, 11],
###        [ 2,  7, 12],
###        [ 3,  8, 13],
###        [ 4,  9, 14]])

## 计算两个数组的点积
i2 = np.random.randn(6,3)
i3 = np.dot(i2.T,i2)    # 计算矩阵内积XT*X
### array([[ 14.0431, 3.5793, 0.5373],
###        [  3.5793, 7.3162, 0.3103],
###        [  0.5373, 0.3103, 2.5405]])

## 另外还有比较难的 处理高阶数组用transpose ，还有一个处理简单转置用swapaxes方法，这里暂时不研究。 