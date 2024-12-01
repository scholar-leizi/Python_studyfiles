'''
获取字典元素的方法：
    []：scores['张三']
    get()：scores.get()

[]取值和get()取值的区别：
    []取值如果字典不存在指定的key，会返回kryError异常
    get()取值如果字典中不存在key，并不会返回keyError异常而是返回None，可以通过参数设置默的value，以便指定的key不存在时返回
'''
scores={'张三':100,'李四':98,'王五':45}
print('-----[]获取-----')
print(scores['张三'])
#print(scores['陈六'])#keyError
print('-----get()获取-----')
print(scores.get('李四'))
print(scores.get('陈六'))#None
print(scores.get('麻七',99))#99是查找指定键对应的值不存在时提供的默认值
