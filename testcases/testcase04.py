# 这个是我自己在网上找的免费接口，可以识别网上的某个验证码图片，也可以识别本地的验证码图片
# 参考地址：https://www.jianshu.com/p/97efb8d988b5
import json
import requests

TOKEN = 'free'  # token 获取：http://www.bhshare.cn/imgcode/gettoken
URL = 'http://www.bhshare.cn/imgcode/'  # 接口地址


def imgcode_online(imgurl):
    """
    在线图片识别
    :param imgurl: 在线图片网址 / 图片base64编码（包含头部信息）
    :return: 识别结果
    """
    data = {
        'token': TOKEN,
        'type': 'online',
        'uri': imgurl
    }
    response = requests.post(URL, data=data)
    print(response.text)
    result = json.loads(response.text)
    if result['code'] == 200:
        print(result['data'])
        return result['data']
    else:
        print(result['msg'])
        return 'error'


def imgcode_local(imgpath):
    """
    本地图片识别
    :param imgpath: 本地图片路径
    :return: 识别结果
    """
    data = {
        'token': TOKEN,
        'type': 'local'
    }

    # binary上传文件
    files = {'file': open(imgpath, 'rb')}

    response = requests.post(URL, files=files, data=data)
    print(response.text)
    result = json.loads(response.text)
    if result['code'] == 200:
        print(result['data'])
        return result['data']
    else:
        print(result['msg'])
        return 'error'


if __name__ == '__main__':
    imgcode_online('https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fzhuangjiba.com%2Fd%2Ffile%2Fhelp%2F2018'
                   '%2F08%2Fcfdefaddb3f47d78f8c66a7de28720aa.png&refer=http%3A%2F%2Fzhuangjiba.com&app=2002&size'
                   '=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1656491660&t=bc51f690ccfa54396285e5c752ef3ff5')

    imgcode_local('/Users/smzdm/selenium_project/testcases/test.png')
