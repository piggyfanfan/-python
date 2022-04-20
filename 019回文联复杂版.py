def hui(x):
    length = len(x)
    times = length // 2
    for i in range(times):
        length = length - 1
        if x[i] == x[length]:
            i += 1
            if i == times:
                return 1
        else:
            return 0
x = input('请输入检测文字：')
if hui(x) == 1:
    print('是回文联')
if hui(x) == 0:
    print('不是回文联')
    
