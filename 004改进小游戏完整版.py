import random
answer = random.randint(1,10)
times = 2
temp = input("猜一猜这个随机数是多少：")
number = int(temp)
if number == answer:
    print("太牛啦！")
else:
    if number > answer:
        print("大了大了")
    else:
        print("小了小了")
    while times > 0 and number != answer:
        temp = input("猜错啦，还有机会，在输入一次吧：")
        number = int(temp)
        if number == answer:
            print("牛逼！")
        else:
            if number > answer:
                print("大了大了")
            else:
                print("小了小了")
        times = times - 1
        if times == 0:
            print("机会没有啦～")
print("结束啦")
