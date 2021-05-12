# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : demo.py
# @ide     : PyCharm
# @time    : 2021/4/6 15:18
from selenium import webdriver
import allure
import time


def test_steps_demo1():
    with allure.step("打开百度网页"):
        driver = webdriver.Chrome()
        driver.get("https://www.baidu.com/")

    with allure.step("搜索关键词"):
        driver.find_element_by_id("kw").send_keys("松勤")
        driver.find_element_by_id("su").click()

    with allure.step("保存图片"):
        driver.save_screenshot("./a.png")
        allure.attach.file("./a.png", attachment_type=allure.attachment_type.PNG)

    with allure.step("退出浏览器"):
        driver.quit()

def test_steps_demo2():
    with allure.step("打开百度网页"):
        driver = webdriver.Chrome()
        driver.get("https://www.baidu.com/")

    with allure.step("搜索关键词"):
        driver.find_element_by_id("kw").send_keys("松勤")
        driver.find_element_by_id("su").click()

    with allure.step("保存图片"):
        driver.save_screenshot("./a.png")
        allure.attach.file("./a.png", attachment_type=allure.attachment_type.PNG)

    with allure.step("退出浏览器"):
        driver.quit()

# # 打开一个浏览器
# driver = webdriver.Chrome()
#
# # 访问网址
# driver.get("https://www.baidu.com/")
#
# # 通过 id寻找元素并输入内容
# driver.find_element_by_id("kw").send_keys("松勤")
# # 通过id 寻找元素并点击
# driver.find_element_by_id("su").click()
#
# time.sleep(1)
# # 对整个页面截图
# driver.save_screenshot("./a.png")
