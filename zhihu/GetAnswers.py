import requests
from json import loads
from urllib.parse import urlencode



class getZhihuAnswers(object):
    
    def __init__(self, questionID, page):
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }                #请求头
        conf = {   
            'include' : 'content',
            'limit' : 10,
            'offset' : page*10,
            'paltform' : 'desktop',
            'sort_by' : 'default'
        }                #url配置项
        self.url_main = 'https://www.zhihu.com/api/v4/questions/{}/answers?'.format(questionID)
        self.url = self.url_main + urlencode(conf)
        self.headers = headers
        
      
    def getPages(self):
        try:
            response = requests.get(self.url, headers = self.headers)
            print(self.url)
            page = loads(response.text)
            return page['data']
        except requests.exceptions.HTTPError:
            return None


        


        