#!/usr/bin/env python
# -*- encoding: utf-8 -*-

#class for scraping

import os
import urlparse
import urllib,urllib2
import re

from PDFMetaData import PDFMetaData
from ImageMetaData import ImageMetaData

import requests
from lxml import html

try:
    from bs4 import BeautifulSoup
except Exception as e:
    print("pip install beautifulsoup4")
    exit(1)


class Scraping:
    
    def scrapingBeautifulSoup(self,hostname):
    
        try:
            print("BeautifulSoup..............")

            if hostname.startswith("http") == False:
                response = requests.get("http://"+hostname,stream=True)
            else:
                response = requests.get(hostname,stream=True)
            bs = BeautifulSoup(response.text, 'lxml')
            for tagImage in bs.find_all("img"): 
                if tagImage['src'].startswith("http") == False:
                    download = url + tagImage['src']
                else:
                    download = tagImage['src']
                print download
                # download images in images directory
                r = requests.get(download)
                f = open('images/%s' % download.split('/')[-1], 'wb')
                f.write(r.content)
                f.close()
        
        except Exception,e:
                print e
                print "Error to connect with " + hostname + " for scraping the site" 
                pass

        print("\nGet Metatada Image")
        print "------------------------------------"
        imageMetaData = ImageMetaData()
        imageMetaData.printMetaData()
    
    def scrapingImagesPdf(self,ip):
        print("\nScraping the server for images and pdfs.... "+ ip)
    
        try:
            url = 'http://'+ip
            print url
            response = requests.get(url)  
            parsed_body = html.fromstring(response.text)

            # Grab links to all images
            images = parsed_body.xpath('//img/@src')
    
            print 'Found %s images' % len(images)
    
            #create directory for save images
            os.system("mkdir images")
    
    
            for image in images:
                if image.startswith("http") == False:
                    download = url + image
                else:
                    download = image
                print download
                # download images in images directory
                r = requests.get(download,stream=True)
                f = open('images/%s' % download.split('/')[-1], 'wb')
                f.write(r.content)
                f.close()
    

            # Grab links to all pdf
            pdfs = parsed_body.xpath('//a[@href[contains(., ".pdf")]]/@href')
    
            #create directory for save pdfs
            if len(pdfs) >0:
                os.system("mkdir pdfs")
        
            print 'Found %s pdf' % len(pdfs)
            
            for pdf in pdfs:
                if pdf.startswith("http") == False:
                    download = url + pdf
                else:
                    download = pdf
                print download
                # download pdfs in pdf directory
                r = requests.get(download,stream=True)
                f = open('pdfs/%s' % download.split('/')[-1], 'wb')
                f.write(r.content)
                f.close()
    
        except Exception,e:
                print e
                print "Error to connect with " + ip + " for scraping the site" 
                pass
            
        print("\nGet Metatada Image")
        print "------------------------------------"
        imageMetaData = ImageMetaData()
        imageMetaData.printMetaData()
    
        print("\nGet Metatada PDF")
        print "------------------------------------"
        pdfMetaData = PDFMetaData()
        pdfMetaData.printMetaData()

    def getImgFromUrl(self, urlSource, extension):
        """
        name: getImgFromUrl
        brief: Get images from a url template.
        param urlSource: Url from where get the links of the images.
        param extension: Extension to add the regular expression.
        return: All the links that match with the regular expresion.
        """
        #check url starts with http
        if urlSource.startswith("http") == False:
                urlSource = "http://" + urlSource
                
        # GET HTML
        response = requests.get(urlSource,stream=True)
        html = response.text

        # REGULAR EXPRESION COMPILATION
        expresion = r'<img src="([^"]+).' + extension + '"'
        regexp = re.compile(expresion, re.I | re.MULTILINE | re.DOTALL)

        # FIND ALL CASES OF THE REG. EXPR.
        links = regexp.findall(html)

        # CREATING A LIST WITH ALL THE LINKS THAT MATCH WITH THE REG. EXPR.
        i=0
        while i<len(links):
            links[i]=links[i]+'.'+extension
            print urlSource + links[i], "\n"
            i += 1

        return links
