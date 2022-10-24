# 27、项目架构设计以及如何通过pyautogui去坐标定位实现单击，问题：不能正常选中的原因可能是checkbox不规范，或者反爬虫代码多种原因
# 由于使用坐标定位存在偏移量，这个偏移量需要调试才能得到，不同的电脑偏移量不一样。
# 偏移量问题和无法选中问题的解决办法后续有讲解
# 安装pyautogui模块（pip3 install pyautogui）

from selenium import webdriver
from time import sleep
import pyautogui
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def test1():
    print('test1')


def test2():
    driver = webdriver.Chrome()
    driver.get("http://www.jpress.io/user/register")
    driver.maximize_window()
    sleep(1)
    elem = driver.find_element(By.ID, "agree")  # 当前理想结果是系统自动勾选了网站条例，实际上是勾选不上的，下面是解决办法

    # 方法一：（实现失败，因为设备的分辨率问题，导致获取坐标不准确，最终没有勾选上）
    # rect = elem.rect
    # pyautogui.click(rect['x'] + 10, rect['y'] + 130)
    # sleep(5)

    # 方法二：（实现成功）
    actions = ActionChains(driver)
    actions.move_to_element(elem).click().perform()
    sleep(5)

