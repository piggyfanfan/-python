temp = input("请输入一个整数：")
number = int(temp)
times = number
while times > 0:
    print(' ' * times + "*" * times)
    times = times - 1
