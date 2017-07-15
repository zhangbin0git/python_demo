#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/7/15 19:57
# @Author  : Zhang Bin
# @Site    : office
# @File    : Python_judges_odd_even_numbers.py
# @Software: PyCharm Community Edition

# python 判断奇偶数
# 开启循环
while 1 == 1:
    # 输入一个数字
    num = input("请输入一个数字,如果您要退出请输入‘q’！")
    if num == "q":
        print("已经退出循环")
        break
    else:
        num = int(num)
        # 如果除以2为余数0为偶数
        # 偶然位奇数
        if (num % 2) == 0:
            print("数字{0}是偶数".format(num))
        else:
            print("数字{0}是奇数".format(num))
# END
