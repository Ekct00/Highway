# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DrivefasterPipeline(object):
    def process_item(self, item, spider):
        return item


class WriteMag(object):
    def __init__(self):
        self.file = open('magnents.txt', 'w+')

    def process_item(self, item, spider):
        line = "\n".join(item["link"])
        self.file.write(line)
        return item