# Time: 2021/3/23 16:29
# Author: 阿尔法
# File: 滑块验证码.py
# @Software: PyCharm
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import time, random
from lxml import etree
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ActionChains

def main():
    # 1、url + headers
    login_url = r'https://login.taobao.com/member/login.jhtml'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/87.0.4280.88 Safari/537.36'
    }

    # 2、创建driver对象, 设置无头模式
    option = ChromeOptions()
    option.add_argument(r'--headless')
    driver_path = r'D:\selenium\chromedriver.exe'
    # driver = webdriver.Chrome(executable_path=driver_path)
    driver = webdriver.Chrome()
    # 防检测
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",
                           {"source": """ Object.defineProperty(navigator, 'webdriver', { get: () => undefined }) """})
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    # 3、登录淘宝, 输入用户名，密码，按住滑块 向右移动
    driver.get(login_url)
    driver.find_element_by_id(r'fm-login-id').send_keys()
    time.sleep(1)
    driver.find_element_by_id(r'fm-login-password').send_keys()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()
    time.sleep(1)
    """加一个弹出验证码的判断，比如获取"""
    text = driver.find_element_by_xpath('//*[@id="J_Col_Main"]/div/div[1]/div/div[1]/div[1]/div/div[1]/a/em/text()')
    try:
        if not text is None:
            print('登录成功:', text)
    except:


        # 滑动验证
        button = driver.find_element_by_class_name('nc_iconfont btn_slide')
        ActionChains(driver).drag_and_drop(button).perform()
        action = ActionChains(driver)
        a = driver.find_element_by_xpath('//*[@id="nc_1_n1z"]')
        # iframe标签切换
        iframe = driver.find_element_by_tag_name("iframe")
        driver.switch_to.frame(iframe)
        """方法一"""
        # # 获取滑块的大小
        # span_background = driver.find_element_by_xpath('//*[@id="nc_1__scale_text"]/span')
        # span_background_size = span_background.size
        # print(span_background_size)
        #
        # # 获取滑块的位置
        # button = driver.find_element_by_xpath('//*[@id="nc_1_n1z"]')
        # button_location = button.location
        # print(button_location)
        #
        # # 拖动操作：drag_and_drop_by_offset
        # # 将滑块的位置由初始位置，右移一个滑动条长度（即为x坐标在滑块位置基础上，加上滑动条的长度，y坐标保持滑块的坐标位置）
        # x_location = span_background_size["width"]
        # y_location = button_location["y"]
        # print(x_location, y_location)
        # action = ActionChains(driver)
        # source = driver.find_element_by_xpath('//*[@id="nc_1_n1z"]')
        # action.click_and_hold(source).perform()
        # action.move_by_offset(300, 0)
        # action.release().perform()
        # time.sleep(1)
        #
        # # 登录
        # driver.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()
        # print('登录成功\n')
        """方法二"""
        # while True:
        #     try:
        #         # 定位滑块元素
        #         source = driver.find_element_by_xpath("//*[@id='nc_1_n1z']")
        #         # 定义鼠标拖放动作
        #         ActionChains(driver).drag_and_drop_by_offset(source, 300, 0).perform()
        #         # 等待JS认证运行,如果不等待容易报错
        #         time.sleep(2)
        #         # 查看是否认证成功，获取text值
        #         text = driver.find_element_by_xpath("//div[@id='nc_1__scale_text']/span")
        #         # 目前只碰到3种情况：成功（请在在下方输入验证码,请点击图）；无响应（请按住滑块拖动)；失败（哎呀，失败了，请刷新）
        #         if text.text.startswith(u'请在下方'):
        #             print('成功滑动')
        #             break
        #         if text.text.startswith(u'请点击'):
        #             print('成功滑动')
        #             break
        #         if text.text.startswith(u'请按住'):
        #             continue
        #     except Exception as e:
        #         # 这里定位失败后的刷新按钮，重新加载滑块模块
        #         driver.find_element_by_xpath('//*[@id="nocaptcha"]/div/span/a').click()
        """方法三"""
        # 定位滑块元素
        source = driver.find_element_by_xpath("//*[@id='nc_1_n1z']")
        action = ActionChains(driver)
        x = 0
        while x < 50:
            x += 100
            action.click_and_hold(source).move_by_offset(x, 0).perform()
            time.sleep(0.1)
        # return
        # # 4、登录完成后，点击"淘宝网首页"进入淘宝主页
        # driver.find_element_by_xpath(r'//*[@id="J_SiteNavHome"]/div/a/span').click()
        #
        # # 5、搜索内容
        # driver.find_element_by_class_name(r'//*[@id="q"]').send_keys(r'iphone X')
        # driver.find_element_by_class_name(r'//*[@id="J_TSearchForm"]/div[1]/button').click()
        #
        # # 6、得到响应数据，并且变成xpath对象
        # response = driver.page_source
        # html_str = etree.HTML(response)
        #
        # # 7、解析得到 商品名称， 商品价格， 付款人数， 卖家地点， 卖家店名
        # shop_names = html_str.xpath(r'//div[@class="items"]//div[@class="ctx-box J_MouseEneterLeave J_IconMoreNew"]//a[@class="J_ClickStat"]/span/text()')



if __name__ == '__main__':
    main()








# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from time import sleep
# driver_path = r'D:\selenium\chromedriver.exe'
# driver = webdriver.Chrome(executable_path=driver_path)
# driver.maximize_window()
# driver.get('https://passport.ctrip.com/user/reg/home')
# driver.find_element_by_css_selector("#agr_pop>div.pop_footer>a.reg_btn.reg_agree").click()
# sleep(5)
# # 获取滑块位置
# sour=driver.find_element_by_css_selector("#slideCode>div.cpt-drop-box>div.cpt-drop-btn")
# ele=driver.find_element_by_css_selector("#slideCode>div.cpt-drop-box>div.cpt-bg-bar")
# # 拖动滑块
# ActionChains(driver).drag_and_drop_by_offset(sour,ele.size['width'],-sour.size['height']).perform()





























