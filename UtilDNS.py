# -*- encoding: utf-8 -*-

import dns.resolver
import dns.reversename
import pythonwhois
from ipaddress import IPv4Address
from socket import getfqdn

try:
    from ipwhois import IPWhois
except Exception as e:
    print("pip install ipwhois")
    exit(1)
    
    
#class dns resolver
class UtilDNS:

    def __init__(self):
        self.myresolver = dns.resolver.Resolver()
        self.myresolver.domain = dns.name.Name("google-public-dns-a.google.com")
        self.myresolver.nameserver = ['8.8.8.8']
        
    def checkDNSInfo(self,ip,hostname):
        print "-------------------------------------------"
        print "Obtain domain and DNS"
        print "-------------------------------------------"

        try:
            whois = pythonwhois.get_whois(ip)
            for key in whois.keys():
                if key =='raw':
                    info = whois[key][0].split("\n")
                    for i in info:
                        print i
                else:    
                    print "[+] %s : %s \n" %(key, whois[key])
        except Exception,e:
                print e

        try:
	    
            self.hostData(hostname)
	    self.obtainMoreData(ip)
	    self.dnsWhois(hostname)
	    self.dnsWhois(ip)
	    
        except Exception,e:
                print str(e)
    
    def dnsWhois(self,hostName):
	print "\nWhois info:"
        print "---------------------------------"
	print whois.whois(hostName)
		
    def hostData(self,hostName):
        print "\nInformation about DNS servers"
        print "---------------------------------"
        try:
            answers = self.myresolver.query(hostName, 'CNAME')
            for rdata in answers:
                print "CNAME:", str(rdata.target)
        except dns.resolver.NoAnswer:
            print "Can not obtain CNAME"
            
        try:
            answers = self.myresolver.query(hostName, 'A')
            ip = []
            for rdata in answers:
                n = dns.reversename.from_address(rdata.address)
                try:
                    answers_inv = self.myresolver.query(n, 'PTR')
                    for rdata_inv in answers_inv:
                        ip += [(rdata.address, str(rdata_inv.target))]
                except dns.resolver.NoAnswer:
                        ip += [(rdata.address, "PTR: No response "+str(n))]
                except dns.resolver.NXDOMAIN:
                        ip += [(rdata.address, "PTR: Domain NX "+str(n))]
                print "IPs:", ip
        except dns.resolver.NoAnswer:
            print "Can not obtain IPs"

        try:
            answers = self.myresolver.query(hostName, 'MX')
            mx = []
            for rdata in answers:
                mx += [str(rdata.exchange)]
            print "MXs:", mx
        except dns.resolver.NoAnswer:
            print "Can not obtain MXs"

        try:
            answers = self.myresolver.query(hostName,'NS')
            ns = []
            for rdata in answers:
                ns += [str(rdata.target)]
            print "NSs:", ns
        except dns.resolver.NoAnswer:
            print "Can not obtain NSs"

        try:
            answers = self.myresolver.query(hostName, 'SOA')
            for rdata in answers:
                print "SOA:", str(rdata.mname), str(rdata.rname)
        except dns.resolver.NoAnswer:
            print "Can not obtain SOA"

        try:
            answers = self.myresolver.query(hostName, 'TXT')
            for rdata in answers:
                print "TXT:", rdata.strings
        except dns.resolver.NoAnswer:
            print "Can not obtain TXT"

        try:
            answers = self.myresolver.query(hostName, 'LOC')
            for rdata in answers:
                print "LOC:", "Latitud",rdata.float_latitude,"Logitud", rdata.float_longitude
        except dns.resolver.NoAnswer:
            print "Can not obtain LOC"

        try:
            answers = self.myresolver.query(hostName, 'MINFO')
            for rdata in answers:
                print "MINFO:", rdata.to_text()
        except dns.resolver.NoAnswer:
            print "Can not obtain MINFO"

        try:
            answers = self.myresolver.query(hostName, 'HINFO')
            for rdata in answers:
                print "HINFO:", rdata.to_text()
        except dns.resolver.NoAnswer:
            print "Can not obtain HINFO"
            
    def obtainMoreData(self,host):
	print "\nInformation about domain name"
	print "---------------------------------"	
	#Obtain domain name and more information with Whois
	domainName = getfqdn(host)
	print 'Domain name:'+ domainName
	
	whois      = IPWhois(host).lookup()
	print whois
	
	aux        = domainName.split('.')
	dnsQuery   = '{0}.{1}'.format(aux[-2],aux[-1])
	
	addr = reversename.from_address(host)
	dns = "Reverser name"
	dns += str(addr) + "\n"  
	
	try:
	    ptrText = "\nPTR\n"
	    for ptr in resolver.query( addr, "PTR" ):
		ptrText += str(ptr)+"\n"
		dns += ptrText
	
	except Exception as e:
	    pass
	
	try:
	    nsText = "\nName servers"
	    for server in resolver.query(dnsQuery, 'NS'):
		nsText += str(server).rstrip('.')+'\n'
		dns += nsText
		
	    print dns
		
	except Exception as e:
	    pass        
        