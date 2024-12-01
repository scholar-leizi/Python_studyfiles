#循环结构中又嵌套了另外的完整的循环结构，其中内层循环做为外层循环的循环执行体
#输出一个三行四列的矩形
a=0
while a<3:#行表，执行一次是一行
    for _ in range(5):#一行执行4次
        print('*',end='\t')#不换行输出
    print()#打印输出
    a+=1

#打印直角三角形
for b in range(1,10):
    for c in range(1,b+1):
        print(str(c)+'*'+str(b)+'='+str(c*b),end='\t')
    print()
