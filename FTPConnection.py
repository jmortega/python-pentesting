# -*- encoding: utf-8 -*-
#class for FTP connection
import socket
import ftplib

class FTPConnection:
    
    def __init__(self,url):
        #ftp connection with ftplib library
        self.url = url
    
    def ftpConnectionAnonymous(self):
        #check port 21 is open
        try:
            sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex((self.url,21))
            if result == 0:
                print "Port 21 open"
                response = raw_input ("Would you like connect with anonymous user to the site "+ self.url +"?[s/n]")
                if response == "s" or response == "S":
                        try:
                            self.ftpClient = ftplib.FTP(self.url)
                            connect = self.ftpClient.login('anonymous', '')
			    print connect
			    print(self.ftpClient.getwelcome())
			    self.ftpClient.set_pasv(1)
			    #print(self.ftp.dir())
                            print "Connecting to site %s"%self.url
                            print self.ftpClient.retrlines('LIST')
                            self.ftpClient.quit()
                            print "Exiting site %s"%self.url
                        except Exception ,e:
			    print e
                            print "Error in listing " +self.url
            else:
                print "Port FTP 21 closed"
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