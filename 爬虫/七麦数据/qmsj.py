import requests
import json

cookies = {
    'Hm_lvt_ff3eefaf44c797b33945945d0de0e370': '1666495679',
    'qm_check': 'A1sdRUIQChtxen8tJ0NMOTQ+GRdzfX0QZlkFBwwKUC03HBd1QlhAXFECEUMgEQsfVkMBdAgBFE4SPVY7SFkKRmgHbwkcFHxSJlJVUVtWF1RaVVpbFgJDUk9UVElWBRsCEkQ%3D',
    'PHPSESSID': 'ka6bbvn0brc3hf6t7inl73l3tt',
    'gr_user_id': '2900bee0-31aa-4a36-856f-98737625aabb',
    'ada35577182650f1_gr_session_id': 'e275d8a7-76a3-45d0-9e2e-d616fca7e515',
    'ada35577182650f1_gr_session_id_e275d8a7-76a3-45d0-9e2e-d616fca7e515': 'true',
    'tgw_l7_route': '1ed618a657fde25bb053596f222bc44a',
    'synct': '1666496023.375',
    'syncd': '-761',
    'Hm_lpvt_ff3eefaf44c797b33945945d0de0e370': '1666496024',
}

headers = {
    # 'authority': 'api.qimai.cn',
    # 'accept': 'application/json, text/plain, */*',
    # 'accept-language': 'zh-CN,zh;q=0.9',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'Hm_lvt_ff3eefaf44c797b33945945d0de0e370=1666495679; qm_check=A1sdRUIQChtxen8tJ0NMOTQ+GRdzfX0QZlkFBwwKUC03HBd1QlhAXFECEUMgEQsfVkMBdAgBFE4SPVY7SFkKRmgHbwkcFHxSJlJVUVtWF1RaVVpbFgJDUk9UVElWBRsCEkQ%3D; PHPSESSID=ka6bbvn0brc3hf6t7inl73l3tt; gr_user_id=2900bee0-31aa-4a36-856f-98737625aabb; ada35577182650f1_gr_session_id=e275d8a7-76a3-45d0-9e2e-d616fca7e515; ada35577182650f1_gr_session_id_e275d8a7-76a3-45d0-9e2e-d616fca7e515=true; tgw_l7_route=1ed618a657fde25bb053596f222bc44a; synct=1666496023.375; syncd=-761; Hm_lpvt_ff3eefaf44c797b33945945d0de0e370=1666496024',
    # 'origin': 'https://www.qimai.cn',
    # 'referer': 'https://www.qimai.cn/',
    # 'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': '"Windows"',
    # 'sec-fetch-dest': 'empty',
    # 'sec-fetch-mode': 'cors',
    # 'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
}

params = {
    'analysis': 'dkJNEQUWElVcX1MGHDFVQxJNARYZFx5qWFNMVSEaA1NVUl1MS08FAHdAVw==',
}

response = requests.get('https://api.qimai.cn/rank/indexPlus/brand_id/1', params=params, cookies=cookies, headers=headers)
data = json.loads(response.text)["list"]
for ele in data:
    print(ele)