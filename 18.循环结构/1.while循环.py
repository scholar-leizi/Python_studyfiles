#反复做同一件事的过程叫做循环
#语法结构：
'''while 条件表达式：
    条件执行体（循环体）'''

print('-----if语句-----')
a=1
if a<10:
    print(a)
    a+=1

print('-----while语句-----')
b=1
while b<10:
    print(b)
    b+=1
#分支结构的if和循环结构的while的区别：if是判断一次，条件为True执行一行；while是判断N+1次，条件为True执行N次

#while的四步循环法：初始变化量；条件判断；条件执行体（循环体）；改变变量
#总结：初始化的变量，条件判断的变量和改变的变量为同一个变量
print('-----要求计算0到4之间的累加和-----')
c=0#初始变化量
sum=0#用来存储和
while c<5:#判断循环条件
    sum+=c#存储和
    c+=1#改变初始变化量
print('和为'+str(sum))

print('-----while循环练习-----')
#计算1到100的偶数,奇数和
d=1
e=0
f=0
while d<=100:
    if d%2==0:#if not bool(d%2)
        e+=d
    else:
        f+=d
    d+=1
print('奇数和为'+str(f)+','+'偶数和为'+str(e))