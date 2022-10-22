import scrapy


class MusicSpider(scrapy.Spider):
    name = 'music'
    allowed_domains = ['music.163.com']
    start_urls = ['https://music.163.com/discover/toplist']

    def parse(self, response):
        print("+"*30)
        text_list = response.xpath('//div[@id="song-list-pre-cache"]//li/a')
        for text in text_list:
            print(text.xpath('./text()').extract_first())
            print(text.xpath('./@href').extract_first())
        print("-"*30)
        pass
