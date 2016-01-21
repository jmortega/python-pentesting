#!/usr/bin/env python

""" This is the fuzzutils package. This contains useful items for performing
your fuzzing tasks agaist web applications

(c) 2010 Nathan Hamiel
Email: nathan{at}neohaxor{dot}org
Hexsec Labs: http://hexsec.com/labs

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
"""

import urllib
import urllib2
import datetime

def make_request(location, method="GET", postdata=None, headers=None):
    """ This provides a convenience function for making requests. This interfaces
    with urllib2 and provides the ability to make GET, POST, PUT and DELETE requests.
    The return data from this function is headers, content, http status, and
    the timedelta from a succesful request"""
    
    # Checks to ensure that header values and postdata are in the appropriate format
    if type(headers) != dict and headers != None:
        raise TypeError, ("headers are not a valid Python dictionary")
    if type(postdata) != str and postdata != None:
        raise TypeError, ("postdata is not a valid Python string")
    
    if headers:
        req = urllib2.Request(location, method, headers=headers)
    else:
        req = urllib2.Request(location, method)
        
    req.get_method = lambda: method.upper()
    req.add_data(postdata)
    
    # Anticipate errors from either unavailable contentt or nonexistent resources
    try:
        start = datetime.datetime.now()
        response = urllib2.urlopen(req)
        end = datetime.datetime.now()
    except urllib2.HTTPError, error:
        return(error.headers, error.msg, error.code, None)
    except urllib2.URLError, error:
        # Noneexistent resources won't have headers or status codes
        return(None, error.reason, None, None)
    else:
        headers = response.info()
        content = response.read()
        # Grab the HTTP Status Code
        code = response.getcode()
        # Compute timedelta from a successful request
        time = end - start
        return(headers, content, code, time)
    
def generate_range(start, stop, step=1, pre=None, post=None):
    """ Generate a range of values with optional stepping. Chars can be prepended or attached to
    the end of each value that is generated. """
    
    rangevals = range(start, stop, step)
    values = []
    
    try:
        if pre and post:
            for item in rangevals:
                values.append(pre + str(item) + post)
            return(values)
        elif pre:
            for item in rangevals:
                values.append(pre + str(item))
            return(values)
        elif post:
            for item in rangevals:
                values.append(str(item) + post)
            return(values)
        else:
            for item in rangevals:
                values.append(str(item))
            return(values)
    except:
        print("You did not specify all of the values necessary for this function")
        
def webstring(value):
    """ Convert a Python dictionary to a web string where the values are in the
    format of 'foo=bar&up=down'. This is necessary when processing needs to be done
    on a dictionary but the values need to be passed to urllib2 as POST data. """
    
    data = ""
    for key in value:
        newstring = key + "=" + value[key] + "&"
        data += newstring
        
    return(data.rstrip("&"))
        
    
        