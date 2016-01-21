=====================
MSF-RPC Python Module
Release Date: December 23, 2011
Ryan Linn  <rlinn@trustwave.com>
http://www.trustwave.com
=====================
-----------------------------------------------------
A module for dealing with msgpack RPC with Metasploit
-----------------------------------------------------


Introduction
============
This module is designed to allow interaction with Metasploit msgrpc plugin to 
allow remote requests and commands to be executed through scripts and programs. 
In order to start the Metasploit msgrpc plugin to test this module, issue the 
commands in msfconsole:

	load msgrpc Pass=abc123

Once the load message appears, you should be able to run these scripts.

Using The Module
================
Creating a Msfrpc client instance
--------------------------------
To create a new instance of the client, you must import the msfrpc module, and 
then create a new Msfrpc instance.  You can specify any number of options in a 
dict form to the constructor which will allow any of the options such as host, 
port or ssl to be modifled or enabled. An example of creating a new client is :

	import msfrpc

  
  	  # Create a new instance of the Msfrpc client with the default options
  	  client = msfrpc.Msfrpc({})

Logging into Metasploit
-----------------------
Before any commands can be issued, you must authenticate into metasploit to do 
this, use the login method of the new client and specify the username and 
password to use.  The default user is always msf, and the password was specified
either through the Pass option when we loaded the msgrpc module, or assigned by 
default and presented to the screen.  To use the method we call the method with 
the two arguments:

	# Login to the msfmsg server using the password "abc123"
	client.login('msf','abc123')

Executing API Calls
-------------------
The call method allows us to call API elements from within Metasploit that are 
surfaced through the msgrpc interface.  For the first example, we will request 
the list of all exploits form the server.  To do this, we call the 
module.exploits function.

	# Get a list of the exploits from the server
	mod = client.call('module.exploits')

The information returned from the call is a dict containing the list of modules 
under the key modules. If we wanted to take the first of those modules, and then
find all of the payloads that were compatible, we could call the 
module.compatible_payloads method to find the payloads compatible with our 
exploit.  In this case, if more than one option is required a list of options are
passed.  The compatible_payloads method requires one argument: the exploit to get
more information about.
  
	# Get the list of compatible payloads for the first option
	ret = client.call('module.compatible_payloads',[mod['modules'][0]])

The ret in this case contains a dict of payloads, which can be enumerated. The 
full example can be found under the examples directory.  

Copyright
=========
MSFRPC - A module for dealing with msgpack RPC with Metasploit
Ryan Linn
Copyright (C) 2012 Trustwave Holdings, Inc.
 
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
 
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>
