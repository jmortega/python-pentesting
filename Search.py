#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import string
import sys
import re
import time
import requests
import urllib
import mechanize

from ParserResults import ParserResults

class Search:

    def __init__(self, domain):
        self.domain = domain
        self.counter = 0
        self.results = ""
        self.totalresults = ""
        self.server = "www.google.com"
        self.userAgent = "(Mozilla/5.0 (Windows; U; Windows NT 6.0;en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6"
        self.quantity = "100"
  
    def do_search(self):
        try:
            url="http://" + self.server + "/search?num=" + self.quantity + "&start=" + str(self.counter) + "&hl=en&meta=&q=%40\"" + self.domain + "\""
        except Exception, e:
            print e
        try:
            r=requests.get(url)
            self.results = r.content 
            self.totalresults += self.results
        except Exception,e:
            print e
        

    def get_emails(self):
        rawres = ParserResults(self.totalresults, self.domain)
        return rawres.emails()

    def get_hostnames(self):
        rawres = ParserResults(self.totalresults, self.domain)
        return rawres.hostnames()

    def get_files(self):
        rawres = ParserResults(self.totalresults, self.domain)
        return rawres.fileurls(self.files)

    def process(self):
        while self.counter <= 100 and self.counter <= 1000:
            self.do_search()
            time.sleep(1)
            self.counter += 100
            
    def getLinks(self,ip,depth):
        br= mechanize.Browser()
        br.set_handle_robots(False)
        br.addheaders[('User-agent','chrome')]
        
        query="http://www.google.com/search?num=100&q="+ip+"&start="+depth
        htmltext=br.open(query).read()
        soup=BeautifulSoup(htmltext)
        search=soup.findAll('div',attrs={'id':'search'})
        searchtext=str(search[0])
        soup1=BeautifulSoup(searchtext)
        list_items=soup1.findAll('li')
        
        regex="q(?!.*q).*?&amp"
        pattern =re.compile(regex)
        
        results_array=[]
        
        for li in list_items:
            soup2 = BeautifulSoup(str(li))
            links=soup2.findAll('a')
            source_link=links[0]
            source_url=re.findall(pattern,str(source_link))
            if len(source_url)>0:
                results_array.append(str(source_url[0].replace("q=","").replace("&amp","")))
        
        return results_array
                     