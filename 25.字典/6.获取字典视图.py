'''
获取字典视图：
    keys()：
        获取字典中所有的键
    values()：
        获取字典中所有的值
    items()：
        获取字典中所有的键值对
'''
scores={'张三':100,'李四':98,'王五':45}

#获取所有的键
keys=scores.keys()
print(keys)
print(type(keys))
print(list(keys))#将所有key组成的视图转换成列表

#获取所有的值
values=scores.values()
print(values)
print(type(values))
print(list(values))#将所有value组成的视图转换成列表

#获取所有的键值对
items=scores.items()
print(items)
print(type(items))
print(list(items))#将所有item组成的视图转换成列表；转换后的列表元素是由元组组成的