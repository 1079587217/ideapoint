import string
import random

from get import get
from trake import get_trake
import execjs

import requests
import ddddocr

def get_seild():
    ocr =ddddocr.DdddOcr(det=False,show_ad=False)
    with open('bg.jpg','rb') as f:
        bg=f.read()
    with open('fg.jpg','rb') as f:
        fg= f.read()
    target =ocr.slide_match(bg,fg,simple_target=True)
    return int((target.get('target')[0]+25)*(304/480))

def run():
    token =get()
    distance =get_seild()
    # print("识别距离是 ",distance)
    points=get_trake(distance)

    with open('yunpian.js', encoding='utf-8') as f:
        js_code = f.read()
    data = execjs.compile(js_code).call('get_data', points, distance)

    cookies = {
        '__wksid': 'n-7202B52EC84847FD8483BAA653D26ECC',
        '_gid': 'GA1.2.1616831453.1748697422',
        'MEIQIA_TRACK_ID': '2xoA25fDjKWxTDPwMaItVc4QkD7',
        'MEIQIA_VISIT_ID': '2xrViQzPP2bWamavAsCAQ5gs8Qv',
        '_ga_ESVMH6YSPX': 'GS2.1.s1748697421$o1$g1$t1748698308$j33$l0$h0',
        '_ga_B8H0JYR4RL': 'GS2.1.s1748697421$o1$g1$t1748698308$j33$l0$h0',
        '_ga': 'GA1.2.2091767417.1748697422',
    }
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'script',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0',
        'sec-ch-ua': '"Chromium";v="136", "Microsoft Edge";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        # 'Cookie': '__wksid=n-7202B52EC84847FD8483BAA653D26ECC; _gid=GA1.2.1616831453.1748697422; MEIQIA_TRACK_ID=2xoA25fDjKWxTDPwMaItVc4QkD7; MEIQIA_VISIT_ID=2xrViQzPP2bWamavAsCAQ5gs8Qv; _ga_ESVMH6YSPX=GS2.1.s1748697421$o1$g1$t1748698308$j33$l0$h0; _ga_B8H0JYR4RL=GS2.1.s1748697421$o1$g1$t1748698308$j33$l0$h0; _ga=GA1.2.2091767417.1748697422',
    }
    params = {
        'cb': ''.join(random.choices(string.ascii_lowercase, k=11)),
        'i': data['i'],
        'k': data['k'],
        'token': token,
        'captchaId': '974cd565f11545b6a5006d10dc324281',
    }
    response = requests.get('https://captcha.yunpian.com/v1/jsonp/captcha/verify', params=params, cookies=cookies,
                            headers=headers)
    print(response.text)

for i in range(10):
    run()