def mfun(*member, base = 3):
    result = 0
    for each in member:
        result += each
    result *= base
    print('结果是：', result)
mfun(1, 2, 3, 4, 5, base=5)
        
    
