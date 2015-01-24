# -*- coding: utf-8 -*-

# Scrapy settings for Jobspider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'Jobspider'

SPIDER_MODULES = ['Jobspider.spiders']
NEWSPIDER_MODULE = 'Jobspider.spiders'


ITEM_PIPELINES = ['Jobspider.pipelines.SqliteStorePipeline']

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Jobspider (+http://www.yourdomain.com)'
