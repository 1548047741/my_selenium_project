# 30、实现工具类：设计获得验证码、随机字符串生成、cookie操作工具类
# 注意：工具类一搬会放在util文件包中，并在文件包中新建一个.py文件,详见get_code和gen_random_str方法

import pickle
import random
import string
import time
from lib.ShowapiRequest import ShowapiRequest
from PIL import Image
import os


def get_logger():
    # import logging
    import logging.handlers
    import datetime

    logger = logging.getLogger('mylogger')
    logger.setLevel(logging.DEBUG)

    rf_handler = logging.handlers.TimedRotatingFileHandler('all.log', when='midnight', interval=1, backupCount=7,
                                                           atTime=datetime.time(0, 0, 0, 0))
    rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

    f_handler = logging.FileHandler('error.log')
    f_handler.setLevel(logging.ERROR)
    f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

    logger.addHandler(rf_handler)
    logger.addHandler(f_handler)
    return logger


def get_code(driver, ele_id):
    # 获取并保存验证码图片
    t = time.time()
    path = os.path.dirname(os.path.dirname(__file__)) + '\\screenshots'
    picture_name1 = path + '\\' + str(t) + '.png'

    driver.save_screenshot(picture_name1)  # 实现截屏

    ce = driver.find_element_by_id(ele_id)  # 根据ID拿到验证码元素的位置

    left = ce.location['x']
    top = ce.location['y']
    right = ce.size['width'] + left
    height = ce.size['height'] + top

    dpr = driver.execute_script('return window.devicePixelRatio')
    print(dpr)
    im = Image.open(picture_name1)
    img = im.crop((left * dpr, top * dpr, right * dpr, height * dpr))

    t = time.time()
    picture_name2 = path + '\\' + str(t) + '.png'
    img.save(picture_name2)  # 这里就是截取到的验证码图片

    # 解析验证码图片
    r = ShowapiRequest("http://route.showapi.com/184-4", "290728", "1bd001f23c874581aac4db788a92c71d")
    r.addFilePara("image", picture_name2)
    r.addBodyPara("typeId", "34")
    r.addBodyPara("convert_to_jpg", "0")
    r.addBodyPara("needMorePrecise", "0")
    res = r.post()
    text = res.json()['showapi_res_body']
    print(text['Result'])
    return text['Result']


# 生成随机字符串
def gen_random_str():
    rand_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    return rand_str


def save_cookie(driver, path):
    with open(path, 'wb') as filehandler:
        cookies = driver.get_cookies()
        print(cookies)
        pickle.dump(cookies, filehandler)


def load_cookie(driver, path):
    with open(path, 'rb') as cookiesfile:
        cookies = pickle.load(cookiesfile)
        for cookie in cookies:
            driver.add_cookie(cookie)
