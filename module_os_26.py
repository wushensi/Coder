'''
注意，如果是读写文件的话，建议使用内置函数open()；
如果是路径相关的操作，建议使用os的子模块os.path；
如果要逐行读取多个文件，建议使用fileinput模块；
要创建临时文件或路径，建议使用tempfile模块；
要进行更高级的文件和路径操作则应当使用shutil模块
'''
import os
def get_filelists(file_dir='.'):
    list_directory = os.listdir(file_dir)
    filelists = []
    for directory in list_directory:
        # os.path 模块稍后会讲到
        if(os.path.isfile(directory)):
            filelists.append(directory)
    return filelists
#获取当前路径下的文件
print(get_filelists())

with open("basic IO.py", encoding="utf-8") as f:
    print(f.read())
