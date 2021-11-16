'''
注意，如果是读写文件的话，建议使用内置函数open()；
如果是路径相关的操作，建议使用os的子模块os.path；
如果要逐行读取多个文件，建议使用fileinput模块；
要创建临时文件或路径，建议使用tempfile模块；
要进行更高级的文件和路径操作则应当使用shutil模块
'''
#
import shutil
print(shutil.disk_usage('.\\basic IO.py'))
print(shutil.disk_usage('d:\\'))

#返回 cmd 调用的可执行文件路径，没有返回 None。mode：用于判断文件是否存在或可执行，path：cmd 的查找路径。示例如下：
print(shutil.which('python'))

# zipfile:生成文件名；归档 tmp 目录下文件和文件夹
#shutil.make_archive('zipfile', 'zip', 'tmp')

# 输出支持的归档格式
#shutil.unregister_archive_format('zip')
print(shutil.get_archive_formats())

# 注册和注销归档格式
'''
3）register_archive_format(name, function, extra_args=None, description='')

注册一个格式名并绑定到一个压缩时使用的程序，function 是用于解包存档文件的可调用函数。

4）unregister_archive_format(name)

从支持的归档格式中移除 name。
'''

print(shutil.get_unpack_formats())

#查询终端大小
print(shutil.get_terminal_size())