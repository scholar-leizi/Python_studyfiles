#程序执行顺序：从左到右
#支持链式赋值：变量存储的地址，数据类型跟值都相同
a=b=c=20
print(a,b,c)
print(id(a),id(b),id(c))
print(type(a),type(b),type(c))

#支持系列解包赋值：等号两边从左到右一一对应
e,f,g,h=10,False,3.14,'Hllo werld'
print(e,f,g,h)
print(id(e),id(f),id(g),id(h))
print(type(e),type(f),type(g),type(h))
#可以给不同变量存储不同的数据；等号两边的变量个数和数据个数必须相等
#值的交换
i,j=10,20
print(id(a),id(b),id(c))
print('交换之前：',i,j)
i,j=j,i#交换值
print('交换之后：',i,j)

#支持参数赋值
#+=：加法运算和从新给变量赋值
print('-----+=运算-----')
d=10
d+=10#d=d+10；用最新的变量进行加法运算，并把结果重新赋值给变量
print(d)#20：新的值
#现在d=20
#-=：减法运算和从新给变量赋值
print('------=运算-----')
d-=10#d=d-10；用最新的变量进行加法运算，并把结果重新赋值给变量
print(d)#10：新的值
#现在d=10
#*=：乘法运算和从新给变量赋值
print('-----*=运算-----')
d*=2#d=d*2；用最新的变量进行乘法运算，并把结果重新赋值给变量
print(d)#20：新的值
#现在d=20
#/=：除法运算和从新给变量赋值
print('-----/=运算-----')
d/=2#d=d/2；用最新的变量进行除法运算，并把结果重新赋值给变量
print(d)#10.0：新的值为浮点数类型，转换为整数类型
d=int(d)#数据类型转换：floa转int
print(d)
#现在d=10
#//=：整出运算和从新给变量赋值
print('-----//=运算-----')
d//=2#d=d//2；用最新的变量进行整除运算，并把结果重新赋值给变量
print(d)#5：新的值
#现在d=5
#%=：取余运算和从新给变量赋值
print('-----%=运算-----')
d%=2#d=d//2；用最新的变量进行取余运算，并把结果重新赋值给变量
print(d)#1：新的值
#现在d=1