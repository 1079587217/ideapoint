import json

import requests
import execjs

from cookies import get_cookies

# cookies = {
#     'cookie2': '15537b6c6bb2dfed9bb9cd558696c7ab',
#     'cna': '1+W+INmRhxcCAXWTGzhryqvL',
#     'xlly_s': '1',
#     'mtop_partitioned_detect': '1',
#     '_m_h5_tk': '2bc0f1cb6ce655fb16595a03072342ba_1748516484560',
#     '_m_h5_tk_enc': 'a79d92b14ef6e4bef2c877472ac801f0',
#     'tfstk': 'gfmIZej4R6fQayqRFyvNf6Oi_7Z7Vd-VVTw-nYIFekEdw_HY_XPUYLx7wXVZYWkUv90igxIEYeqPVkqu2IR20nJnKuq-AajS2w2Tn--PwyLaX5FXTiR20nkpJJqrBIoP25OQ18E8pzURWdw3U_E8J8F9C8eP9aIKwd9_FJedw7Ud6AeUnuF-wyp_X8PTpuUKwAhPgtwWRWDBLwY8zyYNEvV12gn_BQVjdUjuBceBiSDQ1QOEfm4QMvF12BHFbGP7smdw5AcjJXyiNnO_DqcsVrEWAs2IWxZTToLf5kMZtmZKcBsUQlVUk4U6pHH_AWa0CrKytkg-t0anRTvmBkhioS4pSC2sYmz7iP199Ak_9rgSTCj8TqMt1roN_irxofi7koIzxiPjUE_5Crj7CSJ6CabuUSf-L0GiwaaLIJawCd1KryegC-J6CaXuJR2wCd91uI5..',
# }





class Spider():
    def __init__(self):
        self.cookies = get_cookies()
        self.headers = {
            'accept': 'application/json',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.goofish.com',
            'priority': 'u=1, i',
            'referer': 'https://www.goofish.com/',
            'sec-ch-ua': '"Chromium";v="136", "Microsoft Edge";v="136", "Not.A/Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0',
            # 'cookie': 'cookie2=15537b6c6bb2dfed9bb9cd558696c7ab; mtop_partitioned_detect=1; _m_h5_tk=dec2584f5f18c14af1df3717d7cb1bf4_1748508110997; _m_h5_tk_enc=032c1a6d1178ec4b359a4719a85bd7b2; cna=1+W+INmRhxcCAXWTGzhryqvL; xlly_s=1; tfstk=gHlja0fUhijfF8PO5-YPNOgIPZNsGURF1Nat-VCVWSFAXG3L4mr4gFA_Xmqrgou4MZDoY2CqgKVN1SVg6H-eTB8mo5Vt8Lht5if88rOaksUYi7UTY2CeTBumkZzv84dE_gKv5urT6-eTeTEu5lCO6ce-yyrRMPCYWgL7quCYklUOwzU3JZBtX5LSyu4T6rnTHUg-a4_Q5KZmlEWqu01MiwMLV1CtNzKgAqOO9rcblNZIlutp0bG3hk3YV1Kxu_5zfucp4LgoAxn4rcOBVWHnVfwL1Is3lY3QwoPpdTNjzmcQMXtfgzPu0JHTFEdxPSZbKzwp_nVjBmc_nx_M-4Fxqvq3HLxuPjlUCk252n3rPoeICm-l6okIy0wEag5U9vmS1JFd4K5UAVJCCawh1zZePU6GIPrhXqlsqcB_Hz4bUUT5DA2YrziWPU6GP-UuzUTWP9oR.',
        }
    def run(self,number):
        if self.cookies['_m_h5_tk'] == '':
            self.cookies =get_cookies()
        data = {
            'data': json.dumps({
                "itemId": "",
                "pageSize": 30,
                "pageNumber": number,
                "machId": "165362_1"
            }, separators=(',', ':'))}

        with open('xianyu.js', encoding='utf-8') as f:
            js_code = f.read()
        params =execjs.compile(js_code).call('get_params',data,self.cookies['_m_h5_tk'])
        # print(params)
        response = requests.post(
            'https://h5api.m.goofish.com/h5/mtop.taobao.idlehome.home.webpc.feed/1.0/',
            params=params,
            cookies=self.cookies,
            headers=self.headers,
            data=data,
        )
        with open(f'xianyu_{number}.json', 'w', encoding='utf-8') as f:
            json.dump(response.json(), f,  ensure_ascii=False, indent=4)
s =Spider()
index=0
for i in range(1,11):
    s.run(i)
    index=i
print(index)