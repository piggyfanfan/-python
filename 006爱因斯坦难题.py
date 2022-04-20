print('爱因斯坦难题')
number = 0
x = 0
i = 1
while i <= 100:
    if(number % 2 == 1)and(number % 3 == 2)and(number % 5 == 4)and(number % 6 == 5):
        x = 1
    else:
        number += 7
    i += 1
if x == 1:
    print("台阶数量为", number)
else:
    print('在程序设定范围内没有合适的数字')
    
