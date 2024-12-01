#对变量或者表达式的结果进行大小，真假等的比较；比较运算的结果是布尔类型（bool）
a,b=10,20
#<：小于；比较值
print('a小于b吗？',a<b)
#>：大于；比较值
print('a大于b吗？',a>b)
#<=：小于等于；比较值
print('a小于等于b吗？',a<=b)
#>=：大于等于；比较值
print('a大于等于b吗？',a>=b)
#==：等于；比较值
print('a等于b吗？',a==b)
#!=：不等于；比较值
print('a不等于b吗？',a!=b)
#一个“=”为赋值运算符，两个“=”为比较运算符；“==”比较的是值

#is：比较标识（id）；标识相同
c=10
d=10
print('c和d的值相同吗？',c==d)#比较值
print(c,d)
print('c和d的标识相同吗？',c is d)#比较标识
print(id(c),id(d))
#以下代码没学，后面讲解
lst1=[10,20,30]
lst2=[10,20,30]
print('lst1和lst2的值相同吗？',lst1==lst2)#比较值
print(lst1,lst2)
print('lst1和lst2的标识相同吗？',lst1 is lst2)#比较标识
print(id(lst1),id(lst2))
#is not：比较标识（id）；标识不相同
print('c和d的标识不相同吗？',c is not d)
print('lst1和lst2的标识不相同吗？',lst1 is not lst2)