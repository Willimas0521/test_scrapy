from pymongo import MongoClient
from scrapy import settings

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface


class AnSpiderPipeline:
    # def process_item(self, item, spider):
    #     return item
    # def __init__(self):
    #     host = settings['MONGODB_HOST']
    #     port = settings['MONGODB_PORT']
    #     db_name = settings['MONGODB_DBNAME']
    #     collection_name = settings['MONGODB_COLLNAME']
    #     client = pymongo.MongoClient(host=host, port=port)
    #     db = client[db_name]
    #     self.post = db[collection_name]

    def process_item(self, item, spider):
        client = MongoClient('localhost', 27017)
        db = client.test
        collection = db.houseprice
        # 对所获取的数据字典化处理
        house_info = dict(item)
        collection.insert_one(house_info)
        return item


    # item['area']=item['area'].map(lambda d: d.replace('㎡', ""))
    # item['price'] = item['price'].map(lambda d: d.replace('元/㎡', ""))
    # item['area'] = float(item['area'])
    # item['price'] = float(item['price'])