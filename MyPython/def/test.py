import os  '<- os 模块当中包含 os.path 模块'

os.path.dirname() '<- 表示去掉一个路径的文件名 返回目录路径 返回值是目录路径' 
os.path.isabs() '<- 表示判断是否为一个绝对路径，无论是目录还是文件 返回值' True or False
os.path.isabs(os.path.dirname(__file__))

至于这中间的file应该是个文件名 被dirname 分离后成为路径，然后在用isabs 判断是否是绝对路径
