a = 'FishC.com'
times = 3
while times != 0:
    secret = str(input('请输入密码：'))
    if secret == a:
        print('密码输入正确，正在进入...')
        break
    elif '*' in secret:
        print('密码中不能含有"*"号！您还有', times , '次机会！', end=' ')
        continue
    else:
        print('密码输入错误！您还有', times-1, '次机会！', end=' ')
    times -= 1
