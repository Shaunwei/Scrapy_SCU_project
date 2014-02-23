from edu_project.linksgen.links_mis13 import url_links
from scrapy import log
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.spider import Spider


def nextURL():
    list_of_url = url_links[:]
    for next_url in list_of_url:
        yield next_url

class one_ponit_three_mis(Spider):
    name = "1point3_mis"
    allowed_domains = ["1point3acres.com"]
    download_delay = 10
    
    url = nextURL()
    start_urls = []
    
    def start_requests(self):
        start_url = self.url.next()
        log.msg("Current url at %s" %start_url)
        request = Request(start_url, dont_filter=True)
        yield request

#each thread at about 38 is the useful link start
    
    def parse(self, response):
        filename = "Raw_data_mis.txt"
        sel = Selector(response)
        #front-link = sel.xpath("//tr//a/@href").extract()
        raw_data = sel.xpath("//div[@id='JIATHIS_CODE_HTML4']").extract()
        with open(filename,'a') as f:
            f.write("\n=====NEXT=====\n")
            try:
               f.write(raw_data[0].encode('utf8'))
            except IndexError:
               print("-------------------------ERROR--------------------")
        #print raw_data[0].encode('utf8')
        
        next_url = self.url.next()
        yield Request(next_url)
