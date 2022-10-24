# 31、完成用户注册测试用例：解决验证码、等待弹窗等复杂内容（由于测试系统的版本和视频中的版本不一样，注册时没有弹窗，而是红色文字标识提示，所以代码无法运行）
from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# from lib.HTMLTestRunner import HTMLTestRunner
from util import util


class TestUserRegister(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8080/jpress/user/register')
        self.driver.maximize_window()

    # 测试登录验证码错误
    def test1_register_code_error(self):
        username = 'test001'
        email = 'test001@qq.com'
        pwd = '123456'
        confirmPwd = '123456'
        captcha = '666'
        expected = '验证码不正确'

        self.driver.find_element_by_name('username').send_keys(username)
        self.driver.find_element_by_name('email').send_keys(email)
        self.driver.find_element_by_name('pwd').send_keys(pwd)
        self.driver.find_element_by_name('confirmPwd').send_keys(confirmPwd)
        self.driver.find_element_by_name('captcha').send_keys(captcha)
        self.driver.find_element_by_class_name('btn').click()

        WebDriverWait(self.driver, 5).until(EC.alert_is_present())          # 浏览器等待5秒，直到期望的弹窗出现为止
        alert = self.driver.switch_to.alert             # 将焦点切换到弹窗

        assert alert.text == expected       # python的断言来判断实际结果和理想结果是否一致
        # self.assertEqual(alert.text, expected)
        alert.accept()
        sleep(5)

    # 测试成功
    def test2_register_ok(self):
        username = util.gen_random_str()  # 用工具类随机生成一个用户名
        email = username + '@qq.com'
        pwd = '123456'
        confirmPwd = '123456'
        # 自动获取
        captcha = ''
        expected = '注册成功，点击确定进行登录。'

        # 输入用户名
        username_elem = self.driver.find_element_by_name('username')
        username_elem.clear()
        username_elem.send_keys(username)

        # email
        email_elem = self.driver.find_element_by_name('email')
        email_elem.clear()
        email_elem.send_keys(email)
        # 密码
        self.driver.find_element_by_name('pwd').clear()
        self.driver.find_element_by_name('pwd').send_keys(pwd)
        # 确认密码
        self.driver.find_element_by_name('confirmPwd').clear()
        self.driver.find_element_by_name('confirmPwd').send_keys(confirmPwd)
        # 自动识别验证码
        captcha = util.get_code(self.driver, 'captcha-img')
        # 输入验证码
        self.driver.find_element_by_name('captcha').clear()
        self.driver.find_element_by_name('captcha').send_keys(captcha)
        # 点击注册
        self.driver.find_element_by_class_name('btn').click()

        # 等待alert出现
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert

        # 验证
        assert alert.text == expected
        # self.assertEqual(alert.text, expected)
        alert.accept()

    # def runTest(self):
    #     self.test1_register_code_error()
    #     self.test2_register_ok()
