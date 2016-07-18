#class foR NMAP Scanning

import nmap
from datetime import datetime

def callbackHTTP(host, result):
        try:
                script = result['scan'][host]['tcp'][80]['script']
                for key, value in script.items():
                        print 'Script {0} --> {1}'.format(key, value)
        except Exception,KeyError:
                # Key is not present
                pass

def callbackPostgres(host, result):
        try:
            script = result['scan'][host]['tcp'][5432]['script']

            for key, value in script.items():
                print 'Script {0} --> {1}'.format(key, value)
        except KeyError:
            # Key is not present
                pass
 
def callbackMySql(host, result):
        try:
            script = result['scan'][host]['tcp'][3306]['script']

            for key, value in script.items():
                print 'Script {0} --> {1}'.format(key, value)
        except KeyError:
            # Key is not present
            pass

def callbackMongoDB(host, result):
        try:
            script = result['scan'][host]['tcp'][27017]['script']

            for key, value in script.items():
                print 'Script {0} --> {1}'.format(key, value)
        except KeyError:
            # Key is not present
            pass
    
def callbackSSH(host, result):
        try:
            script = result['scan'][host]['tcp'][22]['script']

            for key, value in script.items():
                print 'Script {0} --> {1}'.format(key, value)
        except KeyError:
            # Key is not present
            pass  

def callbackFTP(host, result):
        try:
            script = result['scan'][host]['tcp'][21]['script']

            for key, value in script.items():
                print 'Script {0} --> {1}'.format(key, value)
        except KeyError:
            # Key is not present
            pass  
    
def callbackSSL(host, result):
        try:
            script = result['scan'][host]['tcp'][443]['script']

            for key, value in script.items():
                print 'Script {0} --> {1}'.format(key, value)
        except KeyError:
            # Key is not present
            pass  

def callbackVNC(host, result):
        try:
            script = result['scan'][host]['tcp'][5900]['script']

            for key, value in script.items():
                print 'Script {0} --> {1}'.format(key, value)
        except KeyError:
            # Key is not present
            pass  
    
def callbackMetaExploit(host, result):
        try:
            script = result['scan'][host]['tcp'][55553]['script']

            for key, value in script.items():
                print 'Script {0} --> {1}'.format(key, value)
        except KeyError:
            # Key is not present
            pass  
    
 
def callbackNessus(host, result):
        try:
            script = result['scan'][host]['tcp'][1241]['script']

            for key, value in script.items():
                print 'Script {0} --> {1}'.format(key, value)
        except KeyError:
            # Key is not present
            pass
    
def callbackCassandra(host, result):
        try:
            script = result['scan'][host]['tcp'][9160]['script']

            for key, value in script.items():
                print 'Script {0} --> {1}'.format(key, value)
        except KeyError:
            # Key is not present
            pass
        
class ScanningNMAP:
    
    def __init__(self):
        #Escaneo asincrono
        self.nma = nmap.PortScannerAsync()
        #Escaneo sincrono
        self.nm = nmap.PortScanner()
        
    def scanNMAP(self,ip,portlist):
        print "Cheking ports...."
        print portlist
        results = self.nm.scan(ip, portlist,arguments='-sSV -A -n -T5')
        
        # Command info
        print "[*] Execuing command: %s" % self.nm.command_line()        

        print results['scan'].keys()
        try:
                for port in self.nm[ip]['tcp']:
                
                        thisDict = self.nm[ip]['tcp'][port]
                        print 'Port ' + str(port) + ': ' + thisDict['state'] + ' ' + thisDict['name']
        except Exception:
                pass
            
    def scanning(self):
        while self.nma.still_scanning():
            self.nma.wait(5)
        
    def scanningNmapUnix(self, ip, hostname,portlist):
    
        print 'Scannning NMAP Unix....................'
    
        # Check what time the scan started
        t1 = datetime.now()
        
        self.nm.scan(ip, arguments="-A -sV -p"+portlist)
        
        # Command info
        print "[*] Execuing command: %s" % self.nm.command_line()        

        print self.nm.scaninfo()
        print self.nm.all_hosts()

        host = self.nm.all_hosts()[0]
        print 'Host: ' + host
        print self.nm[host]['status']
        print self.nm[host]['tcp']

        for port in self.nm[host]['tcp']:
            print 'Port {0} --> {1}'.format(port,self.nm[host]['tcp'][port]['state'])
            
            #mysql
            if (port==3306) and self.nm[host]['tcp'][port]['state']=='open':
                print 'Checking MYSQL port with nmap scripts......'
                #scripts for mysql:3306 open
                print 'Checking mysql-audit.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p3306 --script=/usr/share/nmap/scripts/mysql-audit.nse",callback=callbackMySql)
                self.scanning()
                print 'Checking mysql-brute.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p3306 --script=/usr/share/nmap/scripts/mysql-brute.nse",callback=callbackMySql)
                self.scanning()
                print 'Checking mysql-databases.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p3306 --script=/usr/share/nmap/scripts/mysql-databases.nse",callback=callbackMySql)
                self.scanning()
                print 'Checking mysql-databases.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p3306 --script=/usr/share/nmap/scripts/mysql-dump-hashes.nse",callback=callbackMySql)
                self.scanning()
                print 'Checking mysql-dump-hashes.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p3306 --script=/usr/share/nmap/scripts/mysql-empty-password.nse",callback=callbackMySql)
                self.scanning()
                print 'Checking mysql-enum.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p3306 --script=/usr/share/nmap/scripts/mysql-enum.nse",callback=callbackMySql)
                self.scanning()
                print 'Checking mysql-info.nse".....'
                self.nma.scan(hostname,arguments="-A -sV -p3306 --script=/usr/share/nmap/scripts/mysql-info.nse",callback=callbackMySql)
                self.scanning()
                print 'Checking mysql-query.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p3306 --script=/usr/share/nmap/scripts/mysql-query.nse",callback=callbackMySql)
                self.scanning()
                print 'Checking mysql-users.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p3306 --script=/usr/share/nmap/scripts/mysql-users.nse",callback=callbackMySql)
                self.scanning()
                print 'Checking mysql-variables.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p3306 --script=/usr/share/nmap/scripts/mysql-variables.nse",callback=callbackMySql)
                self.scanning()
                print 'Checking mysql-vuln-cve2012-2122.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p3306 --script=/usr/share/nmap/scripts/mysql-vuln-cve2012-2122.nse",callback=callbackMySql)
                self.scanning()
            
            #FTP
            if (port==21) and self.nm[host]['tcp'][port]['state']=='open':
                print 'Checking ftp port with nmap scripts......'
                #scripts for ftp:21 open
                print 'Checking ftp-anon.nse .....'
                self.nma.scan(hostname,arguments="-A -sV -p21 --script=/usr/share/nmap/scripts/ftp-anon.nse",callback=callbackFTP)
                self.scanning()
                print 'Checking ftp-bounce.nse  .....'
                self.nma.scan(hostname,arguments="-A -sV -p21 --script=/usr/share/nmap/scripts/ftp-bounce.nse",callback=callbackFTP)
                self.scanning()
                print 'Checking ftp-brute.nse  .....'
                self.nma.scan(hostname,arguments="-A -sV -p21 --script=/usr/share/nmap/scripts/ftp-brute.nse",callback=callbackFTP)
                self.scanning()
                print 'Checking ftp-libopie.nse  .....'
                self.nma.scan(hostname,arguments="-A -sV -p21 --script=/usr/share/nmap/scripts/ftp-libopie.nse",callback=callbackFTP)
                self.scanning()
                print 'Checking ftp-proftpd-backdoor.nse  .....'
                self.nma.scan(hostname,arguments="-A -sV -p21 --script=/usr/share/nmap/scripts/ftp-proftpd-backdoor.nse",callback=callbackFTP)
                self.scanning()
                print 'Checking ftp-vsftpd-backdoor.nse   .....'
                self.nma.scan(hostname,arguments="-A -sV -p21 --script=/usr/share/nmap/scripts/ftp-vsftpd-backdoor.nse",callback=callbackFTP)
                self.scanning()
            
            #vnc
            if (port==5900) and self.nm[host]['tcp'][port]['state']=='open':
                print 'Checking VNC port with nmap scripts......'
                #scripts for vnc:5900 open
                print 'Checking vnc-brute.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p5900 --script=/usr/share/nmap/scripts/vnc-brute.nse",callback=callbackVNC)
                self.scanning()
                print 'Checking vnc-info.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p5900 --script=/usr/share/nmap/scripts/vnc-info.nse",callback=callbackVNC)
                self.scanning()
                
            #postgres
            if (port==5432) and self.nm[host]['tcp'][port]['state']=='open':
                print 'Checking POSTGRES port with nmap scripts......'
                #scripts for postgres:5432 open
                print 'Checking pgsql-brute.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p5432 --script=/usr/share/nmap/scripts/pgsql-brute.nse",callback=callbackPostgres)
                self.scanning()
                
            #mongodb
            if (port==27017) and self.nm[host]['tcp'][port]['state']=='open':
                print 'Checking MONGODB port with nmap scripts......'
                #scripts for mondogb:27017 open
                print 'Checking mongodb-brute.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p27017 --script=/usr/share/nmap/scripts/mongodb-brute.nse",callback=callbackMongoDB)
                self.scanning()
                print 'Checking mongodb-databases.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p27017 --script=/usr/share/nmap/scripts/mongodb-databases.nse",callback=callbackMongoDB)
                self.scanning()
                print 'Checking mongodb-info.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p27017 --script=/usr/share/nmap/scripts/mongodb-info.nse",callback=callbackMongoDB)
                self.scanning()
                
            #cassandra
            if (port==9160) and self.nm[host]['tcp'][port]['state']=='open':
                print 'Checking CASSANDRA port with nmap scripts......'
                #scripts for cassandra:9160 open
                print 'Checking cassandra-brute.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p9160 --script=/usr/share/nmap/scripts/cassandra-brute.nse",callback=callbackCassandra)
                self.scanning()
                print 'Checking cassandra-info.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p9160 --script=/usr/share/nmap/scripts/cassandra-info.nse",callback=callbackCassandra)
                self.scanning()
            
            #ssl
            if (port==443) and self.nm[host]['tcp'][port]['state']=='open':
                print 'Checking SSL port with nmap scripts......'
                #scripts for ssl:443 open
                print 'Checking ssl-cert.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p443 --script=/usr/share/nmap/scripts/ssl-cert.nse",callback=callbackSSL)
                self.scanning()
                print 'Checking ssl-date.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p443 --script=/usr/share/nmap/scripts/ssl-date.nse",callback=callbackSSL)
                self.scanning()
                print 'Checking ssl-enum-ciphers.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p443 --script=/usr/share/nmap/scripts/ssl-enum-ciphers.nse",callback=callbackSSL)
                self.scanning()
                print 'Checking ssl-google-cert-catalog.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p443 --script=/usr/share/nmap/scripts/ssl-google-cert-catalog.nse",callback=callbackSSL)
                self.scanning()
                print 'Checking ssl-known-key.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p443 --script=/usr/share/nmap/scripts/ssl-known-key.nse",callback=callbackSSL)
                self.scanning()
                print 'Checking sslv2.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p443 --script=/usr/share/nmap/scripts/sslv2.nse",callback=callbackSSL)
                self.scanning()
                
            #ssh
            if (port==22) and self.nm[host]['tcp'][port]['state']=='open':
                print 'Checking SSH port with nmap scripts......'
                #scripts for SSH:22 open
                print 'Checking ssh-hostkey.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p22 --script=/usr/share/nmap/scripts/ssh-hostkey.nse",callback=callbackSSH)
                self.scanning()
                print 'Checking ssh2-enum-algos.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p22 --script=/usr/share/nmap/scripts/ssh2-enum-algos.nse",callback=callbackSSH)
                self.scanning()
                print 'Checking sshv1.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p22 --script=/usr/share/nmap/scripts/sshv1.nse",callback=callbackSSH)
                self.scanning()
                
            #metaexploit
            if (port==55553) and self.nm[host]['tcp'][port]['state']=='open':
                print 'Checking METAEXPLOIT port with nmap scripts......'
                #scripts for metaexploit:55553 open
                print 'Checking metasploit-info.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p55553 --script=/usr/share/nmap/scripts/metasploit-info.nse",callback=callbackMetaExploit)
                self.scanning()
                print 'Checking metasploit-msgrpc-brute.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p55553 --script=/usr/share/nmap/scripts/metasploit-msgrpc-brute.nse",callback=callbackMetaExploit)
                self.scanning()
                print 'Checking metasploit-xmlrpc-brute.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p55553 --script=/usr/share/nmap/scripts/metasploit-xmlrpc-brute.nse",callback=callbackMetaExploit)
                self.scanning()
                
            #nessus
            if (port==1241) and self.nm[host]['tcp'][port]['state']=='open':
                print 'Checking NESSUS port with nmap scripts......'
                #scripts for nessus:1241 open
                print 'Checking netbus-brute.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p1241 --script=/usr/share/nmap/scripts/netbus-brute.nse",callback=callbackNessus)
                self.scanning()
                print 'Checking nessus-xmlrpc-brute.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p1241 --script=/usr/share/nmap/scripts/nessus-xmlrpc-brute.nse",callback=callbackNessus)
                self.scanning()
                
            #http
            if (port==80 or port==8080) and self.nm[host]['tcp'][port]['state']=='open':
                print 'Checking HTTP port with nmap scripts......'
                #scripts for http:80 open
                print 'Obtain Hosts on IP hostmap-bfk.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/hostmap-bfk.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking dns-brute.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/dns-brute.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-adobe-coldfusion-apsa1301.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-adobe-coldfusion-apsa1301.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-affiliate-id.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-affiliate-id.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-apache-negotiation.nse.....'
                self.nma.scan(hostname,arguments="-A -sS -p80 --script=/usr/share/nmap/scripts/http-apache-negotiation.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-auth-finder.nse....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-auth-finder.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-auth.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-auth.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-awstatstotals-exec.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-awstatstotals-exec.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-axis2-dir-traversal.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-axis2-dir-traversal.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-backup-finder.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-backup-finder.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-barracuda-dir-traversal.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-barracuda-dir-traversal.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-barracuda-dir-traversal.nse....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-brute.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-cakephp-version.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-cakephp-version.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-chrono.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-chrono.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-coldfusion-subzero.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-coldfusion-subzero.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-comments-displayer.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-comments-displayer.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-config-backup.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-config-backup.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-cors.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-cors.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-date.nse....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-date.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-default-accounts.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-default-accounts.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-domino-enum-passwords.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-domino-enum-passwords.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-drupal-enum-users.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-drupal-enum-users.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-drupal-modules.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-drupal-modules.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-email-harvest.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-email-harvest.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-enum.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-enum.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-exif-spider.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-exif-spider.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-favicon.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-favicon.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-fileupload-exploiter.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-fileupload-exploiter.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-form-brute.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-form-brute.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-form-fuzzer.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-form-fuzzer.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-frontpage-login.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-frontpage-login.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-generator.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-generator.nse",callback=callbackHTTP)
                self.scanning()
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-git.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-gitweb-projects-enum.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-gitweb-projects-enum.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-google-malware.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-google-malware.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-grep.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-grep.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-headers.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-headers.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-huawei-hg5xx-vuln.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-huawei-hg5xx-vuln.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-icloud-findmyiphone.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-icloud-findmyiphone.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-icloud-sendmsg.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-icloud-sendmsg.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-iis-webdav-vuln.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-iis-webdav-vuln.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-joomla-brute.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-joomla-brute.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-litespeed-sourcecode-download.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-litespeed-sourcecode-download.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-majordomo2-dir-traversal.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-majordomo2-dir-traversal.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-malware-host.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-malware-host.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-method-tamper.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-method-tamper.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-methods.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-methods.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-open-proxy.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-open-proxy.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-open-redirect.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-open-redirect.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-passwd.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-passwd.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-php-version.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-php-version.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-phpmyadmin-dir-traversal.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-phpmyadmin-dir-traversal.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking netbus-brute.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-phpself-xss.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-proxy-brute.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-proxy-brute.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-put.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-put.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-qnap-nas-info.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-qnap-nas-info.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-rfi-spider.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-rfi-spider.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-robots.txt.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-robots.txt.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-robtex-reverse-ip.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-robtex-reverse-ip.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-robtex-shared-ns.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-robtex-shared-ns.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-sitemap-generator.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-sitemap-generator.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-slowloris-check.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-slowloris-check.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-slowloris.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-slowloris.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-sql-injection.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-sql-injection.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking hhttp-stored-xss.nse....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/hhttp-stored-xss.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-title.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-title.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-tplink-dir-traversal.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-tplink-dir-traversal.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-trace.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-trace.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-traceroute.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-traceroute.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-unsafe-output-escaping.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-unsafe-output-escaping.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-userdir-enum.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-userdir-enum.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-vhosts.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-vhosts.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-virustotal.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-virustotal.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-vlcstreamer-ls.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-vlcstreamer-ls.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-vmware-path-vuln.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-vmware-path-vuln.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-vuln-cve2009-3960.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-vuln-cve2009-3960.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-vuln-cve2010-0738.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-vuln-cve2010-0738.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-vuln-cve2010-2861.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-vuln-cve2010-2861.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-vuln-cve2011-3192.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-vuln-cve2011-3192.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-vuln-cve2011-3368.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-vuln-cve2011-3368.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-vuln-cve2012-1823.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-vuln-cve2012-1823.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-vuln-cve2013-0156.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-vuln-cve2013-0156.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-waf-detect.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-waf-detect.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-waf-fingerprint.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-waf-fingerprint.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-wordpress-brute.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-wordpress-brute.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-wordpress-enum.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-wordpress-enum.nse",callback=callbackHTTP)
                self.scanning()
                print 'Checking http-wordpress-plugins.nse.....'
                self.nma.scan(hostname,arguments="-A -sV -p80 --script=/usr/share/nmap/scripts/http-wordpress-plugins.nse",callback=callbackHTTP)
                self.scanning()
                
        # Checking the time again
        t2 = datetime.now()

        # Calculates the difference of time, to see how long it took to run the script
        total =  t2 - t1

        # Printing the information to screen
        print 'Scanning Completed in: ', total

    def scanningNmapWindows(self, ip, hostname, portlist):
            
        print 'Scannning NMAP Windows....................'
    
        # Check what time the scan started
        t1 = datetime.now()
        
        self.nm.scan(ip, arguments="-A -sT -p"+portlist)
        
        # Command info
        print "[*] Execuing command: %s" % self.nm.command_line()        

        print self.nm.scaninfo()
        print self.nm.all_hosts()
        
        if len(self.nm.all_hosts())>0:
                host = self.nm.all_hosts()[0]
                print 'Host: ' + host
                
                print self.nm[host]['status']
                print self.nm[host]['tcp']

                for port in self.nm[host]['tcp']:
                        print 'Port {0} --> {1}'.format(port,self.nm[host]['tcp'][port]['state'])
            
                        #mysql
                        if (port==3306) and self.nm[host]['tcp'][port]['state']=='open':
                                print 'Checking MYSQL port with nmap scripts......'
                                #scripts for mysql:3306 open
                                print 'Checking mysql-audit.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p3306 --script mysql-audit.nse",callback=callbackMySql)
                                self.scanning()
                                print 'Checking mysql-brute.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p3306 --script mysql-brute.nse",callback=callbackMySql)
                                self.scanning()
                                print 'Checking mysql-databases.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p3306 --script mysql-databases.nse",callback=callbackMySql)
                                self.scanning()
                                print 'Checking mysql-databases.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p3306 --script mysql-dump-hashes.nse",callback=callbackMySql)
                                self.scanning()
                                print 'Checking mysql-dump-hashes.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p3306 --script mysql-empty-password.nse",callback=callbackMySql)
                                self.scanning()
                                print 'Checking mysql-enum.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p3306 --script mysql-enum.nse",callback=callbackMySql)
                                self.scanning()
                                print 'Checking mysql-info.nse".....'
                                self.nma.scan(hostname,arguments="-A -sV -p3306 --script mysql-info.nse",callback=callbackMySql)
                                self.scanning()
                                print 'Checking mysql-query.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p3306 --script mysql-query.nse",callback=callbackMySql)
                                self.scanning()
                                print 'Checking mysql-users.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p3306 --script mysql-users.nse",callback=callbackMySql)
                                self.scanning()
                                print 'Checking mysql-variables.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p3306 --script mysql-variables.nse",callback=callbackMySql)
                                self.scanning()
                                print 'Checking mysql-vuln-cve2012-2122.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p3306 --script mysql-vuln-cve2012-2122.nse",callback=callbackMySql)
                                self.scanning()
            
                                #FTP
                        if (port==21) and self.nm[host]['tcp'][port]['state']=='open':
                                print 'Checking ftp port with nmap scripts......'
                                #scripts for ftp:21 open
                                print 'Checking ftp-anon.nse .....'
                                self.nma.scan(hostname,arguments="-A -sV -p21 --script ftp-anon.nse",callback=callbackFTP)
                                self.scanning()
                                print 'Checking ftp-bounce.nse  .....'
                                self.nma.scan(hostname,arguments="-A -sV -p21 --script ftp-bounce.nse",callback=callbackFTP)
                                self.scanning()
                                print 'Checking ftp-brute.nse  .....'
                                self.nma.scan(hostname,arguments="-A -sV -p21 --script ftp-brute.nse",callback=callbackFTP)
                                self.scanning()
                                print 'Checking ftp-libopie.nse  .....'
                                self.nma.scan(hostname,arguments="-A -sV -p21 --script ftp-libopie.nse",callback=callbackFTP)
                                self.scanning()
                                print 'Checking ftp-proftpd-backdoor.nse  .....'
                                self.nma.scan(hostname,arguments="-A -sV -p21 --script ftp-proftpd-backdoor.nse",callback=callbackFTP)
                                self.scanning()
                                print 'Checking ftp-vsftpd-backdoor.nse   .....'
                                self.nma.scan(hostname,arguments="-A -sV -p21 --script ftp-vsftpd-backdoor.nse",callback=callbackFTP)
                                self.scanning()
            
                                #vnc
                        if (port==5900) and self.nm[host]['tcp'][port]['state']=='open':
                                print 'Checking VNC port with nmap scripts......'
                                #scripts for vnc:5900 open
                                print 'Checking vnc-brute.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p5900 --script vnc-brute.nse",callback=callbackVNC)
                                self.scanning()
                                print 'Checking vnc-info.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p5900 --script vnc-info.nse",callback=callbackVNC)
                                self.scanning()
                
                                #postgres
                        if (port==5432) and self.nm[host]['tcp'][port]['state']=='open':
                                print 'Checking POSTGRES port with nmap scripts......'
                                #scripts for postgres:5432 open
                                print 'Checking pgsql-brute.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p5432 --script pgsql-brute.nse",callback=callbackPostgres)
                                self.scanning()
        
                                #mongodb
                        if (port==27017) and self.nm[host]['tcp'][port]['state']=='open':
                                print 'Checking MONGODB port with nmap scripts......'
                                #scripts for mondogb:27017 open
                                print 'Checking mongodb-brute.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p27017 --script mongodb-brute.nse",callback=callbackMongoDB)
                                self.scanning()
                                print 'Checking mongodb-databases.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p27017 --script mongodb-databases.nse",callback=callbackMongoDB)
                                self.scanning()
                                print 'Checking mongodb-info.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p27017 --script mongodb-info.nse",callback=callbackMongoDB)
                                self.scanning()
                
                                #cassandra
                        if (port==9160) and self.nm[host]['tcp'][port]['state']=='open':
                                print 'Checking CASSANDRA port with nmap scripts......'
                                #scripts for cassandra:9160 open
                                print 'Checking cassandra-brute.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p9160 --script cassandra-brute.nse",callback=callbackCassandra)
                                self.scanning()
                                print 'Checking cassandra-info.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p9160 --script cassandra-info.nse",callback=callbackCassandra)
                                self.scanning()
        
                                #ssl
                        if (port==443) and self.nm[host]['tcp'][port]['state']=='open':
                                print 'Checking SSL port with nmap scripts......'
                                #scripts for ssl:443 open
                                print 'Checking ssl-cert.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p443 --script ssl-cert.nse",callback=callbackSSL)
                                self.scanning()
                                print 'Checking ssl-date.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p443 --script ssl-date.nse",callback=callbackSSL)
                                self.scanning()
                                print 'Checking ssl-enum-ciphers.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p443 --script ssl-enum-ciphers.nse",callback=callbackSSL)
                                self.scanning()
                                print 'Checking ssl-google-cert-catalog.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p443 --script ssl-google-cert-catalog.nse",callback=callbackSSL)
                                self.scanning()
                                print 'Checking ssl-known-key.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p443 --script ssl-known-key.nse",callback=callbackSSL)
                                self.scanning()
                                print 'Checking sslv2.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p443 --script sslv2.nse",callback=callbackSSL)
                                self.scanning()
        
                                #ssh
                        if (port==22) and self.nm[host]['tcp'][port]['state']=='open':
                                print 'Checking SSH port with nmap scripts......'
                                #scripts for SSH:22 open
                                print 'Checking ssh-hostkey.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p22 --script ssh-hostkey.nse",callback=callbackSSH)
                                self.scanning()
                                print 'Checking ssh2-enum-algos.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p22 --script ssh2-enum-algos.nse",callback=callbackSSH)
                                self.scanning()
                                print 'Checking sshv1.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p22 --script sshv1.nse",callback=callbackSSH)
                                self.scanning()
                
                                #metaexploit
                        if (port==55553) and self.nm[host]['tcp'][port]['state']=='open':
                                print 'Checking METAEXPLOIT port with nmap scripts......'
                                #scripts for metaexploit:55553 open
                                print 'Checking metasploit-info.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p55553 --script metasploit-info.nse",callback=callbackMetaExploit)
                                self.scanning()
                                print 'Checking metasploit-msgrpc-brute.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p55553 --script metasploit-msgrpc-brute.nse",callback=callbackMetaExploit)
                                self.scanning()
                                print 'Checking metasploit-xmlrpc-brute.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p55553 --script metasploit-xmlrpc-brute.nse",callback=callbackMetaExploit)
                                self.scanning()
                
                                #nessus
                        if (port==1241) and self.nm[host]['tcp'][port]['state']=='open':
                                print 'Checking NESSUS port with nmap scripts......'
                                #scripts for nessus:1241 open
                                print 'Checking netbus-brute.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p1241 --script netbus-brute.nse",callback=callbackNessus)
                                self.scanning()
                                print 'Checking nessus-xmlrpc-brute.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p1241 --script nessus-xmlrpc-brute.nse",callback=callbackNessus)
                                self.scanning()
                
                                #http
                        if (port==80 or port==8080) and self.nm[host]['tcp'][port]['state']=='open':
                                print 'Checking HTTP port with nmap scripts......'
                                #scripts for http:80 open
                                print 'Obtain Hosts on IP hostmap-bfk.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script hostmap-bfk.nse",callback=callbackHTTP)
                                self.scanning() 
                                print 'Checking dns-brute.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script dns-brute.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-adobe-coldfusion-apsa1301.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-adobe-coldfusion-apsa1301.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-affiliate-id.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-affiliate-id.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-apache-negotiation.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-apache-negotiation.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-auth-finder.nse....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-auth-finder.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-auth.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-auth.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-awstatstotals-exec.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-awstatstotals-exec.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-axis2-dir-traversal.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-axis2-dir-traversal.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-backup-finder.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-backup-finder.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-barracuda-dir-traversal.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-barracuda-dir-traversal.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-barracuda-dir-traversal.nse....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-brute.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-cakephp-version.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-cakephp-version.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-chrono.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-chrono.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-coldfusion-subzero.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-coldfusion-subzero.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-comments-displayer.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-comments-displayer.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-config-backup.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-config-backup.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-cors.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-cors.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-date.nse....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-date.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-default-accounts.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-default-accounts.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-domino-enum-passwords.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-domino-enum-passwords.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-drupal-enum-users.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-drupal-enum-users.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-drupal-modules.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-drupal-modules.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-email-harvest.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-email-harvest.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-enum.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-enum.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-exif-spider.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-exif-spider.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-favicon.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-favicon.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-fileupload-exploiter.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-fileupload-exploiter.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-form-brute.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-form-brute.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-form-fuzzer.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-form-fuzzer.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-frontpage-login.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-frontpage-login.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-generator.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-generator.nse",callback=callbackHTTP)
                                self.scanning()
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-git.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-gitweb-projects-enum.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-gitweb-projects-enum.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-google-malware.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-google-malware.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-grep.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-grep.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-headers.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-headers.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-huawei-hg5xx-vuln.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-huawei-hg5xx-vuln.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-icloud-findmyiphone.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-icloud-findmyiphone.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-icloud-sendmsg.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-icloud-sendmsg.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-iis-webdav-vuln.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-iis-webdav-vuln.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-joomla-brute.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-joomla-brute.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-litespeed-sourcecode-download.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-litespeed-sourcecode-download.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-majordomo2-dir-traversal.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-majordomo2-dir-traversal.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-malware-host.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-malware-host.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-method-tamper.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-method-tamper.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-methods.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-methods.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-open-proxy.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-open-proxy.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-open-redirect.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-open-redirect.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-passwd.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-passwd.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-php-version.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-php-version.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-phpmyadmin-dir-traversal.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-phpmyadmin-dir-traversal.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking netbus-brute.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-phpself-xss.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-proxy-brute.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-proxy-brute.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-put.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-put.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-qnap-nas-info.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-qnap-nas-info.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-rfi-spider.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-rfi-spider.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-robots.txt.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-robots.txt.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-robtex-reverse-ip.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-robtex-reverse-ip.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-robtex-shared-ns.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-robtex-shared-ns.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-sitemap-generator.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-sitemap-generator.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-slowloris-check.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-slowloris-check.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-slowloris.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-slowloris.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-sql-injection.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-sql-injection.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking hhttp-stored-xss.nse....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script hhttp-stored-xss.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-title.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-title.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-tplink-dir-traversal.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-tplink-dir-traversal.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-trace.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-trace.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-traceroute.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-traceroute.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-unsafe-output-escaping.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-unsafe-output-escaping.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-userdir-enum.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-userdir-enum.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-vhosts.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-vhosts.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-virustotal.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-virustotal.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-vlcstreamer-ls.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-vlcstreamer-ls.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-vmware-path-vuln.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-vmware-path-vuln.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-vuln-cve2009-3960.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-vuln-cve2009-3960.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-vuln-cve2010-0738.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-vuln-cve2010-0738.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-vuln-cve2010-2861.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-vuln-cve2010-2861.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-vuln-cve2011-3192.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-vuln-cve2011-3192.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-vuln-cve2011-3368.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-vuln-cve2011-3368.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-vuln-cve2012-1823.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-vuln-cve2012-1823.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-vuln-cve2013-0156.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-vuln-cve2013-0156.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-waf-detect.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-waf-detect.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-waf-fingerprint.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-waf-fingerprint.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-wordpress-brute.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-wordpress-brute.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-wordpress-enum.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-wordpress-enum.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-wordpress-plugins.nse.....'
                                self.nma.scan(hostname,arguments="-A -sV -p80 --script http-wordpress-plugins.nse",callback=callbackHTTP)
                                self.scanning()
 
        # Checking the time again
        t2 = datetime.now()

        # Calculates the difference of time, to see how long it took to run the script
        total =  t2 - t1

        # Printing the information to screen
        print 'Scanning Completed in: ', total
