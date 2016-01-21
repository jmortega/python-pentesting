#!/usr/bin/env python
# MSF-RPC - A  Python library to facilitate MSG-RPC communication with Metasploit
# Ryan Linn  - RLinn@trustwave.com
# Copyright (C) 2011 Trustwave
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program. If not, see <http://www.gnu.org/licenses/>.

from distutils.core import setup

setup(name='msfrpc',
      version='0.1',
      description='Python MSF-RPC Bindings',
      author='Ryan Linn',
      author_email='RLinn@trustwave.com',
      url='http://www.trustwave.com',
      license='GPLv3',
      py_modules=['msfrpc'],
     )
