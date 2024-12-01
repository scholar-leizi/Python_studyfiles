#用于生成一个整数序列
'''创建range函数的三种方法：
    range(stop)-->创建一个[0,stop)之间的整数序列，步长为1
    range(start,stop)-->创建一个[start,stop)之间的整数序列，步长为1
    range(start,stop,step)-->创建一个[start,stop)之间的整数序列，步长为step'''
#返回值是一个迭代对象
#优点：不管range对象表示的序列有多长，所有range对象占用的内存空间都是相同的，因为仅仅需要存储start，stop和step，只有用到range对象时才会去计算序列中的相关元素
#in（not in）判断整数序列中是否存在（不存在）指定的整数
#可以使用函数list()查看序列中的元素
a=range(10)#指定了终止数；默认从0开始，到9结束；步长默认为1
print(list(a))

b=range(1,10)#指定了起始数和终止数；从1开始，到9结束；步长默认为1
print(list(b))

c=range(1,10,3)#指定了起始数，终止数和步长；从1开始，到9结束；步长为3
print(list(c))
#判断指定的数是否在序列中存在
print(5 in a)
print(5 not in b)
print(5 in c)