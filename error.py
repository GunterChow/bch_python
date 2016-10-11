#!/usr/bin/python
#coding:utf-8
import glob
import random

n = glob.bch_n
bch_t = glob.t
'''---------------------参数随机错误位-----------------------'''
def error(data):
    t = raw_input("请输入错误个数（最大纠错能力：%d位）：" % bch_t)
    err = []
    for i in range(int(t)):
        error = random.randint(0,n)
        while error in err:
            error = random.randint(0,n)
        err.append(error)
    for j in range(int(t)):
        if data[err[j]] == 1:
            data[err[j]] = 0
        else :
            data[err[j]] = 1


