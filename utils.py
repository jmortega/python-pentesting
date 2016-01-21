#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from urlparse import urlparse
import urllib2
import dns.resolver

import sys
import socket
import requests

try:
    from bs4 import BeautifulSoup
except Exception as e:
    print("pip install beautifulsoup4")
    exit(1)
    
def verify_url(url):
    #check if url starts with http or https
    if url[:7].lower() != "http://" or url[:8].lower() != "https://":
        url = "http://" + url
    #verify url
    temp = urlparse(url)
    if temp.hostname is None:
        url = None
    return url

class _MyRedirects(urllib2.HTTPRedirectHandler):

    def http_error_301(self, req, fpc, code, msg, headers):
        print code, " http_error_301 ", headers['Location']
        return urllib2.HTTPRedirectHandler.http_error_301(self, req, fpc, code, msg, headers)

    def http_error_302(self, req, fpc, code, msg, headers):
        print code, " http_error_302 ", headers['Location']
        return urllib2.HTTPRedirectHandler.http_error_302(self, req, fpc, code, msg, headers)

    def http_error_303(self, req, fpc, code, msg, headers):
        print code, " http_error_303 ", headers['Location']
        return urllib2.HTTPRedirectHandler.http_error_303(self, req, fpc, code, msg, headers)

    def http_error_307(self, req, fpc, code, msg, headers):
        print code, " http_error_304 ", headers['Location']
        return urllib2.HTTPRedirectHandler.http_error_307(self, req, fpc, code, msg, headers)

# Extracts the html code
class HtmlExtractor(object):

    def __init__(self, url):
        self.follow_redirects = False
        self.html_body = None
        self.url = verify_url(url)
        if self.url is None:
            raise ValueError("URL No valida")

    def get_url(self):
        return self.url


    def get_body(self, follow_redirects = False):
        self.follow_redirects = follow_redirects
        request = urllib2.Request(self.url)
        opener = urllib2.build_opener(_MyRedirects())
        content = opener.open(request)
        self.html_body = content.read()
        return self.html_body

class DataExtractor(object):

    def __init__(self, html_body, url = None, only_href = False):
        self.html_body = html_body
        self.url = url
        self.only_href = only_href
        self.urls = []
        self.domains = []
        self.domain_ips = {}


    def get_urls(self):
        result = BeautifulSoup(self.html_body,"lxml")
        lst_tag = result.findAll("a")
        for c_url in lst_tag:
	    if 'href' in c_url:
		self.urls.append(c_url["href"])
        return self.urls


    def get_domains(self, urls = None):
        if urls is None:
            self.urls = self.get_urls()
        for url in urls:
            temp = urlparse(url)
            if temp.hostname is None:
                continue
            self.domains.append(temp.hostname)
        return dict.fromkeys(self.domains).keys()


    def get_ips_for_domains(self, domains = None):
        if domains is None:
            self.domains = self.get_domains()
        for domain in domains:
            answer = dns.resolver.query(domain, 'A')
            temp = []
            for rdata in answer:
                temp.append(rdata.address)
            self.domain_ips[domain] = temp
        return self.domain_ips
    
    def get_predictable_urls(self, url,logins):
	
	print "[+] Get predictable urls"
	print logins
	for login in logins:
	    try:
		print "Testing.." + (url+login)
		response = requests.get(url + login)
		if response.status_code == 200:
		    print "[+] Found Login Resource: " +login
	    except Exception,e:
		print str(e)
    
    def get_http_methods(self, url, httpMethods):

	print "[+] Get HTTP methods"
	print httpMethods
	
	for method in httpMethods:
	    try:
		print "Testing.." + method + " method"
		response = requests.get(url , method)
		if response.status_code not in range(400,599):
		    print "[+] Method Allowed: " +method + " " +str(response.status_code)
	    except Exception,e:
		print str(e)	      

    
class Checker():

    def __init__(self, hosts):
        self.hosts = hosts
        self.realhosts = []

    def check(self):
        for x in self.hosts:
            try:
                res = socket.gethostbyname(x)
                self.realhosts.append(res + ":" + x)
            except Exception as e:
                pass
        return self.realhosts