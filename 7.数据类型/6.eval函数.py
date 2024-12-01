'''
eval：
    定义：
        Python中的内置函数
        用于字符串最外侧的引号，并按照Python语句方式执行去掉引号后的字符串
        eval函数经常与input函数一起使用
    语法格式：
        变量=eval(字符串)
'''
s='3.14+3'
print(s,type(s))
x=eval(s)#去除变量s中字符串左右引号
print(x,type(x))#直接执行了加法运算

#eval函数经常和input函数一起使用
age=eval(input('请输入你的年龄：'))#将字符串类型转成int类型，相当于int(age)
print(age,type(age))

height=eval(input('请输入你的身高：'))
print(height,type(height))

hello='北京欢迎你！'
print(hello)
print(eval('hello'))