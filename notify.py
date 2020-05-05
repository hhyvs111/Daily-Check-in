#!usr/bin/python
# -*- coding:utf-8 -*-

import requests


def notify_to_wx(title, result):
    with open('../AccountInfo/server_key.txt', 'r') as f:
        key = f.readlines()
    url = "https://sc.ftqq.com/%s.send" % key[0]
    print url
    content = "%s 打卡情况 %s" % (title, result)

    print content

    data = {
        'text': title + result,
        'desp': content
    }

    requests.post(url, data=data)


if __name__ == '__main__':
    notify_to_wx("健康打卡", "成功")