def euclid(x, y):
    z = x % y
    if z != 0:
        x = y
        y = z
        return euclid(x, y)
    else:
        return y
    
print(euclid(100, 10))
