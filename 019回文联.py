def back(word):
    list1 = list(word)
    list2 = reversed(list1)
    if list2 == list1:
        return('是回文联' )
    else:
        return('不是回文联')
        
print(back('上海自来水来自海上'))
