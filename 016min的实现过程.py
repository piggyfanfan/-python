def least(x):
    least = x[0]
    for each in x:
        if each < least:
            least = each
    return least 

print(least((1,2,3)))
            
            
