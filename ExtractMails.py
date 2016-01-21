#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import urllib
import urllib2
import re
import mechanize
import cookielib
import requests

try:
    from bs4 import BeautifulSoup
except Exception as e:
    print("pip install beautifulsoup4")
    exit(1)
    

class ExtractMails:
    
    def create_browser(self):
        br = mechanize.Browser()           # Create basic browser
        cj = cookielib.LWPCookieJar()      # Create cookiejar to handle cookies
        br.set_cookiejar(cj)               # Set cookie jar for our browser
        #Browser options
        br.set_handle_equiv(True)          # Allow opening of certain files
        br.set_handle_gzip(False)          # Allow handling of zip files(experimental option)
        br.set_handle_redirect(True)       # Automatically handle auto-redirects
        br.set_handle_referer(True)
        br.set_handle_robots(False)        # ignore anti-robots.txt
        
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
	
        # Necessary headers to simulate an actual browser
        br.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'),
                         ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
                         ('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'),
                         ('Accept-Encoding', 'gzip,deflate,sdch'),
                         ('Accept-Language', 'en-US,en;q=0.8,fr;q=0.6'),
                         ('Connection', 'keep-alive')
                         ]
        return br
	
    #obtain mails from a specific domain
    def obtain_mails(self,domain):
        
        br = self.create_browser()
        
        f = open("mails.txt","wb")
        
        print "Obtaining mail info from domain "+ domain
        
        if domain.startswith("http") == False:
            response = requests.get("http://"+domain)
        else:
            response = requests.get(domain)        

        contents = response.content
        soup = BeautifulSoup(contents,'lxml')
        links = soup.find('a',href=re.compile("mailto"))

        if links:
            print links['href'].replace("mailto:","")
            f.write(links['href'].replace("mailto:","")+'\n')
	
        f.close()