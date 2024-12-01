'''
判断指定元素是否在列表中存在：
元素 in 列表
元素 not in 列表
'''
lst=[520,3.14,'Python',True]
print(10 in lst)
print(520 not in lst)
print('Python' in lst)

print('-----------')
#列表的遍历：“for 迭代变量 in 列表名”
for item in lst:
    print(item)