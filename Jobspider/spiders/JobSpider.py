from scrapy.spider import Spider
from scrapy.selector import Selector

from Jobspider.items import JobspiderItem
import urllib

class JobSpider(Spider):
    name = "Monster"
    allowed_domains = ["jobsearch.monster.com"]
    start_urls = []
    categories = ["C__2B__2B","C__23","java","python","ruby","web","iOS","PHP"]
    job_types = ["full-time","part-time","intern"]
    basic_url =  "http://jobsearch.monster.com/search/?q="
    for cate in categories:
        for job_type in job_types:
            url = basic_url + cate +'-' + job_type
            start_urls.append(url)

    
    def parse(self, response):
        # """
        # The lines below is a spider contract. For more info see:
        # http://doc.scrapy.org/en/latest/topics/contracts.html

        # @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        # @scrapes name
        # """
        category_dic = {'C__2B__2B':'C++','C__23':'C#','java':'Java','python':'Python',
                          'ruby':'Ruby','web':'Web','iOS':'iOS','PHP':'PHP'}
        sel = Selector(response)
        jobwrapper = sel.xpath('//div[@class="jobTitleCol fnt4"]')
        loc_wrapper = sel.xpath('//div[@class="companyCol fnt20 locationInfo"]')
        
        # jobtitles = jobwrapper.xpath('.//div[@class="jobTitleContainer"]/a/text()')
        # locations = sel.xpath('//div[@class="jobLocationSingleLine"]/a/@title')
        # companies = jobwrapper.xpath('.//div[@class="companyContainer"]/div/a[1]/@title')
        # urls = sel.xpath('//div[@class="jobTitleContainer"]/a/@href')
        items = []

        
        if len(loc_wrapper) == len(jobwrapper):
            for i in range(len(loc_wrapper)):
                item = JobspiderItem()
                keyword_list = response.url.split('/')[-1][3:].split('-')
                item['category'] = category_dic[keyword_list[0]]
                item['job_type'] = keyword_list[1]
                if len(keyword_list) == 3:
                    item['job_type'] += ' ' + keyword_list[2]
                item['name'] = jobwrapper[i].xpath('.//div[@class="jobTitleContainer"]/a/text()').extract()[0]
                item['url'] = jobwrapper[i].xpath('.//div[@class="jobTitleContainer"]/a/@href').extract()[0]
                item['company'] = jobwrapper[i].xpath('.//div[@class="companyContainer"]/div/a[1]/@title').extract()[0]
                item['source'] = 'Monster'
                location = loc_wrapper[i].xpath('.//div[@class="jobLocationSingleLine"]/a/@title').extract()
                # print item['name'],item['url'],item['company'],item['job_type'],location
                if len(location)>0:
                    location_list = location[0].split(',')
                    item['city'] = location_list[0]
                    if len(location_list)>1:
                        item['state'] = location_list[1]
                items.append(item)
        else:
            print"locations:",len(loc_wrapper),"jobwrapper",len(jobwrapper)

        return items


