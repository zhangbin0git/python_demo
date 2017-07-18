#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017-7-18 18:06
# @Author  : Zhang Bin
# @Site    : office
# @File    : Generate calendar.py
# @Software: PyCharm Community Edition

# 引入日历模块
import calendar
# 输入年月
yy = int(input("输入年份"))
mm = int(input("输入月份"))

# 显示日历
print(calendar.month(yy,mm))
