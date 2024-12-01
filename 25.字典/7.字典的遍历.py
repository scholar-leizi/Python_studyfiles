#依次获取字典中的元素
scores={'张三':100,'李四':98,'王五':45}
for item in scores:
    print(item)#输出的值字典的键
    print(item,scores[item],scores.get(item))