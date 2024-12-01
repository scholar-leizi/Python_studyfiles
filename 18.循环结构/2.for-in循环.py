#in表示从字符串，序列等中依次取值，又称为遍历
#for-in遍历的对象必须是可迭代对象
#语法结构：
'''for 自定义的变量 in 可迭代对象：
    循环体'''
for item in 'Python':#依次取值并赋值给变量
    print(item)
#range函数产生的整数序列也是一个可迭代对象
for i in range(10):
    print(i)
#循环体内不需要访问自定义变量，可以将自定义变量代替为下划线
for _ in range(5):
    print('人生苦短，我用Python')
#使用for循环，计算1到100的累加和
print('-----使用for循环，计算1到100的累加和-----')
b=0
for a in range(1,101):
    if a%2==0:
        b+=a
print('1到100的偶数和为'+str(b))

print('-----for-in循环练习-----')
#输出100到999之间的水仙花数
#水仙花数：各位上的数的三次方的和等于它本身的数
for c in range(100,1000):
    ge=c%10#个位
    shi=c//10%10#十位
    bai=c//100#百位
    if ge**3+shi**3+bai**3==c:
        print(c)