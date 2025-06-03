import random
import re
import time
import requests
import execjs
import ddddocr
from track import track
def get_seild():
    ocr =ddddocr.DdddOcr(det=False,show_ad=False)
    with open('bg.jpg','rb') as f:
        bg=f.read()
    with open('fg.jpg','rb') as f:
        fg= f.read()
    target =ocr.slide_match(bg,fg,simple_target=True)
    return int((target.get('target')[0] + 15)*(200/600))

def get_rid():
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Referer': 'https://www.duitang.com/',
        'Sec-Fetch-Dest': 'script',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Storage-Access': 'active',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0',
        'sec-ch-ua': '"Chromium";v="136", "Microsoft Edge";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'sdkver': '1.1.3',
        'organization': 'ltA7kUoBFCTVmRodXoKD',
        'appId': 'default',
        'data': '{}',
        'lang': 'zh-cn',
        'model': 'slide',
        'callback': 'sm_'+str(int(time.time() * 1000)),
        'rversion': '1.0.3',
        'channel': 'DEFAULT',
    }

    response = requests.get('https://captcha1.fengkongcloud.cn/ca/v1/register', params=params, headers=headers)
    rid =re.findall( r'"rid":"(.*?)"', response.text)[0]
    pre_str="https://castatic.fengkongcloud.cn"
    bg = pre_str + re.findall(r'"bg":"(.*?)"', response.text)[0]
    fg = pre_str + re.findall(r'"fg":"(.*?)"', response.text)[0]
    with open('bg.jpg', 'wb') as f1,open('fg.jpg','wb') as f2:
         f1.write(requests.get(bg).content)
         f2.write(requests.get(fg).content)
    return rid
def verify():
    rid =get_rid()
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Referer': 'https://www.duitang.com/',
        'Sec-Fetch-Dest': 'script',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Storage-Access': 'active',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0',
        'sec-ch-ua': '"Chromium";v="136", "Microsoft Edge";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    x =get_seild()
    distance = x / 210
    array = track(max_x=x -5)
    times = random.randint(1750, 2000)
    with open('verify.js', encoding='utf-8') as f:
        js_code = f.read()
    data_params = execjs.compile(js_code).call('get_params', distance, array, times)
    params = {
        'sdkver': '1.1.3',
        'fc': 'dvINnLT4kns=',
        'ly': data_params[2],
        'jp': 'Wq4jwGqOHYM=',
        'callback': 'sm_'+str(int(time.time() * 1000)),
        'organization': 'ltA7kUoBFCTVmRodXoKD',
        'tm': data_params[1],
        'gp': '7kP9OL4ZRNU=',
        'ostype': 'web',
        'tb': data_params[0],
        'og': 'IxbGpVfruz0=',
        'rid': rid,
        'act.os': 'web_pc',
        'aj': 'Z8JptdSbQHg=',
        'sy': 'lN908/15DcI=',
        'protocol': '184',
        'wz': 'ufdT5h7SVes=',
        'rversion': '1.0.3',
        'dj': '7SnISxDhfjI=',
        'uc': 'zXfZHGRuNSs=',
    }

    response = requests.get('https://captcha1.fengkongcloud.cn/ca/v2/fverify', params=params, headers=headers)
    risk_level = re.search(r'"riskLevel"\s*:\s*"([^"]+)"', response.text).group(1);
    if risk_level != "PASS":
        return verify()
    print(risk_level)
    return rid
def login():
    rid =verify()
    cookies = {
        'js': '1',
        'HWWAFSESID': '43900f402363982fcc',
        'HWWAFSESTIME': '1748763100120',
        'Hm_lvt_d8276dcc8bdfef6bb9d5bc9e3bcfcaf4': '1748763101',
        'HMACCOUNT': 'D6C3E80FB50D5BDA',
        '_gid': 'GA1.2.1115104323.1748763102',
        '_ga_G8PGQ4LHXZ': 'GS2.1.s1748763133$o1$g0$t1748763133$j60$l0$h0',
        'Qs_lvt_476474': '1748763134',
        'Qs_pv_476474': '4371575573356091000',
        'smidV2': '202506011553357e767e3881517f0edc5c86a2859ee3bf000d2f4425f402ab0',
        'auth_token': 'e4de8428-6559-4502-a7ee-2655843aa7a5',
        '_gat_gtag_UA_19056403_7': '1',
        'JSESSIONID': 'node01kjt9iqtnxx5rmp5jxc2ct4y25594322.node0',
        'sessionid': '02a80c0d-79b4-40e4-bbb6-d5b01ca55e66',
        'Hm_lpvt_d8276dcc8bdfef6bb9d5bc9e3bcfcaf4': '1748764995',
        '_ga_EE20FJFZZQ': 'GS2.1.s1748763101$o1$g1$t1748764994$j49$l0$h0',
        '_ga': 'GA1.1.12229446.1748763102',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://www.duitang.com',
        'priority': 'u=1, i',
        'referer': 'https://www.duitang.com/login/',
        'sec-ch-ua': '"Chromium";v="136", "Microsoft Edge";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
        # 'cookie': 'js=1; HWWAFSESID=43900f402363982fcc; HWWAFSESTIME=1748763100120; js=1; Hm_lvt_d8276dcc8bdfef6bb9d5bc9e3bcfcaf4=1748763101; HMACCOUNT=D6C3E80FB50D5BDA; _gid=GA1.2.1115104323.1748763102; _ga_G8PGQ4LHXZ=GS2.1.s1748763133$o1$g0$t1748763133$j60$l0$h0; Qs_lvt_476474=1748763134; Qs_pv_476474=4371575573356091000; smidV2=202506011553357e767e3881517f0edc5c86a2859ee3bf000d2f4425f402ab0; auth_token=e4de8428-6559-4502-a7ee-2655843aa7a5; _gat_gtag_UA_19056403_7=1; JSESSIONID=node01kjt9iqtnxx5rmp5jxc2ct4y25594322.node0; sessionid=02a80c0d-79b4-40e4-bbb6-d5b01ca55e66; Hm_lpvt_d8276dcc8bdfef6bb9d5bc9e3bcfcaf4=1748764995; _ga_EE20FJFZZQ=GS2.1.s1748763101$o1$g1$t1748764994$j49$l0$h0; _ga=GA1.1.12229446.1748763102',
    }
    with open('duitang.js', encoding='utf-8') as f:
        js_code = f.read()
    pswd = execjs.compile(js_code).call('get_pswd', "wcz115566324")

    data = {
        'login_name': '18926456802',
        'pswd': pswd,
        'rid': rid,
        '':'',
        'remember': 'false',
    }

    response = requests.post('https://www.duitang.com/login/',cookies =cookies,  headers=headers, data=data)
    print(response.text)
login()
# for i in range(10):
#     verify()

# print(get_seild())