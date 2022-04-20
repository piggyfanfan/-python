def power(x, y):
    if y == 0:
        return y+1
    else:
        return x *  power(x, y-1)
    
print(power(3,3))
