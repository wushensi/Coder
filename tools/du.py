#__author__ = 'luchengjin'
# -*- coding: utf-8 -*-
import os
#4、获取文件大小
def getsize(file):
   return os.path.getsize(file)

#3、罗列path下有哪些目录及文件
def list(path):
   dirs={}#定义个存放目录的字典
   #罗列出path下所有的一级目录及文件
   for subitem in os.listdir(path):
      #3.1、判断subitem是否是目录
      if os.path.isdir(os.path.join(path,subitem)):
         dir_size=0#临时存储目录大小
         #os.walk遍历目录,取得所有文件
         for root,dir,files in os.walk(os.path.join(path,subitem)):
            for name in files:#每个目录下的文件清单
               try:
                  #累加文件夹下每个文件大小
                  dir_size +=getsize(os.path.join(root,name))
               except Exception:
                  pass
         dirs[subitem]=dir_size#添加目录及大小
         #dirs.update(subitem=dir_size)#添加目录及大小

      #3.2、文件处理
      elif os.path.isfile(os.path.join(path,subitem)):
         try:
            #计算文件大小,并加入到dir字典中
            dirs[subitem]=getsize(os.path.join(path,subitem))
         except Exception:
            pass
   #对目录或文件大小排序;把字典转化为列表，按照value进行降序排序
   result=sorted(dirs.items(),key=lambda d:d[1],reverse=True)
   #输出目录大小
   for item in result:
      fileName = item[0]
      fileSize=item[1]
      caculatedSize=''
      if fileSize>=1073741824:
         caculatedSize=str(fileSize/1024/1024/1024)+' GB'
      elif fileSize>=106496 and fileSize<=1073741824:
         caculatedSize=str(fileSize/1024/1024)+' MB'
      elif fileSize<106496:
         caculatedSize=str(fileSize/1024)+' KB'
      print('%-50s %50s'%(fileName,caculatedSize))

#2、定义用户输入的函数,用户输入n/N,就停止这个程序,输入路径就调用list函数,统计目录及文件
def start():
    isNext=1 #定义一个是否继续让用户输入path的变量
    while isNext==1:#isNext==1,就继续循环这个输入、处理的过程
        path = input("enter path (d:\\\),stop enter n/N: ")#raw_input让用户输入,并获取输入内容
        if path=='n' or path=='N':#如果用户输入的死n/N,isNext赋值0,执行完就不在执行了
            isNext=0
        else:
            list(path)#反之,调用list(path)函数,将path交给list处理

#1、开始执行这个文件时,先从start作为main函数开始执行
if __name__=='__main__':
    start()