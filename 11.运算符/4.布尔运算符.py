#针对布尔值的运算
a,b=1,2
#and：只有两个运算数的结果都为True时运算结果才为True；反之为False
print('-----and 并且-----')
print(a==1 and b==2)#True
#or：只有两个运算数的结果都为False时运算结果才为False；反之为True
print('-----or 或者-----')
print(a<1 or b>2)#False
#not：运算结果跟运算数的结果相反
print('-----not 对bool操作数取反-----')
f1=True
f2=False
print(not f1)#False
print(not f2)#True

s='helloworld'
#in：包含
print('-----in 包含-----')
print('h' in s)#True
print('y' in s)#False
#not in：不包含
print('-----not in 不包含-----')
print('h' not in s)#False
print('y' not in s)#True