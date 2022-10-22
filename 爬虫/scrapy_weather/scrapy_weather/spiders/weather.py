import scrapy
import json
import jsonpath


class WeatherSpider(scrapy.Spider):
    name = 'weather'
    allowed_domains = ['www.weather.com.cn']
    start_urls = ['http://d1.weather.com.cn/calendar_new/2022/101010100_202210.html?_=1666074786768']

    def parse(self, response):
        print("="*40)
        content = response.text[len('var fc40 = '):]
        data_json = json.loads(content)
        date_list = jsonpath.jsonpath(data_json, '$..date')
        print(date_list)
        pass
