#!/usr/bin/env python
# MSF-RPC - A  Python library to facilitate MSG-RPC communication with Metasploit
# Ryan Linn  - RLinn@trustwave.com
# Copyright (C) 2011 Trustwave
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program. If not, see <http://www.gnu.org/licenses/>.

import msfrpc

if __name__ == '__main__':
  
  # Create a new instance of the Msfrpc client with the default options
  client = msfrpc.Msfrpc({})

  # Login to the msfmsg server using the password "abc123"
  client.login('msf','abc123')

  # Get a list of the exploits from the server
  mod = client.call('module.exploits')
  
  # Grab the first item from the modules value of the returned dict
  print "Compatible payloads for : %s\n" % mod['modules'][0]
  
  # Get the list of compatible payloads for the first option
  ret = client.call('module.compatible_payloads',[mod['modules'][0]])
  for i in (ret.get('payloads')):
    print "\t%s" % i

