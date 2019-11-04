===============================
Tool pentesting with Python
===============================

The main script is pentesting-tool.py and you need execute with python 2.7
Also you need install requeriments.txt and other modules like python-msfrpc

Install dependences from requeriments.txt
================================
pip install -r requirements.txt

Introduction
============

This tool allows obtain information about a specific ip or domain.
-----------------------------------------------------------------
It has options like port scanning and detect vulnerabilities in some ports like ftp or mysql

It has another advanced features like connecting with metasploit and nexpose for extracting information about vulnerabilities
discovered in specific servers.

<img src="https://github.com/jmortega/python-pentesting/blob/master/tool.png" alt="python-pentesting-tool"/>


Using The tool
================

The first step is introduce the target ip or domain
These are the options we can view when we have introduced a ip or domain:

1.Check Open Ports
-------------------
This option checks the ports open for a target ip or domain

2.Port Scanning
-----------------------
This option checks the ports for a target ip or domain

3.Nmap Scanning advanced
-----------------------
Check ports in more advanced mode

4.Check Option methods
-----------------------
This option checks the methods(GET,POST,PUT,DELETE) a target ip or domain

If the server doesn't support this option methods,it show an message error

5.Check DNS Servers Info
------------------------
This options show the info about DNS server for a target ip or domain

6.Check Host info fron Shodan Service
--------------------------------------
This option obtain info about the target ip from shodan services

For get info from Shodan services in the class ShodanSearch you can put your own shodanKey in the init method

7.NMAP Scanning
-------------------
This option makes a port scanning with python-nmap and for each port checks if the port is open

If the port is open,checks the nmap scripts for detecting some vulnerability in the port or in the service

The ports to analyze are:
21,22,80,8080,443,5432,3306,27017,55553,1241,9160,5900

21-->FTP

22->SSH

80,8080-->HTTP

443-->SSL

5432-->POSTGRES SQL

3306-->MySQL

27017-->MongoDB

9160-->CASSANDRA

5900-->VNC


8.Host Info by Socket Call
-----------------------------
Shows info about the call socket.gethostbyname(hostname)

9.GeoLocation Host Info
-----------------------
Shows server geolocation info with the pygeocoder library
This options uses the 'GeoLiteCity.dat' file for obtain the geolocation info

10.Scraping for images and pdf & obtain metadata
------------------------------------------------
Obtain images and pdfs from the server and metadata info that could be found inside images and pdfs

When images and pdfs are found in the server,a local folder is created for storing these items

11.Get Headers info
------------------
Check request headers info from ip and hostname

12.Get SSH user/password Brute Force
------------------------------------
If the server has the port 22 open,we can try a brute force process with dictionary for users and passwords

The script is using 2 files,users.txt and passwords.txt

This files and other dictionaries can be download from repository

https://github.com/fuzzdb-project/fuzzdb/tree/master/wordlists-user-passwd/unix-os

These files can be found in the FuzzDB project: https://code.google.com/p/fuzzdb

13.Get FTP Anonymous access
---------------------------
If the server has the port 21 open,we can check if it has anonymous access activated

14.MetaSploitFrameWork
-----------------------
You must enter information about the server where metasploit is running

Introduce IP server where MetaSploit is running:

Introduce Port server where MetaSploit is running:

Introduce user for MetaSploit:

Introduce password for MetaSploit:

15.NexposeFramework
--------------------
You must enter information about the server where nexpose is running

Introduce IP server where Nexpose is running:

Introduce Port server where Nexpose is running:

Introduce user for Nexpose:

Introduce password for Nexpose:

Logs
================
For each option ,a log file is generated

1.logOpenPorts.txt

2.logOptionMethods.txt

3.logDnsInfo.txt

4.logHostInfo.txt

5.logNScanningNmap.txt

6.logHostByName.txt

7.logGeoLocationInfo.txt

8.logScraping.txt

9.logCheckHeaders.txt

10.logSSHBruteForce.txt

11.logFTP.txt

12.metaSploit_log.txt

13.nexpose_log.txt


Libraries
================
These are the main libraries that we have to install in order to execute the program

Some libraries are easy install with pip and others like python-msfprc for metasploit framework must be install with the source code

Install requirements
====================
pip install -r requirements.txt


pythonwhois
================
pip install pythonwhois

http://cryto.net/pythonwhois/install.html


ipwhois
================
pip install ipwhois

https://pypi.python.org/pypi/ipwhois



python-nmap
================
pip install python-nmap

https://pypi.python.org/pypi/python-nmap


pygeoip
================
pip install pygeoip

https://pypi.python.org/pypi/pygeoip


pygeocoder
================
pip install pygeocoder

https://pypi.python.org/pypi/pygeocoder


shodan
================
https://shodan.readthedocs.org/en/latest/tutorial.html#installation


dnspython
================
pip install dnspython

https://pypi.python.org/pypi/dnspython/1.12.0


paramiko
================
pip install paramiko

https://pypi.python.org/pypi/paramiko/1.15.2


Paramiko also requires pyCrypto

https://pypi.python.org/pypi/pycrypto


requests
================
pip install requests

http://www.python-requests.org/en/latest/user/install/#install


msgpack
================
pip install msgpack-python

https://pypi.python.org/pypi/msgpack-python


python-msfrpc
================
https://github.com/SpiderLabs/msfrpc/tree/master/python-msfrpc
python setup install


PyPDF2
================
https://pypi.python.org/pypi/PyPDF2


lxml
================
pip install lxml


BeautifulSoup
================
pip install beautifulsoup4

http://www.crummy.com/software/BeautifulSoup


Selenium
================
pip install selenium

https://pypi.python.org/pypi/selenium


Pillow
================
Python Imaging Library

pip install Pillow



FTPLib
================
https://docs.python.org/2/library/ftplib.html


Scapy
================
It is used in an option for port scanning

http://www.secdev.org/projects/scapy

Ghost.py
================
It is used in check Headers && Clicjacking as webkit web client

http://jeanphix.me/Ghost.py/

Contact
================

Twitter

http://twitter.com/jmortegac

Web

http://about.me/jmortegac
