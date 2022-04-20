print('|--- 欢迎进入通讯录程序---|')
print('|--- 1：查询联系人资料---|')
print('|--- 2：插入新的联系人---|')
print('|--- 3：删除已有联系人---|')
print('|--- 4：退出通讯录程序---|')


dict1 = {}
while 1:
    number = int(input('请输入相关的代码指令：'))
    
    if number == 2:
        name = input('请输入联系人姓名：')
        if name in dict1:
            print('您输入的姓名在通讯录中已存在 -->>',name,':',dict1[name])
            change = input('是否要更改用户资料(YES/NO)：')
            if change == 'YES':
                phone2 = input('请输入要更改的电话：')
                dict1[name] = phone2
        else:
            phone = input('请输入用户联系电话：')
            dict1 = {name : phone}
    elif number == 1:
        name = input('请输入联系人姓名：')
        print(name,':',dict1[name])
    else:
        if number == 4:
            break
print('|--- 感谢使用通讯录程序---|')
