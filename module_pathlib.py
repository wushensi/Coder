'''
使用 pathlib 模块，相比于 os 模块可以写出更简洁，易读的代码。pathlib 模块中的 Path 类继承自 PurePath，对 PurePath 中的部分方法进行了重载，相比于 os.path 有更高的抽象级别。本文将带你学习如何使用 pathlib 模块中的 Path 类读写文件、操纵文件路径和基础文件系统，统计目录下的文件类型以及查找匹配目录下某一类型文件等
'''

# 获取目录
from pathlib import Path
currentPath = Path.cwd()
homePath = Path.home()
print("文件当前所在目录:%s\n用户主目录:%s" %(currentPath, homePath))

# 拼接目录
currentPath = Path.cwd()
newPath = currentPath / 'python-100'
print("新目录为:%s" %(newPath))

# 创建 删除目录
#homePath = Path.home()
#makePath = homePath / 'python-100'
#makePath.mkdir()
#print("创建的目录为:%s" %(makePath))

#currentPath = Path.home()
#delPath = currentPath / 'python-100'
#delPath.rmdir()
#print("删除的目录为:%s" %(delPath))

'''
Path.open(mode='r')，以 "r" 格式打开 Path 路径下的文件，若文件不存在即创建后打开。
Path.read_bytes()，打开 Path 路径下的文件，以字节流格式读取文件内容，等同 open 操作文件的 "rb" 格式。
Path.read_text()，打开 Path 路径下的文件，以 str 格式读取文件内容，等同 open 操作文件的 "r" 格式。
Path.write_bytes()，对 Path 路径下的文件进行写操作，等同 open 操作文件的 "wb" 格式。
Path.write_text()，对 Path 路径下的文件进行写操作，等同 open 操作文件的 "w" 格式。
'''
#currentPath = Path.home()
#mkPath = currentPath / 'python-100.txt'
#with mkPath.open('w') as f:  # 创建并以 "w" 格式打开 python-100.txt 文件。
#    f.write('python-100')  # 写入 python-100 字符串。
#f = open(mkPath, 'r')
#print("读取的文件内容为:%s" % f.read())
#f.close()

#currentPath = Path.home()
#mkPathText = currentPath / 'python-100-text.txt'
#mkPathText.write_text('python-100')
#print("读取的文件内容为:%s" % mkPathText.read_text())

#currentPath = Path.home()
#str2byte = bytes('python-100', encoding = 'utf-8')
#mkPathByte = currentPath / 'python-100-byte.txt'
#mkPathByte.write_bytes(str2byte)
#print("读取的文件内容为:%s" % mkPathByte.read_bytes())

'''
Path.resolve()，通过传入文件名，返回文件的完整路径。
Path.name，可以获取文件的名字，包含后缀名。
Path.parent，返回文件所在文件夹的名字。
Path.stem，获取文件名不包含后缀名。
Path.suffix，获取文件的后缀名。
Path.anchor，获取文件所在的盘符。
'''

#txtPath = Path('users.json')
#nowPath = txtPath.resolve()
#print("文件的完整路径为:%s" % nowPath)
#print("文件完整名称为(文件名+后缀名):%s" % nowPath.name)
#print("文件名为:%s" % nowPath.stem)
#print("文件后缀名为:%s" % nowPath.suffix)
#print("文件所在的文件夹名为:%s" % nowPath.parent)
#print("文件所在的盘符为:%s" % nowPath.anchor)

'''
Path.exists()，判断 Path 路径是否指向一个已存在的文件或目录，返回 True 或 False。
Path.is_dir()，判断 Path 是否是一个路径，返回 True 或 False。
Path.is_file()，判断 Path 是否指向一个文件，返回 True 或 False。
'''

#currentPath = Path.home() / 'python'
#
#print(currentPath.exists())  # 判断是否存在 python 文件夹，此时返回 False。
#print(currentPath.is_dir())  # 判断是否存在 python 文件夹，此时返回 False。
#
#currentPath.mkdir()  # 创建 python 文件夹。
#
#print(currentPath.exists())  # 判断是否存在 python 文件夹，此时返回 True。
#print(currentPath.is_dir())  # 判断是否存在 python 文件夹，此时返回 True。
#
#currentPath = Path.home() / 'python-100.txt'
#
#print(currentPath.exists())  # 判断是否存在 python-100.txt 文件，此时文件未创建返回 False。
#print(currentPath.is_file())  # 判断是否存在 python-100.txt 文件，此时文件未创建返回 False。
#
#f = open(currentPath,'w')  # 创建 python-100.txt 文件。
#f.close()
#
#print(currentPath.exists())  # 判断是否存在 python-100.txt 文件，此时返回 True。
#print(currentPath.is_file())  # 判断是否存在 python-100.txt 文件，此时返回 True。

'''
Path.iterdir()，返回 Path 目录文件夹下的所有文件，返回的是一个生成器类型。
Path.glob(pattern)，返回 Path 目录文件夹下所有与 pattern 匹配的文件，返回的是一个生成器类型。
Path.rglob(pattern)，返回 Path 路径下所有子文件夹中与 pattern 匹配的文件，返回的是一个生成器类型。
'''
from collections import Counter
currentPath = Path.cwd()
gen = (i.suffix for i in currentPath.iterdir())
print(Counter(gen))
gen = (i.suffix for i in currentPath.glob('*.txt'))  # 获取当前文件下的所有 txt 文件，并统计其个数。
print(Counter(gen))
gen = (i.suffix for i in currentPath.rglob('*.txt'))  # 获取目录中子文件夹下的所有 txt 文件，并统计其个数。
print(Counter(gen))