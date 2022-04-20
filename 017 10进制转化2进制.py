def tentotwo(x):
    list1 = []
    result = ''
    
    while x:
        y = x % 2
        x = x // 2
        list1.append(y)
    while list1:
        result += str(list1.pop())#二进制是这个方法倒着来的～#
    
        
    return result

print(tentotwo(111))
        
        
    
