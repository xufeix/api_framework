# /usr/bin/env python3.8
# coding:utf-8

"""
@file: run.py
@time: 2021/5/12 8:44 上午
@author:XF
"""
from package.HTMLTestRunner_cn import HTMLTestRunner
from lib.public import getReport, getTestCase


def run():
    with open(getReport(), 'wb') as f:
        ruuner = HTMLTestRunner(f, verbosity=2, title='徐飞孙志杰加油', description='接口自动化python+unittest')
        ruuner.run(getTestCase())


if __name__ == '__main__':
    run()
