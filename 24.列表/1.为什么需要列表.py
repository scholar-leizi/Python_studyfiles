#列表可以存储一个元素，而列表是一个“大容器”，它可以存储多个元素，程序可以方便的对这些数据进行整体操作
#列表相当于其它语言中的数组
#列表示意图：
'''
索引    -7       -6     -5    -4     -3      -2      -1
数据  ”hello“  “world”  123  3.14  “world”  False  ”world“
索引     0        1      2    3       4       5       6
'''
lst=['hello',123,3.14,False]
print(id((lst)))
print(type(lst))
print(lst)
#列表中的元素都有不同的id；列表是一个新的对象，有自己的地址，类型和值
