#!/usr/bin/env python
# -*- encoding: utf-8 -*-

#class foR CHECK methods
import requests
import io
import socket

#Operating System Library
import os

#datetime
from datetime import datetime

#Image library
from PIL import Image

from socket import AF_INET, SOCK_STREAM, setdefaulttimeout

try:
    from selenium import webdriver
except Exception as e:
    print("pip install selenium")
    exit(1)
    
class Checker:
    
    def checkOptionMethods(self,hostname):
        try:
            r = requests.options('http://'+ hostname, timeout=5)
            print(r.headers['allow'])
        except KeyError:
            # Key is not present
            print "Not allow methods found!"
            pass
        except Exception,e:
                print "Error to connect with " + hostname + " for obtain option methods" 
                pass
    
    def checkOpenPorts(self,ip,hostname,portlist):
        # Check what time the scan started
        t1 = datetime.now()
        print "Cheking ports...."
        print portlist
        try:
            for port in portlist:
                sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                sock.settimeout(5)
                result = sock.connect_ex((ip,int(port)))
                if result == 0:
                    print "Port {}: \t Open".format(port)
                sock.close()
        except KeyError:
            # Key is not present
            print "Error checking ports!"
            pass
        except socket.gaierror:
            print 'Hostname could not be resolved. Exiting'
            sys.exit()
        except socket.error:
            print "Couldn't connect to server"
            sys.exit()
        
        # Checking the time again
        t2 = datetime.now()

        # Calculates the difference of time, to see how long it took to run the script
        total =  t2 - t1

        # Printing the information to screen
        print 'Scanning Completed in: ', total
	
	print 'Checking Port 80.....: '
	
	self.checkOpenPort80(ip,hostname)
	
    #check port 80 and obtain screenshot for the web page
    def checkOpenPort80(self,ip,host):
	
	setdefaulttimeout(5)
	
	template = "{0:16}{1:3}{2:40}"
	
	try:
	    #   AF_INET: Set(host, port)
	    #   SOCK_STREAM: connection TCP Protocol
	    connection = socket.socket(AF_INET, SOCK_STREAM)
	    # IP+port
	    connection.connect_ex((ip, 80))
	    # Obtain banner
	    connection.send(b'HEAD / HTTP/1.0\r\n\r\n')
	    banner = connection.recv(1024)
	    print(template.format(ip, '->', 'Open Port'))

	    aux = str(banner).replace('\\r\\n','<br/>')
	    banner = aux[2:len(aux)-3]
	    
	    # Close connection
	    connection.close()
		
	    #capturing screenshot of the web page
	    screenshot = self.takeScreenshot(host, str(80))
		
	    #save image screenshot
	    stream = io.BytesIO(screenshot)
	    img = Image.open(stream)
	    img.save("screenshot.png")
	
	except Exception as e:
	    print(template.format(host, '->', 'Closed Port: ('+str(e)+')'))
	    return False        

    def checkHeadersInfoByHostName(self,hostname):
        # Get the headers of a given hostname
        resp = requests.head('http://'+hostname)
        print resp.status_code, resp.text, resp.headers

        response = requests.get('http://'+hostname)
        for header, value in response.headers.items():
            print header+' : '+value

    def checkHeadersInfoByIp(self,ip):
        # Get the headers of a given IP
        resp = requests.head('http://'+ip)
        print resp.status_code, resp.text, resp.headers

        response = requests.get('http://'+ip)
        for header, value in response.headers.items():
            print header+' : '+value
            
    def checkNmapOptions(self,ip):
        print "Scanning Options"
        print "[1] Intense Scan"
        print "[2] Intense Scan + UDP"
        print "[3] Intense Scan - all TCP ports"
        print "[4] Intense Scan without ping"
        print "[5] Ping Scan"
        print "[6] Quickie Scan"
        print "[7] Quick Traceroute"
        print "[8] Normal Scan"
        print "[9] Send Bad Checksums"
        print "[10] Generate Randon Mac Adress Spoofing for Evasion"
        print "[11] Fragment Packets"
        
        option = raw_input("Choose your Scanning Option:")
        
        if option == '1':
                os.system("nmap -T4 -A -v "+ip)
                print "\n[**] Done \n"
        
        elif option == '2':
                os.system("nmap -sS -sU -T4 -A -v "+ip)
                print "\n[**] Done \n"

        
        elif option == '3':
                os.system("nmap -p 1-65535 -T4 -A -v "+ip)
                print "\n[**] Done \n"

        
        elif option == '4':

                os.system("nmap -T4 -A -v -Pn "+ip)
                print "\n[**] Done \n"

        
        elif option == '5':
                os.system("nmap -sn "+ip)
                print "\n[**] Done \n"

        
        elif option == '6':
                os.system("nmap -T4 -F "+ip)
                print "\n[**] Done \n"

        
        elif option == '7':
                os.system("nmap -sn --traceroute "+ip)
                print "\n[**] Done \n"

        
        elif option == '8':
                os.system("nmap "+ip)
                print "\n[**] Done \n"

        
        elif option == '9':
                os.system("nmap --badsum "+ip)
                print "\n[**] Done \n"

        
        elif option == '10':
                os.system("nmap -sT -Pn --spoofmac 0 "+ip)
                print "\n[**] Done \n"

        
        elif option == '11':
                os.system("nmap -f "+ip)
                print "\n[**] Done \n"
        else:
            print "Incorrect option"
	    
    def takeScreenshot(self,host, port):
	
	setdefaulttimeout(200)
	
	try:
	    browser = webdriver.Firefox(timeout=200)
	    browser.implicitly_wait(200)
	    print 'http://'+host
	    browser.get('http://{0}'.format(host))
	    screenshot = browser.get_screenshot_as_png()
	    state = True
	    browser.quit()
		
	except selenium.common.exception.WebDriverException as e:
	    print("ERROR: Do you have Firefox installed?")
	    exit(1)
	    
	except Exception as e:
	    state = False
	    print("[Error] takeScreenShot: {0}".format(e))
	    browser.quit()
	      
	    
	if state:
	    return screenshot
	else:
	    return None    