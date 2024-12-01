#print函数是可以直接使用的函数，可以将你想展示的任何东西在IDLE或者标准控制台上显示
print(520)
#向计算机发送打印520的请求，python解释器把代码翻译成计算机能听懂的语言，做出相应的执行操作（在控制台上输出结果）

#print函数的使用
#print函数可以输出那些内容
#可以输出数字
print(25)
print(3.1415)
#可以输出字符串
print("你好")
#可以输出含有运算符的表达式
print(3+5)

#print函数输出的地址
#输出在控制台
print(520)
#输出在文件中
fp=open('D:/输出在文件中.txt','a+')#a+的意义为文件存在就写入，不存在创建再写入
print("hello world",file=fp)
fp.close()
#把文件输出在文件中时地址要存在并正确，同时要用函数file=来给文件写入内容

#print函数的换行和不换行输出
#不换行（输出内容在同一行）
print(45,'Python',False)
#换行（输出内容不在同一行）
print(45)
print('Python')
print(False)