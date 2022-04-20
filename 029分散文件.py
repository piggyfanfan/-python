#打开record.txt文件
f = open('/Users/zhaokai/Desktop/record.txt')  
 
#定义3个变量，并对它们初始化
boy = []     
girl = []
count = 1
 
#循环读取文件
for each_line in f:
  
  #如果当前内容不等于"======"，则继续读取内容；否则读取，开始写操作
  if each_line[:6] != "======":            
    
    #读取的内容以":"进行分割，分割后分别赋值给元组元素role和spoken
    (role,spoken) = each_line.split('：',1) 
    
    #如果对话角色为"小甲鱼"，则将文件追加到boy列表中
    if role == '小甲鱼':                  
       boy.append(spoken)
       
    #如果对话角色为"小客服"，则将文件追加到girl列表中
    if role == '小客服':                   
       girl.append(spoken)
  else:
     #定义输出文件名称
     file_name_boy = 'boy_'+str(count)+'.txt'  
     file_name_girl = 'girl_'+str(count)+'.txt' 
    
     #打开文件
     boy_file = open(file_name_boy,'w')         
     girl_file = open(file_name_girl,'w')     
     
     #writelines的参数是序列(比如列表)，它会迭代帮你写入文件。
     boy_file.writelines(boy)     
     girl_file.writelines(girl) 
     
     #关闭文件对象
     boy_file.close()                                   
     girl_file.close()                          
     
     #当前写操作完毕后，必须进行初始化操作，以准备下一个的写入操作
     boy = []
     girl = []
     count += 1
 
#因为第三段对话的结尾没有"==="，所以需要再次进行上面的重复写操作，保存第三段对话
#定义输出文件名称     
file_name_boy = 'boy_'+str(count)+'.txt'  
file_name_girl = 'girl'+str(count)+'.txt'  
 
#打开文件    
boy_file = open(file_name_boy,'w')         
girl_file = open(file_name_girl,'w') 
 
#writelines的参数是序列(比如列表)，它会迭代帮你写入文件。     
boy_file.writelines(boy)   
girl_file.writelines(girl) 
 
#关闭文件对象      
boy_file.close()                                
girl_file.close()                    
 
#关闭文件对象
f.close()
