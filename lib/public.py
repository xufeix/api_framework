# /usr/bin/env python3.8
# coding:utf-8

"""
@file: public.py
@time: 2021/5/12 2:53 下午
@author:XF
"""

import os
import unittest
import time
import requests
from utils.mySettings import url


#  获取项目根目录
def getRootDir():
    # os.path.abspath(
    #   __file__)  # os.path.abspath方法是获取绝对路径（这样别人用此代码也可以根据绝对路径找到），file变量代表文件本身，比如现在这个file变量就代表了public.py(在哪个文件里就代表谁)
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# 获取测试用例
def getTestCase():
    #  用来加载testcase到TestSuite
    loder = unittest.TestLoader()
    #  获取测试用例所在路径
    caseDir = os.path.join(getRootDir(), "testcase")
    #  加载测试用例
    suite = loder.discover(caseDir)
    return suite


#  获取测试报告
def getReport():
    #  获取测试报告路径
    caseDir = os.path.join(getRootDir(), 'report')
    #  拼接一个完整的测试报告名称：报告目录+时间戳+HTML文件后缀名
    return os.path.join(caseDir, ('%s' % time.time()).split('.')[0] + '.html')


#  发送请求
def postRequest(path, parameters):
    data = requests.post(url=''.join([url, path]), json=parameters)
    return data
