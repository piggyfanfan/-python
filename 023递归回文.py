def is_palindrome(n, start, end):

        if start > end:
                return 1     
        else:
                return is_palindrome(n, start+1, end-1) if n[start] == n[end] else 0
        

string = input('请输入一串字符串：')
length = len(string)-1

if is_palindrome(string, 0, length):#n=string;0=start;end=length,当is_palindrome(string, 0, length)=1时成立
        print('"%s"是回文字符串!' % string)
else:#当is_palindrome(string, 0, length)=0时成立
        print('"%s"不是回文字符串!' % string)
