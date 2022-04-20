dict1 = {}

def new():
    prompt = input('请输入用户名：')
    while True:
        name = input(prompt)
        if name in dict1:
            prompt = input('此用户名已经被使用，请重新输入：')
            continue
        else:
            break
    passwd = input('请输入密码：')
    dict1[name] = passwd
    print('注册成功，赶紧试一试吧～')


def old():
    prompt = ('请输入用户名：')
    while True:
        name = input(prompt)
        if name not in dict1:
            prompt = input('你输入的用户名不存爱，请重新输入：')
            continue
        else:
            break
    passwd = input('请输入密码：')
    pwd = dict1.get(name)
    if passwe == pwd:
        print('欢迎～')
    else:
        print('密码错误！')

def showmenu():
    prompt = input('''
|--- 新建用户：N/n ---|
|--- 登录账号：E/e ---|
|--- 推出程序：Q/q ---|
|--- 请输入指令代码：''')
    while True:
        chosen = Flase
        while not chosen:
            chioce = input(prompt)
            if chioce not in 'EeNnQq':
                print('输入的指令有误，请重新输入：')
            else:
                chose = True
            if choice == 'q' or choice == 'Q':
                break
            if choice == 'n' or choice == 'N':
                new_user()
            if choice == 'e' or choice == 'E':
                old_user()

showmenu()
        
