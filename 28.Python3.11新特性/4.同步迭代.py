'''
语法结构：
    match data1,data2:
        case data1,data2:
            pass
'''
#fruites={'apple','orange','pear','grape'}
fruites=['apple','orange','pear','grape']
counts=[10,3,4,5]
for f,c in zip(fruites,counts):
    match f,c:
        case 'apple',10:
            print('有10个苹果')
        case 'orange',3:
            print('有3个橘子')
        case 'pear',4:
            print('有4个梨')
        case 'grape',5:
            print('有5串葡萄')