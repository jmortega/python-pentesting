#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import threading

from scapy.all import sr1, IP, TCP
    

CONCURRENCY = 5
OPEN_PORTS = []

#class for multi-threaded scanning of single ports

class ScannerScapy:
    
    def analyze_port(host, port, thread):
        
        print "[ii] Analyzing port %s" % port

        res = sr1(IP(dst=host)/TCP(dport=port), verbose=False, timeout=0.2)

        if res is not None and TCP in res:
            if res[TCP].flags == 18:
                OPEN_PORTS.append(port)

                print "Port %s opened " % port

        thread.release()
	
    #scan ports from a specific domain
    def scan_ports_multithread(self,domain,port_list):
        
        thread = threading.BoundedSemaphore(value=CONCURRENCY)
        
        threads = []
        
        ports = port_list.split(',')
        
        #iterate over port_list
        for x in xrange(ports):
            
            t = threading.Thread(target=analyze_port, args=("domain", x, thread, ))
            threads.append(t)
        
            t.start()
        
            thread.acquire()
        
        for x in threads:
            x.join()
        
        print "[*] Ports opened:"
        for x in OPEN_PORTS:
            print "     - %s/TCP" % x
        print