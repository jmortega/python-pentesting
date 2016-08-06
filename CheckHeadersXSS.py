#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import requests
from ghost import Ghost
#pip install Ghost.py
import logging
import os
    
class CheckHeadersXSS:

    def test(self,url):
        
        if url.startswith("http://") == True:
            target = url
        else:   
            target = "http://" + url
            
        req = requests.get(target)
        
	print 'Checking X-XSS-Protection...'
	
	try:
		xssprotect = req.headers['X-XSS-Protection']
		if 1 not in 'xssprotect':
			print 'X-XSS-Protection not set properly, XSS may be possible'
	except:
		print 'X-XSS-Protection not set, XSS may be possible'
		
	print '----------------------------------'
	print 'Checking X-Content-Type-Options...'
	
	try:
		contenttype = req.headers['X-Content-Type-Options']
		if contenttype != 'nosniff':
			print 'X-Content-Type-Options not set properly:',contenttype
	except:
		print 'X-Content-Type-Options not set'
	
	print '----------------------------------'
	print 'Checking Strict-Transport-Security...'
	
	try:
		hsts = req.headers['Strict-Transport-Security']
	except:
		print 'HSTS header not set, MITM should be possible via HTTP'
	
	print '----------------------------------'
	print 'Checking x-frame-options...'
	
	try:
		xframe = req.headers['x-frame-options']
		print 'X-FRAME-OPTIONS:', xframe , 'present, clickjacking not likely possible'
	except:
		print 'X-FRAME-OPTIONS missing'
	
	print '----------------------------------'
	print 'Checking Content-Security-Policy...'
	
	try:
		csp = req.headers['Content-Security-Policy']
		print 'Content-Security-Policy set:', csp
	except:
		print 'Content-Security-Policy missing'
	
	print '----------------------------------'
	print 'Checking clickjacking...'
	
	self.clickjack(target)
	
    def clickjack(self,url):
	html = '''<html>
		<body>
		<iframe src="'''+url+'''"></iframe>
		</body>
		</html>'''
	
	html_file = 'clickjack.html'
	log_file = 'test.log'
		 
	f = open(html_file, 'w+')
	f.write(html)
	f.close()
	
	logging.basicConfig(filename=log_file)
	logger = logging.getLogger('ghost')
	logger.propagate = False
		 
	ghost = Ghost(log_level=logging.INFO)
	with ghost.start() as session:
	    page, resources = session.open(html_file)
		
	ghost.exit()
		
	log = open(log_file, 'r')
	if 'forbidden by X-Frame-Options.' in log.read():
	    print 'Clickjacking mitigated'
	else:
	    print 'Clickjacking successful'
			
	log = open(log_file, 'r')
	if 'forbidden by X-Frame-Options.' in log.read():
	    print 'Clickjacking mitigated via X-FRAME-OPTIONS'
	else:
	    with ghost.start() as session:
		href = session.evaluate('document.location.href')[0]
		if html_file not in href:
		    print 'Frame busting detected'
		else:
		    print 'Frame busting not detected, page is likely vulnerable to clickjacking'
				
		
	log.close()    
        
        
    
