JobSpider

This is a Scrapy project to fetch online employment data from public websites.
This project is only for studying purposes.

Items:
The items scraped by this project are employment information. The item is defined in the class:
Jobspider.items.JobspiderItem

Spiders:
This project contains one spider called JobSpider that you can see by running:
scrapy list

Spider: JobSpider
The "JobSpider" spider fetch the related information from "Monster.com".

You can run the spider with "Scrapy crawl JobSpider" to fetch the data defined in the file. 

Pipelines
This project uses a pipeline to store the data into database named "Job_info_daya.sqlite".
This pipeline is defined in the class:
Jobspider.pipelines.SqliteStorePipeline