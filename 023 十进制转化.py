def ten2two(n):
    result =''
    
    if n // 2 != 0:
        result = ten2two(n // 2)
        return result + str(n%2)
    else:
        return result + str(1)

    
print(ten2two(111))
        
    
