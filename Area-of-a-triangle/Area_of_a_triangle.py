#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017-7-17 19:20
# @Author  : Zhang Bin
# @Site    : office
# @File    : Area_of_a_triangle.py
# @Software: PyCharm Community Edition

# 计算三角形的面积

while 1 == 1:
    # 输入三角形的三条边
    a = input("输入三角形的第一条边，退出请输入'q'")
    # 判断是否退出
    if a == "q":
        print("已经退出")
        break
    b = input("输入三角形的第二条边，退出请输入'q'")
    # 判断是否退出
    if b == "q":
        print("已经退出")
        break
    c = input("输入三角形的第三条边，退出请输入'q'")
    # 判断是否退出
    if c == "q":
        print("已经退出")
        break
    a = float(a)
    b = float(b)
    c = float(c)
    # 判断是否符合三角形的必要条件
    if (a - b) < c and (a - c) < b and (b - c) < a and (a + b) > c and (a + c) > b and (b + c) > a:
        # 计算三角形的半周长
        s = (a + b + c) / 2
        # 计算三角形的面积
        area = (s * (s - a) * (s - c) * (s - b)) ** 0.5
        print("三角形的面积为{0:.2f}".format(area))
    else:
        print("您输入的三角形不正确！！！")
        continue

