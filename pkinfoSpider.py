#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   pkinfoSpider.py
@Time    :   2019/11/24 19:04:48
@Author  :   liajihua
@Version :   1.0
@Contact :   840132699@qq.com
@Desc    :   None
'''

# here put the import lib
import requests
from lxml import etree
import json
import csv
import time
import random


# 获取网页源代码
def get_page(url):
    # headers = {
    #     'USER-AGENT':
    #     'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    # }
    response = requests.get(url=url)
    html = response.text

    return html


# 解析网页源代码，获取下一页链接
def parse4link(html, base_url, index):
    link = None
    index += 3
    html_elem = etree.HTML(html)
    # 获取a标签的属性4开始
    url = html_elem.xpath(
        '//*[@id="mw-content-text"]/div/table[1]/tbody/tr[%s]/td[2]/a/@href' %
        index)

    if url:
        link = base_url + url[0]
        print(link)

    return link


# 解析网页源代码，获取数据
def parse4data(html):
    pkdex_content = etree.HTML(html)
    # xpath后面/text()获取文本 @title 获取title属性值
    # 多形态的属性，如喷火龙X,这时候只取默认形态的信息
    POLY_XPATH = None

    # 多形态的种族值，如喷火龙X,这时候只取种族值会改变，这时取原始形态的种族值
    STRENGTH_XPATH = None
    # 判断有无多形态，有则添加POLY_XPATH，STRENGTH_XPATH
    isPoly = pkdex_content.xpath('//tr[contains(@class,"_toggle form1")]')

    isStrength = pkdex_content.xpath(
        '//div[@class="tabbertab  tabbertabhide"]')
    #是否区分世代
    isExpGen = pkdex_content.xpath(
        '//table[contains(@class,"roundy a-r at-c")]//table[@class="roundy bgwhite fulltable"]//td[1]/span[contains(@original-title,"第五世代起")]/text()'
    )
    if isPoly != []:
        POLY_XPATH = '//tr[contains(@class,"_toggle form1")]'
        print("有多形态信息")
    else:
        POLY_XPATH = ''
        print("没有多形态信息")

    if isStrength != []:
        STRENGTH_XPATH = '//div[@class="tabbertab"]'
        print("有多形态种族值")

    else:
        STRENGTH_XPATH = ''
        print("没有多形态种族值")
    print(isExpGen)
    if isExpGen != []:
        Gen_XPATH = POLY_XPATH + '//table[contains(@class,"roundy a-r at-c")]//table[@class="roundy bgwhite fulltable"]//td[1]/span[contains(@original-title,"第一世代至第四世代")]/text()'
        print("区分世代经验值")
    else:
        Gen_XPATH = POLY_XPATH + '//table[contains(@class,"roundy a-r at-c")]//table[@class="roundy bgwhite fulltable"]//td[contains(string(),"基础经验值")]'

        print("没有区分世代经验值")

    # 编号
    serialNum = pkdex_content.xpath(
        POLY_XPATH +
        '//table[contains(@class,"roundy a-r at-c")]//tr[1]//a[contains(@title,"宝可梦列表（按全国图鉴编号）")]/text()'
    )
    # 名称
    pkmon_name = pkdex_content.xpath(
        POLY_XPATH +
        '//table[contains(@class,"roundy a-r at-c")]//td//span//b/text()')
    # 属性//*[@id="mw-content-text"]/div/table[2]/tbody/tr[1]/td/table/tbody/tr[3]/td[1]/table/tbody/tr/td/table/tbody/tr/td/span[1]/a

    pkmon_type = pkdex_content.xpath(
        POLY_XPATH +
        '//table[@class="roundy bgwhite fulltable"]//tr[1]//td[contains(@class,"roundy")]/span/a/text()'
    )
    print("%s个属性" % len(pkmon_type))

    # 特性
    ability = pkdex_content.xpath(
        POLY_XPATH +
        '//table[@class="roundy bgwhite fulltable"]//tr[1]/td[1]/a[contains(@title,"特性")]/text()'
    )
    print(ability)
    print("%s个普通特性" % len(ability))

    # 梦特
    hidden_ability = pkdex_content.xpath(
        POLY_XPATH +
        '//table[@class="roundy bgwhite fulltable"]//tr[1]/td[2]/a[contains(@title,"特性")]/text()'
    )
    print(hidden_ability)

    # 基础经验值
    base_exp = pkdex_content.xpath(Gen_XPATH)
    #print(type(base_exp))
    # 体力值

    hp_value = pkdex_content.xpath(
        STRENGTH_XPATH +
        '//table[@class="bg-HP bd-HP bw-1"]//th[@class="bgl-HP"]/text()')

    # 攻击值
    atk_value = pkdex_content.xpath(
        STRENGTH_XPATH +
        '//table[@class="bg-攻击 bd-攻击 bw-1"]//th[@class="bgl-攻击"]/text()')
    # 防御
    defend_value = pkdex_content.xpath(
        STRENGTH_XPATH +
        '//table[@class="bg-防御 bd-防御 bw-1"]//th[@class="bgl-防御"]/text()')
    # 特攻
    atk_sp_value = pkdex_content.xpath(
        STRENGTH_XPATH +
        '//table[@class="bg-特攻 bd-特攻 bw-1"]//th[@class="bgl-特攻"]/text()')

    # 特防
    defend_sp_value = pkdex_content.xpath(
        STRENGTH_XPATH +
        '//table[@class="bg-特防 bd-特防 bw-1"]//th[@class="bgl-特防"]/text()')
    # 速度
    speed_value = pkdex_content.xpath(
        STRENGTH_XPATH +
        '//table[@class="bg-速度 bd-速度 bw-1"]//th[@class="bgl-速度"]/text()')

    # 如果有两个属性
    if len(pkmon_type) >= 2:
        pkmon_type1 = [pkmon_type[0].replace(u'\xa0', u'')]
        pkmon_type2 = [pkmon_type[1].replace(u'\xa0', u'')]

    else:
        pkmon_type1 = ["".join(pkmon_type).replace(u'\xa0', u'')]
        pkmon_type2 = [""]
    # 如果有两个特性
    if len(ability) >= 2:
        ability1 = [ability[0]]
        ability2 = [ability[1]]
    else:
        ability1 = ability
        ability2 = [""]
    # 如果有两个形态

    if len(hp_value) >= 2:
        serialNum = [serialNum[0].replace('\n', '')]
        pkmon_name = [pkmon_name[0].replace('\n', '')]
        atk_value = [atk_value[0].replace('\n', '')]
        atk_sp_value = [atk_sp_value[0].replace('\n', '')]
        defend_value = [defend_value[0].replace('\n', '')]
        defend_sp_value = [defend_sp_value[0].replace('\n', '')]
        hp_value = [hp_value[0].replace('\n', '')]
        speed_value = [speed_value[0].replace('\n', '')]
    else:
        serialNum = ["".join(serialNum).replace(u'\n', u'')]
        pkmon_name = ["".join(pkmon_name).replace(u'\n', u'')]
        atk_value = ["".join(atk_value).replace(u'\n', u'')]
        atk_sp_value = ["".join(atk_sp_value).replace(u'\n', u'')]
        defend_value = ["".join(defend_value).replace(u'\n', u'')]
        defend_sp_value = ["".join(defend_sp_value).replace(u'\n', u'')]
        hp_value = ["".join(hp_value).replace(u'\n', u'')]
        speed_value = ["".join(speed_value).replace(u'\n', u'')]

    print(serialNum, pkmon_name, pkmon_type1, pkmon_type2, ability1, ability2,
          hidden_ability, hp_value, atk_value, defend_value, atk_sp_value,
          defend_sp_value, speed_value)

    data = zip(serialNum, pkmon_name, pkmon_type1, pkmon_type2, ability1,
               ability2, hidden_ability, hp_value, atk_value, defend_value,
               atk_sp_value, defend_sp_value, speed_value)
    return data


# 打开文件
def openfile(fm):
    fd = None
    if fm == 'txt':
        fd = open('pkmondex.txt', 'w', encoding='utf-8')
    elif fm == 'json':
        fd = open('pkmondex.json', 'w', encoding='utf-8')
    elif fm == 'csv':
        fd = open('pkmondex.csv', 'a+', encoding='utf-8', newline='')
    return fd


# 将数据保存到文件
def save2file(fm, fd, data):
    if fm == 'txt':
        for item in data:
            fd.write('----------------------------------------\n')
            fd.write('' + str(item[0]) + '\n')
            fd.write('' + str(item[1]) + '\n')
            fd.write('' + str(item[2]) + '\n')
            fd.write('' + str(item[3]) + '\n')
    if fm == 'json':
        temp = ('agree', 'authod', 'star', 'content')
        for item in data:
            json.dump(dict(zip(temp, item)), fd, ensure_ascii=False)
    if fm == 'csv':
        writer = csv.writer(fd)
        for item in data:
            writer.writerow(item)


# 开始爬取网页
def crawl():
    base_url = 'https://wiki.52poke.com/'
    # fm = input('请输入文件保存格式（txt、json、csv）：')
    # while fm != 'txt' and fm != 'json' and fm != 'csv':
    #     fm = input('输入错误，请重新输入文件保存格式（txt、json、csv）：')
    # 采集宝可梦数量
    start_num = 1
    end_num = 386
    fm = 'csv'
    fd = openfile(fm)
    print('开始爬取')
    pkdex_url = base_url + 'wiki/%E5%AE%9D%E5%8F%AF%E6%A2%A6%E5%88%97%E8%A1%A8%EF%BC%88%E6%8C%89%E5%85%A8%E5%9B%BD%E5%9B%BE%E9%89%B4%E7%BC%96%E5%8F%B7%EF%BC%89/%E7%AE%80%E5%8D%95%E7%89%88'
    for i in range(start_num, end_num):
        html = get_page(pkdex_url)
        link = parse4link(html, base_url, i)

        # print('正在爬取 ' + str(link) + ' ......')
        pkmonHtml = get_page(link)

        data = parse4data(pkmonHtml)

        save2file(fm, fd, data)
    #time.sleep(random.random())

    fd.close()
    print('结束爬取')


if __name__ == '__main__':
    crawl()
