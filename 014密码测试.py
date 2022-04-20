symbols = r'''`!@#$%^&*()_+-=/*{}[]\|'";:/?,.<>'''
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = '0123456789'

passwd = input('请输入需要检查的密码组合：')

length = len(passwd)

while(passwd.isspace() or length == 0):
    passwd = input("您输入的密码为空（或空格），请重新输入：")
    length = len(passwd)
    

if length <= 8:
    passwdlen = 1
elif 16 > length >= 8:
    passwdlen = 2
else:
    passwdlen = 3
    
con = 0
for each in passwd:
    if each in symbols:
        con += 1
        break
for each in passwd:
     if each in chars:
         con += 1
         break
for each in passwd:
    if each in nums:
        con +=1
        break

while 1:
    print('您的密码安全等级为：', end = '')
    if len == 1 or con == 1:
        print('低')
    elif len ==3 and con ==3 and (passwd[0] in chars):
        print('高')
        print('请继续保持')
        break
    else:
        print('中')
    print('请按以下方法提升密码安全等级：\n\
        \t1. 密码必须由数字、字母及特殊字符三种组合\n\
        \t2. 密码只能由字母开头\n\
        \t3. 密码长度不能低于16位')
    break
