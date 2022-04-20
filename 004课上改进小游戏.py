import random
secret = random.randint(1,10)
temp = input("不妨猜测一下赵凯心里想的是哪个数字：")
guess = int(temp)
while guess != secret:
    temp = input("输错了，请重新输入：")
    guess = int(temp)
    if guess == secret:
        print("卧槽，你是我心里的蛔虫吗？")
        print("嘻嘻嘻，猜对了也没有奖励")
    else:
        if guess > secret:
            print("嘿嘿，大了大了")
        else:
            print("嘿嘿，小了小了")
print("游戏结束，不玩啦～")
