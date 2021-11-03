import os
import shutil
import sys

# python OS 标准库
'''
os.name                        获取操作系统平台
  os.environ                    一个 dictionary 包含环境变量的映射关系
  print(os.environ)             输出环境变量值
  os.system()                   用来运行shell命令
  os.chdir(dir)                 改变当前目录 
  os.chdir(‘F:\WprkSpace’)      注意符号转义
  os.getegid()                  得到有效组id
  os.getgid()                   得到组id
  os.getuid()                   得到用户id
  os.geteuid()                  得到有效用户id
  os.setegid os.setegid() os.seteuid() os.setuid()  设置id
  os.getgruops()                得到用户组名称列表
  os.getlogin()                 得到用户登录名称
  os.getenv                     得到环境变量
  os.putenv                     设置环境变量
  os.umask                      设置umask
  os.system(cmd)                利用系统调用，运行cmd命令
'''

print(os.getcwd())

#print(os.getegid()) 针对特定系统

#print(os.getgroups()) 针对特定系统

print(os.getlogin())

print(os.getenv("path"))

#os.system('calc')

#python 文件和目录操作

'''



  os.getcwd()                   # 获取现在的工作目录
  os.listdir()                  获取某个目录下的所有文件名
  os.remove()                   删除某个文件
  os.path.exists()              检验给出的路径是否真地存在
  os.path.isfile()              判断是否为文件;若是，返回值为真
  os.path.isdir()               判断是否为文件夹;若是，返回值为真
  os.path.abspath(name)         获得绝对路径
  os.path.splitext()            分离文件名与扩展名
  os.path.split()               把一个路径拆分为目录+文件名的形式
  os.path.join(path,name)       连接目录与文件名或目录
  os.path.basename(path)        返回文件名
  os.path.dirname(path)         返回文件路径
'''

print( os.listdir())

print(os.path.abspath('basic IO.py'))

#shutil 模块 -高级文件操作
'''

# 将文件内容拷贝到另一个文件中
shutil.copyfileobj(fsrc, fdst[, length])

# 拷贝文件
shutil.copyfile(src, dst, *, follow_symlinks=True)

# 仅拷贝权限。内容、组、用户均不变
shutil.copymode(src, dst)

# 仅拷贝状态信息，包括：mode bits, atime, mtime, flags
shutil.copystat(src, dst)

# 拷贝文件和权限
shutil.copy(src, dst)

# 拷贝文件和状态信息
shutil.copy2(src, dst)

# 递归的去拷贝文件夹
shutil.ignore_patterns(*patterns)
shutil.copytree(src, dst, symlinks=False, ignore=None)

# 递归删除文件夹
shutil.rmtree(path[, ignore_errors[, onerror]])

# 递归的去移动文件，它类似mv命令，其实就是重命名。
shutil.move(src, dst)

# 创建压缩包并返回文件路径，例如：zip、tar
shutil.make_archive(base_name, format,...)
'''
shutil.copyfile('basic IO.py','D:\\六壬网安\\1103\\IO.py')

#shutil.make_archive('D:\\六壬网安\\1103\\IO.py', 'zip')

#错误输出重定向和终止程序
sys.stderr.write('Warning, log file not found starting a new one\n')

