# -*- coding: utf-8 -*-
"""
__title__ = '龙部落电影网爬虫'
__author__ = 'zhangjun'
__mtime__ = '2017/3/25'

"""
import scrapy
from scrapy.selector import Selector
from lbldy.items import LbldyItem
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class LblspiderSpider(scrapy.Spider):
    name = "lblSpider"
    allowed_domains = ["lbldy.com"]
    start_urls = (
        'http://www.lbldy.com/movie/',
    )

    def parse(self, response):
        res = Selector(response)
        doms = res.xpath('//*[@id="center"]/div/div[@class="postlist"]')
        for dom in doms:
            # print dom.xpath('h4/a/@title').extract()[0],dom.xpath('h4/a/@href').extract()[0]
            # print dom.xpath('div[@class="postcontent"]/text()').extract()[0]
            # print '*'*100
            href = dom.xpath('h4/a/@href').extract()[0]
            # 将单个电影url传入scrapy，然后解析出电影下载地址
            yield scrapy.Request(url=href, callback=self.second_parse)

        # 取出下一页内容
        next_page = res.xpath('//a[@class="next page-numbers"]/@href').extract()[0]
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)

    # num = 1
    def second_parse(self,response):
        item = LbldyItem()
        res = Selector(response)

        # 电影名称
        dy_name = res.xpath('//div[@class="post"]/h2/text()').extract()[0]
        item['dy_name'] = dy_name.replace('高清迅雷下载','')
        # print item['dy_name']

        # 电影简介
        dy_summary = res.xpath('//div[@class="entry"]/p').extract()[0]
        item['dy_summary'] = dy_summary

        # 磁力链接 匹配4中格式 以（.torrent)开头的，以(magnet:)（ed2k）（thunder） 结尾的
        ma = res.xpath('//div[@class="entry"]/p/a').re("(http.+.torrent|magnet:?[^\"]+|ed2k:[^\"]+|thunder:[^\"]+)")

        # 方式一： 磁力链接有一个至多个，以逗号分隔，数据量较大
        link_string = ''
        # if len(ma)==0:
        #     # break
        #     print "未找到链接"
        # elif len(ma) == 1:
        #     link_string =  ma[0]
        # elif len(ma) > 1:
        #     for link in ma:
        #         link_string = link_string +","+ link
        #     # print link_string
        # item['dy_link'] = link_string #str.strip(link_string.decode('utf-8', 'ignore').encode('utf-8', 'ignore'))

        # 方式二：只取第一条链接存储
        if len(ma)>=1:
            item['dy_websit'] = response.url
            item['dy_link'] = ma[0]
            # 如果有下载链接则存入数据库
            yield item