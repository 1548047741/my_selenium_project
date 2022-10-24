# 28、解决验证码问题方案一（该部分的识别验证码的方法用于识别简单的验证码，复杂的就解决不了了）
# 解决思路：
#   1、截图整个页面
#   2、获取验证码坐标数据
#   3、根据坐标数据抠图
#   4、使用python中的pytesseract 模块进行验证
# 安装pytesseract模块（pip3 install pytesseract、brew install tesseract）和pil模块(pip3 install pillow)

import time
from selenium import webdriver
from PIL import Image
import pytesseract
from selenium.webdriver.common.by import By


def test1():        # 识别线上验证码图片
    browser = webdriver.Chrome()        # 打开谷歌浏览器
    browser.get("http://localhost:8080/jpress/user/register")       # 打开首页
    browser.maximize_window()

    # 获取验证码图片
    t = time.time()  # 获得当前时间
    picture_name1 = str(t) + '.png'  # 将获取的当前的时间变成字符串拼接成存储图片的名称
    browser.save_screenshot(picture_name1)  # 截屏
    # 获取验证码截图方法一（可行）
    # browser.find_element(By.ID,'captcha-img').screenshot('01.png')

    # 获取验证码截图方法二（图片为空白）
    ce = browser.find_element(By.ID, "captcha-img")  # 获得当前验证码所在的位置
    # print(ce.location)
    left = ce.location['x']
    top = ce.location['y']
    right = ce.size['width'] + left
    height = ce.size['height'] + top

    # im = Image.open(picture_name1)
    # img = im.crop((left, top, right, height))               # 抠图(这种抠图方式不行，抠出来的验证码是空白的,出现这样的问题是因为mac的屏幕问题，下面新增了个dpr解决了)

    dpr = browser.execute_script('return window.devicePixelRatio')
    print(dpr)
    im = Image.open(picture_name1)
    img = im.crop((left * dpr, top * dpr, right * dpr, height * dpr))

    t = time.time()
    picture_name2 = str(t) + '.png'  # 姜验证码保存为第二张图片
    img.save(picture_name2)  # 这里就是截取到的验证码图片
    browser.close()


def test2():            # 识别本地验证码图片
    image1 = Image.open('test.jpeg')
    image_to_str = pytesseract.image_to_string(image1)
    print(image_to_str)
