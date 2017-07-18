#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017-7-18 18:11
# @Author  : Zhang Bin
# @Site    : office
# @File    : python_IO.py
# @Software: PyCharm Community Edition

# write a file
with open('text.txt', 'w') as out_file:
    out_file.write("该文本会现在文件中\n看到了吧")

# read a file
with open('text.txt', 'r') as in_file:
    text = in_file.read()
# 对比
with open('text.txt', 'r') as in_file:
    text1 = in_file.readlines()

# 屏幕显示
print(text)
print(type(text))
