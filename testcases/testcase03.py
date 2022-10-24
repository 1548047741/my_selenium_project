# 29、通过第三方AI库识别验证码（当前代码可以运行，但是因为接口是收费的，所以结果没有达到验证码结果）
# 接口url:https://www.showapi.com/console#/myTestCase?list(账号：chengbin   931012)
# 需要引入r；equests包 ：运行终端->进入python/Scripts ->输入：pip install requests
# 免费的API：https://dun.163.com/dashboard#/m/captcha/index/?pid=YD00927905000303

from lib.ShowapiRequest import ShowapiRequest

r = ShowapiRequest("http://route.showapi.com/184-4", "272526", "a924d4e982ae404b8a068b4d1c7784f2")
r.addFilePara("image", "test.png")
r.addBodyPara("typeId", "34")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")
res = r.post()
result = res.text
print(result)
body = res.json()['showapi_res_body']
print(body)
print(body['Result'])
# print(res.text['showapi_res_body']['result'])  # 返回信息
