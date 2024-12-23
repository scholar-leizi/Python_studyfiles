#为什么要进行数据类型转换：将不同类型的数据拼接在一起
a=10
b=3.14
c=True
d='人生苦短，我用Python'
e='123'
f=31.4

#str()：将其他数据转换为字符串类型
print('-----整数转换为字符串-----')
print(type(a))#查看类型为int类型（整数类型）
print(str(a))#将int转换为str
print(type(str(a)))#查看转换后的数据类型
print('-----浮点数转换为字符串-----')
print(type(b))#查看类型为float类型（浮点数类型）
print(str(b))#将float转换为str
print(type(str(b)))#查看转换后的数据类型
print('-----布尔值转换为字符串-----')
print(type(c))#查看类型为bool类型（布尔类型）
print(str(c))#将bool转换为str
print(type(str(c)))#查看转换后的数据类型
#注意事项：可以直接使用引号转换

#int()：将其他类型转换为整数类型
print('-----浮点数转换为整数-----')
print(type(b))#查看类型为float类型（浮点数类型）
print(int(b))#将float转换为int
print(type(int(b)))#查看转换后的数据类型
print('-----布尔值转换为整数-----')
print(type(c))#查看类型为bool类型（布尔类型）
print(int(c))#将bool转换为int
print(type(int(c)))#查看转换后的数据类型
print('-----字符串转换为整数-----')
print(type(e))#查看类型为str类型（字符串类型）
print(int(e))#将str转换为int
print(type(int(e)))#查看转换后的数据类型
#注意事项：文字类和小数类的字符串无法转为整数类型；浮点数转为整数时结果会抹零取整

#float()：将其他类型转换为浮点数类型
print('-----整数转换为浮点数-----')
print(type(a))#查看类型为int类型（整数类型）
print(float(a))#将int转换为float
print(type(float(a)))#查看转换后的数据类型
print('-----布尔值转换为浮点数-----')
print(type(c))#查看类型为bool类型（布尔类型）
print(float(c))#将bool转换为float
print(type(float(c)))#查看转换后的数据类型
print('-----字符串转换为浮点数-----')
print(type(f))#查看类型为str类型（字符串类型）
print(float(f))#将str转换为lioat
print(type(float(f)))#查看转换后的数据类型
print('-----字符串转换为浮点数-----')
print(type(e))#查看类型为str类型（字符串类型）
print(float(e))#将str转换为lioat
print(type(float(e)))#查看转换后的数据类型
#注意事项：文字类无法转换成数字；整数转换为浮点数时后面会加一位小数

name='张三'
age=20
print('我叫'+name+'，'+'今年'+str(age)+'岁！')