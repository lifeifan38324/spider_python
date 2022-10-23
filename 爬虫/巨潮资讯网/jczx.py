import time
import base64
import math
import json


#     var time = Math.floor(new Date().getTime() / 1000);
time1 = math.floor(time.time())  # 1666494219
mcode = base64.b64encode(str(time1).encode()).decode()
print(mcode)


import requests

cookies = {
    'routeId': '.uc1',
    'Hm_lvt_489bd07e99fbfc5f12cbb4145adb0a9b': '1666493175',
    'Hm_lpvt_489bd07e99fbfc5f12cbb4145adb0a9b': '1666493315',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'routeId=.uc1; Hm_lvt_489bd07e99fbfc5f12cbb4145adb0a9b=1666493175; Hm_lpvt_489bd07e99fbfc5f12cbb4145adb0a9b=1666493315',
    'Origin': 'http://webapi.cninfo.com.cn',
    'Proxy-Connection': 'keep-alive',
    'Referer': 'http://webapi.cninfo.com.cn/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'mcode': mcode,
}

data = {
    'tdate': '2022-10-21',
    'market': 'SZE',
}

response = requests.post('http://webapi.cninfo.com.cn/api/sysapi/p_sysapi1007', cookies=cookies, headers=headers, data=data, verify=False)
json_data = json.loads(response.text)
for element in json_data['records']:
    print(element['证券简称'])
