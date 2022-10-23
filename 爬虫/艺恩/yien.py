import requests
import subprocess
# 创建一个新的 Popen 类，并继承自 subprocess.Popen
class MySubprocessPopen(subprocess.Popen):
    def __init__(self, *args, **kwargs):
        # 在调用父类（即 subprocess.Popen）的构造方法时，将 encoding 参数直接置为 UTF-8 编码格式
        super().__init__(encoding='UTF-8', *args, **kwargs)


# 必须要在导入 PyExecJS 模块前，就将 subprocess.Popen 类重置为新的类
subprocess.Popen = MySubprocessPopen
import execjs


headers = {
    'Accept': 'text/plain, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://www.endata.com.cn',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'year': '2022',
    'MethodName': 'BoxOffice_GetYearInfoData',
}

response = requests.post('https://www.endata.com.cn/API/GetData.ashx', headers=headers, data=data)
with open('./yien.js', 'r', encoding='utf-8') as f:
    js_file = f.read()
data = execjs.compile(js_file).call('main123', response.text)
# print(data)
for item in data["Data"]['Table']:
    print(item)
