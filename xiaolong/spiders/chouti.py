# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy import Request
from xiaolong.items import XiaolongItem


class ChoutiSpider(scrapy.Spider):
    name = 'chouti'
    allowed_domains = ['chouti.com']
    start_urls = ['http://dig.chouti.com/']

    def parse(self, response):
        hxs = HtmlXPathSelector(response = response)
        items  = hxs.xpath("//div[@id='content-list']/div[@class='item']")
        for item in items:
            # print(item)
            href = item.xpath('.//div[@class="part1"]/a[1]/@href').extract_first()
            text = item.xpath('.//div[@class="part1"]/a[1]/text()').extract_first()
            item = XiaolongItem(title = text, href = href)
            yield item

        pages = hxs.xpath('.//div[@id="page-area"]//a[@class="ct_pagea"]/@href').extract()
        for page_url in pages:
            page_url = "http://dig.chouti.com" + page_url
            yield Request(url = page_url, callback = self.parse)

            123
            

