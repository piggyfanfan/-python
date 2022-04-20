def get_digits(n):
    
    result = []

    
    if n > 0:
        result.insert(0, n % 10)
        return  get_digits(n // 10) + result
    else:
        return []
    

print(get_digits(12345))
