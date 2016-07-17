#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import urllib2, argparse, sys
    
class IdentifyServer:

    def test(self,host):
        
        print("[*] Testing %s") % (str(host))
        
        if host.startswith("http://") == True:
            target = host
            target_secure = host.replace("http","https")
        else:   
            target = "http://" + host
            target_secure = "https://" + host
        
        try:
            request = urllib2.Request(target)
            request.get_method = lambda : 'HEAD'
            response = urllib2.urlopen(request)
        except:
            print("[-] No web server at %s") % (str(target))
            response = None
        
        if response != None:
            print("[*] Response from %s") % (str(target))
            print(response.info())

        try:
            request_secure = urllib2.urlopen(target_secure)
            request_secure.get_method = lambda : 'HEAD'
            response_secure = urllib2.urlopen(request_secure)
        except:
            print("[-] No web server at %s") % (str(target_secure))
            response_secure = None
            
        if response_secure != None:
            print("[*] Response from %s") % (str(target_secure))
            print(response_secure.info())
    
