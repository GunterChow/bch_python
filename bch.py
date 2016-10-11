#!/usr/bin/python
#coding:utf-8
import encode
import decode
import data
import glob
import error
'''-----------------------测试模式选择--------------------------------'''
test = 'y'
while test == 'y':
    while True:
        mod = raw_input("请输入测试数据模式(s--固定数据测试，r--随机数据测试):")
        print " "
        origin_data = []
        if mod == 'r':
            origin_data = data.rand_data()
            break
        elif mod == 's':
            origin_data = data.static_data()
            break
        elif mod == 'q':
            break
        else :
            print "输入有误！！"
            print " "
    '''----------------------BCH编码-------------------------'''    
    print "origin_data =%x" % glob.list2int(origin_data)
    print " "
    check_data = []
    check_data = encode.encode(origin_data)[:]
    encode_data = []
    encode_data = origin_data[:]
    encode_data.extend(check_data)
    '''-------------------产生随机错误-----------------------'''
    error.error(encode_data)
    '''-----------------------BCH译码------------------------'''
    correct_data = []
    correct_data = decode.decode(encode_data)[:]
    '''----------------------判断----------------------------'''
    print "error_data  =%x" % glob.list2int(encode_data)
    print " "
    #print "correct_data=%x" % glob.list2int(correct_data[:4096])

    if correct_data[:4096] == origin_data:
        print "#"*50
        print "************       correct          **************"
        print "#"*50
    else :
        print "#"*50
        print "************         error          **************"
        print "#"*50
    print " "
    test = raw_input("继续测试吗？[y/n]:")
