# -*- encoding: utf-8 -*-
#class for search in shodan
import shodan
import requests

class ShodanSearch:

    def __init__(self):
        #shodan key
        self.shodanKeyString = 'v4YpsPUJ3wjDxEqywwu6aF5OZKWj8kik'
        self.shodanApi = shodan.Shodan(self.shodanKeyString)
	
        
    def shodanKeyInfo(self):
        try:
            info = self.shodanApi.info()
            for inf in info:
                print '%s: %s ' %(inf, info[inf])
        except Exception, e:
            print 'Error: %s' % e
            

    def execute(self,ip):
            try:
                host = self.shodanApi.host(ip)
                self.obtain_host_info(ip)
                return host['data']
            except:
                print "SHODAN empty reply or error in the call"
                return "error"

    #Obtain info IP
    def obtain_host_info2(self,target):

	dnsResolve = 'https://api.shodan.io/dns/resolve?hostnames=' + str(target) + '&key=' + self.shodanKeyString
	
	try:
	    # First we need to resolve our targets domain to an IP
	    resolved = requests.get(dnsResolve)
	    hostIP = resolved.json()[target]
	   
	
	    # Then we need to do a Shodan search on that IP
	    host = self.shodanApi.host(hostIP)
	    print "IP: %s" % host['ip_str']
	    print "Organization: %s" % host.get('org', 'n/a')
	    print "Operating System: %s" % host.get('os', 'n/a')
	
	
	    # Print all banners
	    for item in host['data']:
		print "Port: %s" % item['port']
		print "Banner: %s" % item['data']
		
	
	    # Print vuln information
	    for item in host['vulns']:
		CVE = item.replace('!','')
		print 'Vulns: %s' % item
		exploits = api.exploits.search(CVE)
		for item in exploits['matches']:
		    if item.get('cve')[0] == CVE:
			print item.get('description')
	except Exception as e:
	    print e
	    print 'An error occured'	
	   
    #Obtain info IP
    def obtain_host_info(self,ip):
        try:
                print "Obtaining Shodan info from ["+ ip + "]"
                
                host = self.shodanApi.host(ip)
                if len(host) != 0:
                            # Print host info
                            print 'IP: %s' % host.get('ip_str')
                            print 'Country: %s' % host.get('country_name','Unknown')
                            print 'City: %s' % host.get('city','Unknown')
                            print 'Latitude: %s' % host.get('latitude')
                            print 'Longitude: %s' % host.get('longitude')
                            print 'Hostnames: %s' % host.get('hostnames')
                            print 'O.S: %s' % host.get('os','Unknown')
                            print 'Port: %s' % host.get('port')
                            print 'Updated: %s' % host.get('updated')
                          
                            for i in host['data']:
                                print 'Port: %s' % i['port']
			    
                                if 'organizations' in host.keys():
                                    for key,value in host['organizations'].items():
					    print(host['organizations'].get(key))	
                                if 'countries' in host.keys():
                                    for key,value in host['countries'].items():
                                            print(host['countries'].get(key))
                                if 'cities' in host.keys():
                                    for key,value in host['cities'].items():
					    print(host['cities'].get(key))
                            
			    for key, value in host.items():
				if key=="data":
				    for i, val in enumerate(value):
					for key, value2 in val.items():
					    print(val.get(key))				    

                            return host
			
        except shodan.APIError, e:
                print ' Error obtaning info from Shodan Service: %s' % e