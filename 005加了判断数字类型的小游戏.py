import random
answer = random.randint(1,10)
times = 0
number = 0
while times <= 2 and number != answer:
    temp = input("猜猜这个随机数是多少：")
    if temp.isdigit():
        number = int(temp)
        if number < answer:
            print("小了小了～")
        if number > answer:
            print("大了大了～")
    else:
        print("数据类型不对!",end = ' ')
    times = times + 1
if number == answer:
    print("你真是我心里的蛔虫")
else:
    print("不玩啦")
