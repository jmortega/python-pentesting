#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import requests

class CheckCookies:

    def test(self,url):
        
        if url.startswith("http://") == True:
            target = url
        else:   
            target = "http://" + url
            
        req = requests.get(target)
        
	print req.cookies
	cookies = dict(admin='True')
	
	cookie_req = requests.get(target, cookies=cookies)
	
	for cookie in req.cookies:
		print 'Name:', cookie.name
		print 'Value:', cookie.value
		print 'Secure:', cookie.secure
		print 'Loosly defined domain:', cookie.domain_initial_dot
		print 'HTTPOnly:', self.check_httponly(cookie), '\n'	

    def check_httponly(self,c):
	if 'httponly' in c._rest.keys():
	    return 'True'
	else:
	    return 'False'    
