def fbnq(n):
    a1 = 1
    a2 = 1
    a3 = 1
    while n - 2 > 0:
        a3 = a1 + a2
        a1 = a2
        a2 = a3
        n -= 1
    return a3

print(fbnq(50))
        
    
