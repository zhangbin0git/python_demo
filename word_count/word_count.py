#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017-7-25 18:28
# @Author  : Zhang Bin
# @Site    : office
# @File    : word_count.py
# @Software: PyCharm Community Edition
# 用函数方法计算多个文档的字数
def count_words(file_name):
    """计算一个文件有多少个单词"""
    try:
        # 打开文件
        with open(file_name, 'r', encoding='utf-8') as open_file:
            contents = open_file.read()
    # 防止无文件错误
    except FileNotFoundError:
        print("Sorry, the file " + " does not exist.")
    else:
        # 计算字符量并输出
        words = contents.split()
        words_num = len(words)
        print("The file " + file_name + " has about " + str(words_num) +
              " words")
# 计算多个文件的字符量
file_name = ["txt/Oratory  Sacred.txt", "txt/Poetical Works.txt",
             "txt/The Irish Penny.txt"]
# 开启循环
for i in file_name:
    # 使用函数方法计算
    count_words(i)


