# -*- encoding: utf-8 -*-
#class for obtain metadata info from images

import os
import pygeoip
import pprint
import requests
import urllib
import json
#geolocation lib

try:
    from pygeocoder import Geocoder
except Exception as e:
    print("pip install pygeocoder")
    exit(1)
    
    
class InfoLocation:

    def printRecord(self,tgt):
	try:
	    gi = pygeoip.GeoIP('GeoLiteCity.dat',pygeoip.MEMORY_CACHE)
	    rec = gi.record_by_name(tgt)
	    city = rec['city']
	    country = rec['country_name']
	    long = rec['longitude']
	    lat = rec['latitude']
	    print '[*] Target: ' + tgt + ' Geo-located. ' 
	    print '[+] '+str(city)+', '+str(country) 
	    print '[+] Latitude: '+str(lat)+ ', Longitude: '+ str(long)
	except Exception as e:
	    print str(e)
	    print "Error obtaining geolocation"
	    pass
	
    def geocode(self,latitude,longitude):
	try:
	    # 1. Build the URL.
	    aux=str(latitude)+","+str(longitude)
	    form = { "latlng": aux, "sensor": "false", "key": "AIzaSyB2KqDo8LDMrlzH9nmKN2XMHk-ZM2ib8-g"}

	
	    query = urllib.urlencode(form)
	    scheme_netloc_path = "https://maps.googleapis.com/maps/api/geocode/json"
	
	    print(scheme_netloc_path+"?"+query)
	
	    # 2. Send the request;get the response.
	
	    r = requests.get(scheme_netloc_path+"?"+query,verify=False)
	    json_data = r.json()
	
	    #encoded
	    data_string = json.dumps(json_data)
	
	    #print data_string
	
	    #Decoded
	    decoded = json.loads(data_string)
	

	    print(decoded['results'][0]['formatted_address'])
	    print(decoded['results'][0]['address_components'][1]['long_name'].encode('utf-8'))	
	    print(decoded['results'][0]['address_components'][2]['long_name'].encode('utf-8'))
	    print(decoded['results'][0]['address_components'][3]['long_name'].encode('utf-8'))
	    print(decoded['results'][0]['address_components'][4]['long_name'].encode('utf-8'))
	    print(decoded['results'][0]['address_components'][5]['long_name'].encode('utf-8'))
	    print(decoded['results'][0]['address_components'][6]['long_name'].encode('utf-8'))
	    lat_lon = decoded['results'][0]['geometry']['location']
	    print(lat_lon['lat'].encode('utf-8'))
	    print(lat_lon['lng'].encode('utf-8'))   	    
	
	except Exception,e:
	    pass
	
    def geocode2(self,address):
	try:
	
	    # 1. Build the URL.
	    aux=str(address)
	    form = { "address": aux, "sensor": "false", "key": "AIzaSyB2KqDo8LDMrlzH9nmKN2XMHk-ZM2ib8-g"}
       
	       
	    query = urllib.urlencode(form)
	    scheme_netloc_path = "https://maps.googleapis.com/maps/api/geocode/json"
	       
	    print(scheme_netloc_path+"?"+query)
	       
	    # 2. Send the request;get the response.
	    
	    r = requests.get(scheme_netloc_path+"?"+query,verify=False)
	    json_data = r.json()
	       
	    #encoded
	    data_string = json.dumps(json_data)
	           
	    #print data_string
	       
	    #Decoded
	    decoded = json.loads(data_string)
	       
       
	    print(decoded['results'][0]['formatted_address'])
	    print(decoded['results'][0]['geometry'])
	    print(decoded['results'][0]['address_components'][1]['long_name'].encode('utf-8'))	
	    print(decoded['results'][0]['address_components'][2]['long_name'].encode('utf-8'))
	    print(decoded['results'][0]['address_components'][3]['long_name'].encode('utf-8'))
	    print(decoded['results'][0]['address_components'][4]['long_name'].encode('utf-8'))
	    print(decoded['results'][0]['address_components'][5]['long_name'].encode('utf-8'))
	    print(decoded['results'][0]['address_components'][6]['long_name'].encode('utf-8'))
	    lat_lon = decoded['results'][0]['geometry']['location']
	    print(lat_lon['lat'].encode('utf-8'))
	    print(lat_lon['lng'].encode('utf-8'))    
	  
	except Exception,e:
	    pass
	
	
    def geoInfo(self,hostName,ip):
		print '\nGeoLocation Info'
		print "--------------------------"
		print hostName
		print ip
		try:
			#Informacion geolocalización
			gi = pygeoip.GeoIP('GeoLiteCity.dat',pygeoip.MEMORY_CACHE)
			pprint.pprint("Country code: %s " %(str(gi.country_code_by_name(hostName))) )
			pprint.pprint("Full record: %s " %(str(gi.record_by_addr(ip))) )
			pprint.pprint("City: %s " %((gi.record_by_addr(ip)['city']).decode('utf-8') ))
			pprint.pprint("Timezone: %s " %(str(gi.record_by_addr(ip)['time_zone'])) )
			pprint.pprint("Country name: %s " %(str(gi.country_name_by_addr(ip))) )
			pprint.pprint("Timezone: %s" %(str(gi.time_zone_by_addr(ip))) )
			pprint.pprint("Continent: %s " %(str(gi.record_by_addr(ip)['continent'])) )
			
			for record,value in gi.record_by_addr(ip).items():
				print record + "-->" + str(value)			

			city =(gi.record_by_addr(ip)['city']).decode('utf-8')
			
			print '\nGeoLocation Latitude'
			print "--------------------------"
			print gi.record_by_addr(ip)['latitude']
    
			print '\nGeoLocation Longitude'
			print "--------------------------"
			print gi.record_by_addr(ip)['longitude']
    
			latitude = gi.record_by_addr(ip)['latitude']
			longitude = gi.record_by_addr(ip)['longitude']
    
			
			
			print '\nAddress'
			print "--------------------------"
    
			#results = Geocoder.reverse_geocode(latitude, longitude)
			#pprint.pprint(results.formatted_address)
			
			self.geocode(latitude,longitude)
			self.geocode2(city)
    
		except Exception as e:
                        print str(e)
			print "Error obtaining geolocation"
			pass
