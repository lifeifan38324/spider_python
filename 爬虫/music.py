import random
import math
import requests

class WangYiYun():
    def __init__(self, d):
        self.d = d
        self.e = "010001"
        self.f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
        self.g = "0CoJUm6Qyw8W8jud"
        self.random_str = self.get_random_str()

    def get_random_str(self):
        str1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        res = ''
        for x in range(16):
            index = math.floor(random.random() * len(str1))
            res += str1[index]
        print(res)
        return res


def main():
    songs = input('请输入您要的歌手信息：')
    d = '{"logs":"[{\\"action\\":\\"searchkeywordclient\\",\\"json\\":{\\"type\\":\\"song\\",\\"keyword\\":\\"%s\\",\\"offset\\":0,\\"device_id\\":\\"null\\"}}]","csrf_token":""}' % songs
    wyy = WangYiYun(d)
    wyy.get_random_str()

    url = 'https://music.163.com/weapi/cloudsearch/get/web?csrf_token='
    # post
    headers = {
        'cookie': 'P_INFO=kindle_lifeifan@126.com|1665498987|1|mail126|00&99|bej&1664981918&mailmaster_ios#gud&440100#10#0#0|&0||kindle_lifeifan@126.com; _iuqxldmzr_=32; _ntes_nnid=a194f6d909c85f143995b60bdf796527,1666082326565; _ntes_nuid=a194f6d909c85f143995b60bdf796527; NMTID=00OwFmZHdlLzZcQo0Z7rAuiGVFUU00AAAGD6j7BwA; WEVNSM=1.0.0; WNMCID=uneasy.1666082326823.01.0; WM_TID=7pIcFz8tRddEAQURERLUT%2BU7bpK5EWZv; WM_NI=Ro%2Baqyn743YFZGGk5rDYpbQUQi07kdMMJFyxl1YDxbJUKF1LZcu3If2n9a2xcsQTt6kiYn%2FFiNIkH5E%2BTyyFWWuHLRR3usVYgGjsnnQlQEusGM16lw2CukM4XN1%2FBh2NeFE%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeabbb4a92a78d95ea43b38a8aa7d14e879b8badc854edb297a4aa3abc88f795c92af0fea7c3b92a92b1e582f473aee9fcd4dc4e9a99898cb87a8887c083d45f93b700d8ea708f9386a7fc74b0ef97a5fb6a8a8b85a7b4489abdbbd4cc6ef2b2f782b174a1ad9fb5f73ea9b7978fae4eab92878ccb3f87f59c9afc4e9589bba9cf5a92edbb94d553a599a694ed6693b49fa6f8798593ffd7ef7df29dbb8cd0409c92ffd0c164f292aba7c837e2a3; JSESSIONID-WYYY=4npusnNNzPCriKk0mq2eqkHNlGsTx%2FOxRjZ0UvCz060NVX5hTlYiaJjxJFQg3Hpy98Y0C0hNv5i6nrWc4vWMOu3lbKBnWXRTAktTWKqi6z%5Cv%5C9zNEXiUY96KfiVjdDo3gqAqTRlBWW0yrfGIUdXfTDM%5C7vy%2B3jiZh%5C%2BOz8Q8HqvgCh9y%3A1666089348108',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }

    data = {
        'params': 12,
        'encSecKey': 123
    }


    pass

if __name__ == "__main__":
    main()