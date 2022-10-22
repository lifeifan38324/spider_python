import requests
import execjs

cookies = {
    'P_INFO': 'kindle_lifeifan@126.com|1665498987|1|mail126|00&99|bej&1664981918&mailmaster_ios#gud&440100#10#0#0|&0||kindle_lifeifan@126.com',
    '_iuqxldmzr_': '32',
    '_ntes_nnid': 'a194f6d909c85f143995b60bdf796527,1666082326565',
    '_ntes_nuid': 'a194f6d909c85f143995b60bdf796527',
    'NMTID': '00OwFmZHdlLzZcQo0Z7rAuiGVFUU00AAAGD6j7BwA',
    'WEVNSM': '1.0.0',
    'WNMCID': 'uneasy.1666082326823.01.0',
    'WM_TID': '7pIcFz8tRddEAQURERLUT%2BU7bpK5EWZv',
    'WM_NI': 'vDMPebHK4JvsQjmOlhvmzxdQnHy4i2AMI3q9p3iPPxEDPRikEu6sLtrSauDZelf6Qh4wIgTYz8k4%2F0xGTjJCMY7gctGGtx5SaxPJWuGvYwg%2FUMsvCHeNXczR5h3owAq7VVk%3D',
    'WM_NIKE': '9ca17ae2e6ffcda170e2e6eeabeb52b1abbfa6f77d838a8fa7c84a938a8f83d15db2b3fb88fb349088ffabf52af0fea7c3b92ab69c83b1e86a8c95fcabf57993b6a3b0ef64b6b3b699e75bae98b7d5ec3a839387d4f433b4eda7b1d374879ca0b3ec6187abfa94cf80b28daf96c752a7b4aad7d464f8a98788d753bae8a5d5ae3cbc999c8bc9498f87f988e2808599bc99b859a3a8a0abd67f85aa9798e6259793bd97c244a7929884f95af7b8fd90f64bb3e99ab7ea37e2a3',
    'JSESSIONID-WYYY': '%5CuK8hpevZJ%2BJ%2FtAex%2BjvmWBj8C7ERifuvEoNCbyPQuJ%2BBd%2B8OZaxY9%5Cy53KNd5VMFSxvhO4vlalGp0gK%5CSgaJD%5C%2BSGk7D76YarypNwZA7ZU4SwRTdt3ptsvjVWfmIgZ2iexAzov1HUujVcWm5nkij%5CMG10YQqwG0yhi%5CNsZR%5CmWO1INO%3A1666187744150',
    'playerid': '66553013',
}

headers = {
    'authority': 'music.163.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'P_INFO=kindle_lifeifan@126.com|1665498987|1|mail126|00&99|bej&1664981918&mailmaster_ios#gud&440100#10#0#0|&0||kindle_lifeifan@126.com; _iuqxldmzr_=32; _ntes_nnid=a194f6d909c85f143995b60bdf796527,1666082326565; _ntes_nuid=a194f6d909c85f143995b60bdf796527; NMTID=00OwFmZHdlLzZcQo0Z7rAuiGVFUU00AAAGD6j7BwA; WEVNSM=1.0.0; WNMCID=uneasy.1666082326823.01.0; WM_TID=7pIcFz8tRddEAQURERLUT%2BU7bpK5EWZv; WM_NI=vDMPebHK4JvsQjmOlhvmzxdQnHy4i2AMI3q9p3iPPxEDPRikEu6sLtrSauDZelf6Qh4wIgTYz8k4%2F0xGTjJCMY7gctGGtx5SaxPJWuGvYwg%2FUMsvCHeNXczR5h3owAq7VVk%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeabeb52b1abbfa6f77d838a8fa7c84a938a8f83d15db2b3fb88fb349088ffabf52af0fea7c3b92ab69c83b1e86a8c95fcabf57993b6a3b0ef64b6b3b699e75bae98b7d5ec3a839387d4f433b4eda7b1d374879ca0b3ec6187abfa94cf80b28daf96c752a7b4aad7d464f8a98788d753bae8a5d5ae3cbc999c8bc9498f87f988e2808599bc99b859a3a8a0abd67f85aa9798e6259793bd97c244a7929884f95af7b8fd90f64bb3e99ab7ea37e2a3; JSESSIONID-WYYY=%5CuK8hpevZJ%2BJ%2FtAex%2BjvmWBj8C7ERifuvEoNCbyPQuJ%2BBd%2B8OZaxY9%5Cy53KNd5VMFSxvhO4vlalGp0gK%5CSgaJD%5C%2BSGk7D76YarypNwZA7ZU4SwRTdt3ptsvjVWfmIgZ2iexAzov1HUujVcWm5nkij%5CMG10YQqwG0yhi%5CNsZR%5CmWO1INO%3A1666187744150; playerid=66553013',
    'origin': 'https://music.163.com',
    'referer': 'https://music.163.com/',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
}

params = {
    'csrf_token': '',
}

d1 = "{\"ids\":\"[1990179959]\",\"level\":\"standard\",\"encodeType\":\"aac\",\"csrf_token\":\"\"}"

with open('./music.js', 'r', encoding='utf-8') as f:
    js_obj = f.read()
res = execjs.compile(js_obj).call('main123', d1)

data = {
    'params': 'U6luW+dcHonXuixDpKJGKINFeXJnK8uRUIy49fvmQXw5BEsht1u0OfCjSo9HIc8DJtdo3ZEV5HX5lqsn8Rsa1PdCr3PhWMPmLxSk+iidknHto59KCChQVac6mDIj+d+3pIgYJNFMas1Q+HdAfzLmvw==',
    'encSecKey': '5e17f94e0bcb2d24a899903cbc97cdd94cca76fb7204424d9c15fbb7799725bb4bc4a462c93374e23d21665e841ef3b13deab76ebe80646d5ae22d9a38e24f1d30fda2ff23f9e478814e33782891a3e638eafd4f50590e17545aa6dd65e2dac7d67f6aaafec6af92a121062b8cb56f1d19330e22d3003d68bdd627b2f0799157',
}

response = requests.post('https://music.163.com/weapi/song/enhance/player/url/v1', params=params, cookies=cookies, headers=res, data=data)
print(response.text)

