#二重循环中的break和continue只控制本层循环流程
print('-----内层循环中的break-----')
for i in range(5):#外层循环5次
    for j in range(1,11):
        if j%2==0:
            break
        print(j)

print('-----内层循环中的contiune-----')
for i in range(5):#外层循环5次
    for j in range(1,11):
        if j%2==0:
            continue
        print(j,end='\t')
    print()