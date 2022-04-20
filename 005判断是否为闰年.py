print('判断该年是否为闰年')
temp = input("请输入一个年份：")
while not temp.isdigit():
    temp = input("请输入一个数字：")
number = int(temp)
if ((number % 4 == 0) and (number % 100 != 0)) or (number % 400 == 0):
    print(number, '年是闰年')
else:
    print(number, '年不是闰年')
        
