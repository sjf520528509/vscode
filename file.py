# 读取文件
# file1 = open(r'C:\Users\Administrator.DESKTOP-3IDB3SQ\Desktop\pachong.txt','r',encoding='utf-8') # 文件的绝对路径
# filecontent = file1.read()      # 读取文件内容
# print(filecontent)	# 打印读取的内容
# file1.close()       # 关闭文件

# file2 = open('readme.md','r',encoding='utf-8') # 相对路径
# filecontent = file2.read()
# print(filecontent)
# file2.close()


# 写文件
# file1 = open('readme.md', 'w', encoding='utf-8')
# file1.write('神雕侠侣22\n'.encode('utf-8'))
# file1.write('小龙女22\n'.encode('utf-8'))
# file1.close()

# file2 = open('readme.md', 'r', encoding='utf-8')
# filecontent = file2.read()      # 读取文件内容
# print(filecontent)	# 打印读取的内容
# file2.close()


# with关键字，使用with关键字后可以不用使用close了
# 普通写法
# file1 = open('readme.md','a') 
# file1.write('张无忌') 
# file1.close()

# 使用with关键字的写法
with open('readme.md','a',encoding='utf-8') as file1:  # 格式：with open('文件地址','读写模式') as 变量名:
    file1.write('张无忌')  # 格式：对文件的操作要缩进，无需用close()关闭文件