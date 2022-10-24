# from testcases import testcase01
from testcases import testcase02
# from testcases import testcase03
# from testcases.basic.test_user_register import TestUserRegister
from selenium import webdriver
from util import util

if __name__ == '__main__':
    # testcase02.test1()
    # testcase02.test2()
    # testcase01.test2()

    print(util.gen_random_str())
    driver = webdriver.Chrome()
    driver.get('http://localhost:8080/jpress/user/register')
    driver.maximize_window()
    print(util.get_code(driver, 'captcha-img'))
