#浮点数由整数和小数两部分组成
a=1.1
b=2.2
c=2.1
print(a,type(a))
print(b,type(b))
print(c,type(c))

#浮点数的存储具有不精确性
#使用浮点计算时可能会出现小数点不准确的情况
print(a+c)
print(a+b)
#解决方案为导入模块decimal
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))#deciml要用字符串，不要用变量