import requests
import execjs
cookies = {
    'Hm_lvt_6146f11e5afab71309b3accbfc4a932e': '1748409650',
    'HMACCOUNT': 'F7C2D7B3361409B9',
    'JSESSIONID': 'C2263ACB56F75D87D1257FC6C5CDBF35',
    'Hm_lpvt_6146f11e5afab71309b3accbfc4a932e': '1748409880',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/octet-stream',
    'Origin': 'https://www.spolicy.com',
    'Referer': 'https://www.spolicy.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0',
    'sec-ch-ua': '"Chromium";v="136", "Microsoft Edge";v="136", "Not.A/Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': 'Hm_lvt_6146f11e5afab71309b3accbfc4a932e=1748409650; HMACCOUNT=F7C2D7B3361409B9; JSESSIONID=C2263ACB56F75D87D1257FC6C5CDBF35; Hm_lpvt_6146f11e5afab71309b3accbfc4a932e=1748409880',
}

# data = '\n\x014\x12\x00\x1a\x00"\x00*\x002\x008\x00@\x01H\aP\x01'
with open('dashuju.js', encoding='utf-8') as f:
    js_code = f.read()
result =execjs.compile(js_code).call('getData')
data = bytes(result['data'])
response = requests.post('https://www.spolicy.com/info_api/policyType/showPolicyType', cookies=cookies, headers=headers, data=data)
print(response.json())