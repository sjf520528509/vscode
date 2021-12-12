# import requests
# # 通过属性content能把Response对象的内容以二进制数据的形式返回，适用于图片、音频、
# # 视频的下载
# res = requests.get('https://res.pandateacher.com/2018-12-18-10-43-07.png') 
# pic = res.content		# 将图片以二进制形式返回

# print(pic)
# # 写入文件查看
# f = open('ppt.png','wb')	# 二进制使用wb写入
# f.write(pic)		# 写入返回数据
# f.close()

# # 通过属性text能把Response对象的内容以字符串的形式返回，适用于文字、网页源代码的下载
# # 代码一：获取小说内容
# import requests 
# url = 'https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md'
# res = requests.get(url) 	# 获取小说内容
# novel=res.text		# res.text 返回字符串给novel
# print(novel[:100])	# 字符串支持切片，打印前面100个字符

# 代码二：获取网页源代码
import requests 
url = 'https://www.baidu.com'
res = requests.get(url) 	# 获取百度网页
print(res.text.encode('utf-8'))