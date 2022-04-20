dict1 = {}
while 1:
    print('|---新建用户：N/n ---｜')
    print('|---登陆账号：E/e ---｜')
    print('|---退出程序：Q/q ---｜')
    member = input('|---请输入指令代码：')
    
    if member == 'N' or member == 'n':
        people = input('请输入用户名：')
        if people in dict1:
            people2 = input('此用户名已经被使用，请从新输入：')
            secret = input('请输入密码：')
            dict1.fromkeys(people,secret)
            print('注册成功，赶紧登陆试一下吧！')
        else:
            secret = input('请输入密码：')
            dict1.fromkeys(people,secret)
            print('注册成功，赶紧登陆试一下吧！')
    if  member == 'E' or member == 'e':
        people = input('请输入用户名：')
        if people not in dict1:
            people3 = input('输入的用户名不存在，请从新输入：')
            secret = input('请输入密码：')
            if secret == dict1[people]:
                print('欢迎')
                break
            
