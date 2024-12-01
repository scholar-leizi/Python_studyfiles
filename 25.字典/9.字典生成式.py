##字典生成式是字典生成公式的简称
#items=['Fruits','Books','Others']
#prices=[96,78,85]
#{'FRUITS':96,'BOOKS':78,'OTHERS':85}
'''
内置函数zip()：
    用于将可迭代的对象作为参数，将对象中对应的元素打包成一个元组，然后返回由这些元组组成的列表
    items=['Fruits','Books','Others']
    prices=[96,78,85]
    lst=zip(items,prices)
    print(list(lst))
'''
#字典生成式：{表示字典键的表达式:表示字典值的表达式 for 自定义表示键的变量,自定义表示值的变量 in zip(可迭代对象)}
items=['Fruits','Books','Others']
prices=[96,78,85]
#{'FRUITS': 96, 'BOOKS': 78, 'OTHERS': 85}
a={item.upper():price for item,price in zip(items,prices)}#upper() 大写字母
print(a)
#两列表元素不相等时以元素少的列表为基础生成字典