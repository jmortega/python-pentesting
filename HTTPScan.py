# -*- encoding: utf-8 -*-
#class for HttpScan connection

import socket
import urllib2
import httplib
import socket
import HTMLParser
import socket
import base64
import sys

class HTTPScan:
    
    def basic_auth(self, host, username, passwd, code=0):
        
        try:
            request = urllib2.Request(host)
            authTokenBase64 = base64.encodestring('%s:%s' % (username, passwd)).replace('\n', '')
            request.add_header("Authorization", "Basic %s" % authTokenBase64)
            request.add_header("Host", host)
            result = urllib2.urlopen(request)
            if result is not None:
                print 'Found %s:%s\n' %(username, passwd)
        except (urllib2.HTTPError,socket.gaierror, socket.error, IOError) as e:
            print e
            code = 2
        return code
    
    def basic_auth2(self, host, username, passwd, code=0):
            
            try:
                request = httplib.HTTP(host)
                authTokenBase64 = base64.encodestring('%s:%s' % (username, passwd)).replace('\n', '')
                request.putheader("Authorization", "Basic %s" % authTokenBase64)
                request.putheader("Host", host)
                request.endheaders()
                request.send("")
                statusCode,statusMsg,headers = request.reply()
                if statusCode is not None:
                    print 'Found %s:%s\n' %(username, passwd)
            except (urllib2.HTTPError,socket.gaierror, socket.error, IOError) as e:
                print e
                code = 2
            return code    
    
    def basic_auth_proxy(self, host, username, passwd, proxy_address, code=0):
        
            try:
                proxy = urllib2.ProxyHandler({'http': proxy_address})
                opener = urllib2.build_opener(proxy)
                urllib2.install_opener(opener)           
                request = urllib2.Request(host)
                
                authTokenBase64 = base64.encodestring('%s:%s' % (username, passwd))[:-1]
                request.add_header("Authorization", "Basic %s" % authTokenBase64)
                request.add_header("Host", host)
                result = urllib2.urlopen(request)
                if result is not None:
                    print 'Found %s:%s\n' %(username, passwd)
            except (urllib2.HTTPError,socket.gaierror, socket.error, IOError) as e:
                print e
                code = 2
            return code    
        
    def startHTTPScanBruteForce(self,host,ip,proxy):
        try:
            
            #check port 80 is open
            sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex((ip,80))
            
            if host.startswith("http") == False:
                            host = "http://"+host            

            if result == 0:
                
                    print "Port 80 open"            

                    print '\n[*] Started scanning \'%s\' \n' % (host)
            
                    #open files dictionary
                    users_file = open("users.txt")
                    passwords_file = open("passwords.txt")
                    for user in users_file.readlines():
                        for password in passwords_file.readlines():
                
                            user_text = user.strip("\n")
                            password_text = password.strip("\n")
                            try:
                                    #check connection with user and password
           
                                    if proxy is not None:
                                        response = self.basic_auth_proxy(host,user_text,password_text,proxy)
                                    else:
                                        response = self.basic_auth(host,user_text,password_text)
                                    if response == 0:
                                            print("[*] User: %s [*] Pass Found:%s" %(user_text,password_text))
                                    elif response == 1:
                                        print("[*] User: %s [*] Pass %s => Login incorrect !!!" %(user,password))
                                    elif response == 2:
                                        print("[*] Connection could not be established to %s" %(host))
                                        return 2
                            except Exception,e:
                                print e
                                print "Error http scan"
                                pass
                            
                    #close files
                    users_file.close()
                    passwords_file.close()
            
            else:
                print "Port HTTP 80 closed"        

        except Exception,e:
            print "users.txt /passwords.txt Not found"
            pass
