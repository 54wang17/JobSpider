# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from   twisted.enterprise import adbapi
from os import path
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
import sqlite3


class JobspiderPipeline(object):
    def process_item(self, item, spider):
        return item


class SqliteStorePipeline(object):
    filename = 'Job_info_data.sqlite'
    
    def __init__(self):
        self.conn = None
        dispatcher.connect(self.initialize, signals.engine_started)
        dispatcher.connect(self.finalize, signals.engine_stopped)
 
    def process_item(self, item, domain):
        try:
            self.conn.execute('insert into job_info values(NULL,?,?,?,?,?,?,?,?)', 
                          (item['source'], item['name'], item['category'], item['job_type'],
                         item['company'], item['city'], item['state'], item['url']))
        except:
            print 'Failed to insert item: ' + item['url']
        return item
 
    def initialize(self):
        if path.exists(self.filename):
            self.conn = sqlite3.connect(self.filename)
        else:
            self.conn = self.create_table(self.filename)
 
    def finalize(self):
        if self.conn is not None:
            self.conn.commit()
            self.conn.close()
            self.conn = None
 
    def create_table(self, filename):
        conn = sqlite3.connect(filename)
        sql = "CREATE TABLE IF NOT EXISTS job_info(id INTEGER PRIMARY KEY,web_source TEXT, name TEXT, category TEXT, job_type TEXT, company TEXT, city TEXT, state TEXT, url TEXT)"
        conn.execute(sql)
        conn.commit()
        return conn