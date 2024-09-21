import os
from os import path
'''a = os.listdir()
b = list()

count = 0

for each in a:
    b.append(path.getsize(each))
    print(str(a[count]) + '【' + str(b[count]) + 'Bytes】')
    count += 1
    

dir_Direction = input('请输入待查找的初始目录：')
dir_Document = input('请输入需要查找的目标文件：')
menu = str(dir_Direction)
for root, dirs, files in os.walk(menu):
    if dir_Document in files:
        print(root + '\\' + dir_Document)
'''

all_files = os.listdir(os.curdir) # 使用os.curdir表示当前目录更标准
type_dict = dict()

for each_file in all_files:
    if os.path.isdir(each_file):
        type_dict.setdefault('文件夹', 0)
        type_dict['文件夹'] += 1
    else:
        ext = os.path.splitext(each_file)[1]
        type_dict.setdefault(ext, 0)
        type_dict[ext] += 1

for each_type in type_dict.keys():
    print('该文件夹下共有类型为【%s】的文件 %d 个' % (each_type, type_dict[each_type]))
