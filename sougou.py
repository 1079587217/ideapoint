import json
import os

import requests
from lxml.etree import HTML


class Spider():
    pre_url="https://fabiaoqing.com/biaoqing/lists/page/"
    header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
            'Referer':'https://fabiaoqing.com/'}
    index= 1
    def __init__(self,page):
        self.page=page
    def run(self):
        url=self.pre_url+'{}.html'.format(self.index)
        res=requests.get(url,headers=self.header)
        html=HTML(res.text)
        max_index=int(html.xpath('//*[@id="bqb"]/div[3]/a[7]')[0].text.strip())
        if self.page < max_index:
            max_index=self.page
        img_names = []
        for i in range(1,max_index+1):
            url=self.pre_url+'{}.html'.format(i)
            res=requests.get(url,headers=self.header)
            html=HTML(res.text)
            src_list=html.xpath("//div[@class='tagbqppdiv']/a/img")
            for src in src_list:
                img_url=src.get('data-original')
                img_name=img_url[img_url.rfind('/')+1:]
                img_data=requests.get(img_url,headers=self.header).content
                if not os.path.exists('C:\ProgramData\SogouInput\Components\Picface\Collections\{}'.format(img_name)):
                    with open('C:\ProgramData\SogouInput\Components\Picface\Collections\{}'.format(img_name),'wb') as f:
                        f.write(img_data)
                img_names.append({"picKeyWord":"\u037c\u01ac\u046d\u01e9","picName":img_name,"picType":2})
        with open("C:\ProgramData\SogouInput\Components\Picface\Json\SGUserCollection.json", "w") as f:
            json.dump(img_names,f)
        pass


if __name__ == '__main__':
    Spider(3).run()