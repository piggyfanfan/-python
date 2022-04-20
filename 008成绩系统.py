point = int(input("请输入要查询的成绩："))
if 100 >= point >= 90:
    print('A')
elif 90 > point >= 80:
    print('B')
elif 80 > point >= 60:
    print('C')
elif point < 60:
    print('D')
else:
    print('查询无效～')
