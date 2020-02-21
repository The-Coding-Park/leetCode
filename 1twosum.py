def SumTwo(lst,target):
    sum=0
    s=[]

    for i in range(len(lst)-1):
        if(sum<target):
            sum=sum+lst[i]
            s.append(i)
        else:
            break
    return s

a=[2, 7, 11, 15]
target=9
print(SumTwo(a,target))