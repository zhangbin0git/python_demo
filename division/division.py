#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017-7-25 17:54
# @Author  : Zhang Bin
# @Site    : office
# @File    : division.py
# @Software: PyCharm Community Edition
# 使用try-except-else排除除以0的错误
print("Give me two numbers,and I'll divide them.")
print("Enter 'q' to quit.")
file_name = "zhangbin.txt"
# 开始循环提问
while True:
    # 输入第一个数字
    first_number = input("\n请输入第一个数字！")
    # 如输入“q”退出
    if first_number == "q":
        break
    # 输入第二个数字
    second_number = input("请输入第二个数字！")
    # 如输入“q“退出
    if second_number == "q":
        break
    # 开始计算结果
    try:
        answer = int(first_number)/int(second_number)
    # 发现错误是报错
    except ZeroDivisionError:
        print("You can't divide by 0")
    # 发生输入类型错误
    except ValueError:
        print("输入类型不匹配！")
    # 输出正确的结果
    else:
        print(answer)
        try:
            with open(file_name, 'r') as out_file:
                contents = out_file.read()
        except FileNotFoundError:
            Msg = "Sorry, the file " + file_name + " does not exist."
            print(Msg)
        else:
            print(contents)

