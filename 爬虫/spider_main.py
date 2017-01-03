from 爬虫 import url_manager
from 爬虫 import html_downloader
from 爬虫 import html_outputer
from 爬虫 import html_parser





class SpiderMain(object):
    def __init__(self):
        self.maxcount=100#抓取数据数量
        self.urls=url_manager.UrlManager()
        self.downloader=html_downloader.HtmlDownloader()
        self.parser=html_parser.HtmlParser()
        self.outputer=html_outputer.HtmlOutputer()
    
    
    def craw(self,root_url):
        count=0
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url=self.urls.get_new_url()
    
                html_cont=self.downloader.download(new_url)
                new_urls,new_data=self.parser.parse(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                
                if count==self.maxcount:
                    break
        
            except Exception as e:
                print(e)
                continue
            else:
                count+=1
                print(new_url)
        self.outputer.output_html()   
        
    
    



if __name__=="__main__":
    root_url="http://baike.baidu.com/view/21087.htm"
    obj_spider=SpiderMain()
    obj_spider.craw(root_url)
    