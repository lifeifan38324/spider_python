import requests

cookies = {
    '_m_h5_tk': 'ab95d16414cc54fdd5479d649b12885a_1666501394148',
    '_m_h5_tk_enc': 'e0906bdb49b72809aab2a2352a9e3b83',
    'xlly_s': '1',
    'cookie2': '1ba0d660bb059ac64a68ee211d2a9d2e',
    't': '3a74097fdb273a226856bdde0c155cfb',
    '_tb_token_': '3e55436be9f43',
    '__cn_logon__': 'false',
    'alicnweb': 'touch_tb_at%3D1666491327027',
    'isg': 'BKenhi3HiOpt9wxmyvbwdRvtNttxLHsOxIirjnkQFTZkaMUqgf0SXkopimh2h1OG',
    'l': 'eBSW_e9ITijDs_tiBO5ZPurza77taCRbz1PzaNbMiInca6TFGe6WYNCUeeFwPdtjgt5A2etzv3EoxdEy-5aLRAkDBeYCWQ0gUdJ6-e1..',
    'tfstk': 'cDVPBNVqu_CyELUdXjcU_NMM1TbRaBeLIUgIEM45H4AFeTMobsbMvqm-dbGeuHDl.',
}

headers = {
    'authority': 'h5api.m.1688.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    # Requests sorts cookies= alphabetically
    # 'cookie': '_m_h5_tk=ab95d16414cc54fdd5479d649b12885a_1666501394148; _m_h5_tk_enc=e0906bdb49b72809aab2a2352a9e3b83; xlly_s=1; cookie2=1ba0d660bb059ac64a68ee211d2a9d2e; t=3a74097fdb273a226856bdde0c155cfb; _tb_token_=3e55436be9f43; __cn_logon__=false; alicnweb=touch_tb_at%3D1666491327027; isg=BKenhi3HiOpt9wxmyvbwdRvtNttxLHsOxIirjnkQFTZkaMUqgf0SXkopimh2h1OG; l=eBSW_e9ITijDs_tiBO5ZPurza77taCRbz1PzaNbMiInca6TFGe6WYNCUeeFwPdtjgt5A2etzv3EoxdEy-5aLRAkDBeYCWQ0gUdJ6-e1..; tfstk=cDVPBNVqu_CyELUdXjcU_NMM1TbRaBeLIUgIEM45H4AFeTMobsbMvqm-dbGeuHDl.',
    'referer': 'https://sale.1688.com/',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
}

params = {
    'jsv': '2.6.1',
    'appKey': '12574478',
    't': '1666492616150',
    'sign': '7aa2f64a113710730cee9be98c8d37ae',
    'v': '1.0',
    'type': 'jsonp',
    'isSec': '0',
    'timeout': '20000',
    'api': 'mtop.taobao.widgetService.getJsonComponent',
    'dataType': 'jsonp',
    'jsonpIncPrefix': 'mboxfc',
    'callback': 'mtopjsonpmboxfc9',
    'data': '{"cid":"TpFacRecommendService:TpFacRecommendService","methodName":"execute","params":"{\\"pageNo\\":\\"1\\",\\"cna\\":\\"\\",\\"pageSize\\":\\"20\\",\\"from\\":\\"PC\\",\\"sort\\":\\"mix\\",\\"trafficSource\\":\\"pc_index_recommend\\",\\"url\\":\\"https://sale.1688.com/factory/home.html?spm=a260k.dacugeneral.searchbox.2.663335e4OshDx8\\"}"}',
}

response = requests.get('https://h5api.m.1688.com/h5/mtop.taobao.widgetservice.getjsoncomponent/1.0/', params=params, cookies=cookies, headers=headers)


print(response.text)
