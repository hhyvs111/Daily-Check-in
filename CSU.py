#!usr/bin/python
# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import notify


def check_in():
    driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    driver.get('https://wxxy.csu.edu.cn/ncov/wap/default/index')
    #读取账户密码
    #用绝对路径了
    with open('/Users/tanwenbo/PycharmProjects/Daily-Check-in/AccountInfo/csu.txt', 'r') as f:
        lines = f.readlines()

    username = lines[0].strip('\n')
    password = lines[1].strip('\n')
    username_key = driver.find_element_by_id('userName')
    username_key.send_keys(username)

    password_key = driver.find_element_by_id('passWord')
    password_key.send_keys(password)

    driver.find_element_by_id('login-btn').click()
    time.sleep(3)

    driver.get('https://wxxy.csu.edu.cn/ncov/wap/default/index')
    driver.find_element_by_name('area').click()

    time.sleep(2)
    driver.find_element_by_class_name('footers').click()
    time.sleep(2)

    try:
        driver.find_element_by_class_name('wapcf-btn-ok').click()
        print("%s 打卡成功！" % username)
        notify.notify_to_wx("中南健康打卡", "打卡成功！")
    except:
        driver.find_element_by_class_name('wapat-btn-ok').click()
        print("%s 你今天已经打卡了" % username)
        notify.notify_to_wx("中南健康打卡", "你已经打过卡了！")
    driver.quit()


if __name__ == '__main__':
    check_in()

