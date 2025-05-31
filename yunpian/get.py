import json

import requests
def get():
    cookies = {
        '__wksid': 'n-7202B52EC84847FD8483BAA653D26ECC',
        '_gid': 'GA1.2.1616831453.1748697422',
        'MEIQIA_TRACK_ID': '2xoA25fDjKWxTDPwMaItVc4QkD7',
        'MEIQIA_VISIT_ID': '2xrViQzPP2bWamavAsCAQ5gs8Qv',
        '_gat_gtag_UA_199829768_1': '1',
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
        # 'Cookie': '__wksid=n-7202B52EC84847FD8483BAA653D26ECC; _gid=GA1.2.1616831453.1748697422; MEIQIA_TRACK_ID=2xoA25fDjKWxTDPwMaItVc4QkD7; MEIQIA_VISIT_ID=2xrViQzPP2bWamavAsCAQ5gs8Qv; _gat_gtag_UA_199829768_1=1; _ga_ESVMH6YSPX=GS2.1.s1748697421$o1$g1$t1748698308$j33$l0$h0; _ga_B8H0JYR4RL=GS2.1.s1748697421$o1$g1$t1748698308$j33$l0$h0; _ga=GA1.2.2091767417.1748697422',
    }

    params = {
        'cb': 'mdko45hkq94',
        'i': 'vqOUkzxbC19oHX8F2zzccuTjELTXkjhTIonQSMyn/pfi+/i0pybM76aEQEHbFulwLmlY6dzvKgZyftPDUZ6Z2NBgUPXdXap1OZiKJZlhN4zcW0U8udSF2nTe9/pjY9tUcL2Ah+wB3E2TALUcH/54PzgnKisgCt3Bdrmem67O+gn5rr6khEPqFH3Vzpbeg4j4uBDGigB6m/jbaw+gH77KaFBcn9VFPy4AnDaAKdXw2xflGBYCAuvOnAzGWdr+IUWyN3j4a3ezffFIYCknq2inngHdrItNRIoo+iPlAmU1iWpkz17HGHCVjXRL3ByTLa44lgCCPCLKhKppU1NKY3t3F/Ss2eSVQYS8aCjdq5UFGmq4HnM82N7phRaI83PjKeKZAehXu76MDNEmjJ7/PD+mgAbKopHU0Q72S5oM23AW9AKtpJAhaDGm8HzIirzx0aa5VEWDDZGpwH3Fas5+6PHi5VHmsJJBqLCIvJi/YWKL5qVIHG06NLXHV0rWdPYKSZsSt7gAWhdewBrsEttbN+3CcpUMFEyMLntWAYPteofcC7RR2vQI6P+ryHuG0cA8rsKJKtj3gyk2g/CT6fQwBqNFV1ZOymsbFLGa3ceL+t93/yoIkHC9JpKTWsVtyvczqDq06tD57nBTM4WJr948lHYQiVItv7HupxTheoouaPROjJe3TOoqKC9rDEbsZqr6yj7tdB1nUdulUljCdDfAL2CJDLQnCMvhaYLjEXqfcAORp5chVOb7S6xAGrONLth1/BS7eEWo8agwJOpHDgaEq0eu8jSSo14eNITZmkqI3916J8mdx/tCzk4JLtkS2v+uvs18hmM7rFF1ZwC7Xd9qidnBEIGqFTB0r1ZrtkX8WTQkHFTuwrJRvi0G7X6xujiHjgX7',
        'k': 'lF6SmXjNF1Vih/UqgTMIRnO7gyCwaIC+MbZsB3f6iYA1Ju/caijnUarpq3zWShWRhux3SARNuusWFse6qlM9HAW2Val8M5P8L6k08sbS/aPsmFt5c6gc6QJYI9uDKlTg2z9TxVBpamht32BlmuOlIcnWqfZ8aN+Di7qVIDfDIA0=',
        'captchaId': '974cd565f11545b6a5006d10dc324281',
    }

    response = requests.get('https://captcha.yunpian.com/v1/jsonp/captcha/get', params=params, cookies=cookies, headers=headers)
    data = response.text.split('(')[1].split(')')[0]
    json_data =json.loads(data)
    bg = json_data['data']['bg']
    front= json_data['data']['front']
    token = json_data['data']['token']
    with open('bg.jpg', 'wb') as f1,open('fg.jpg','wb') as f2:
         f1.write(requests.get(bg).content)
         f2.write(requests.get(front).content)
    return token
# get()