import os.path
import shutil

# 判断文件是否存 如果不存在创建该文件夹
path1 = 'E:\\'
if not os.path.exists(path1):
    os.makedirs(path1)
path2 = 'D:\\Users\\CuiZipeng\\NewDirectory1'
# 判断文件是否存 如果不存在创建该文件夹
if not os.path.exists(path2):
    os.makedirs(path2)
# 判断文件是否存 如果不存在创建该文件夹
path3 = 'D:\\Users\\CuiZipeng\\NewDirectory2'
if not os.path.exists(path3):
    os.makedirs(path3)
# 删除文件或者文件夹
os.rmdir('E:\\NewDirectory3')
# shutil.rmtree('D:\\Users\\CuiZipeng\\NewDirectory3')
# 查看文件夹目录下的文件夹
list1 = os.listdir('E:\\')
print(list1)
# os.path.split('D:\\Users\\CuiZipeng\\NewDirectory4')
# 移动该文件夹到另一个文件夹
shutil.move(
    'D:\\Users\\CuiZipeng\\NewDirectory2'
    'D:\\Users\\CuiZipeng\\NewDirectory3'）
# 以二进制形式打开文件夹
fp1 = open(
    'D:\\Users\\CuiZipeng\\NewDirectory4'
    'wb')
# 关闭这个工作流
fp1.close()
# 以二进制形式打开文件夹
fp2 = open(
     'D:\\Users\\CuiZipeng\\NewDirectory5'
    'wb')
# 关闭这个工作流
fp2.close()
# 以二进制形式打开文件夹
fp3 = open(
     'D:\\Users\\CuiZipeng\\NewDirectory6'
    'wb')
# 关闭这个工作流
fp3.close()
# 删除文件夹
os.remove(
   'D:\\Users\\CuiZipeng\\NewDirectory4'
# 批量删除文件夹
shutil.move(
   'D:\\Users\\CuiZipeng\\NewDirectory1'，
   'D:\\Users\\CuiZipeng\\NewDirectory2'）
# 使用二进制读取文件夹
fp1 = open(
     'D:\\Users\\CuiZipeng\\NewDirectory4'，
    'rb+')
# 每次读取一行
fp1.readlines()
fp1.close()
# 对文件进行可读写两种操作（会首先自动清空文件内容）
fp4 = open(
    'D:\\Users\\CuiZipeng\\Text1.txt',
    'w+')
fp4.close()
# 对文件进行可读写两种操作（会首先自动清空文件内容）
fp5 = open(
    'D:\\Users\\CuiZipeng\\Text2.txt',
    'w+')
fp5.close()
# 对文件进行 w+（可读写两种操作（会首先自动清空文件内容））
fp6 = open(
    'D:\\Users\\CuiZipeng\\Text3.txt',
    'w+')
fp6.close()
# 删除文件
os.remove(
   'D:\\Users\\CuiZipeng\\Text2.txt')
# 批量删除文件
shutil.move(
    'D:\\Users\\CuiZipeng\\NewDirectory1'，
    'D:\\Users\\CuiZipeng\\NewDirectory2'）
# 打开该文件 并写入语句Life is short, study Python! 编码格式为utf-8
fp7 = open(
   'D:\\Users\\CuiZipeng\\Text4.txt',
    'w+', encoding='utf-8')
fp7.write("GOOD!")
fp7.readlines()
fp7.close()
# 打开该文件 并写入语句Life is short, study Python! 编码格式为utf-8  a+为追加读写两种操作

fp7 = open(
   'D:\\Users\\CuiZipeng\\Text4.txt',
    'a+', encoding='utf-8')
fp7.writelines('I love Ukraine!')
fp7.close()

def _init_(self, name, max_q_length=10086, max_data_size=13800, memory_limit=13800138, fs=None, persist_method=None,
           persist_params=None, file_io=None, db_io=None):
    self.name = name
    self.max_q_length = max_q_length
    self.max_data_size = max_data_size
    self.memory_limit = memory_limit
    self.fs = fs
    self.persist_method = persist_method
    self.persist_params = persist_params
    # IO method
    self.file_io = file_io
    self.db_io = db_io
    self.is_io = fs.not_bad(file_io)
    # standard property
    self.queue = []
    self.status = True
    self.meta_dict = {}
    self.usage_pct = 0