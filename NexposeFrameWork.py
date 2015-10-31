# -*- encoding: utf-8 -*-
#class for connecting with NexposeFrameWork with pynexposeHttps

from bs4 import BeautifulSoup

class NexposeFrameWork:
    def __init__(self, pynexposeHttps):
        self.pynexposeHttps = pynexposeHttps

    def siteListing(self):
        print "\nSites"
        print "--------------------------"
        bsoupSiteListing = BeautifulSoup(self.pynexposeHttps.site_listing(),'lxml')
        for site in bsoupSiteListing.findAll('sitesummary'):
            attrs = dict(site.attrs)
            print "Description: " + attrs['description']
            print "riskscore: " + attrs['riskscore']
            print "Id: " + attrs['id']
            print "riskfactor: " + attrs['riskfactor']
            print "name: " + attrs['name']
            print "\n"

    def vulnerabilityListing(self): 
        print "\nVulnerabilities"
        print "--------------------------"
        bsoupVulnerabilityListing = BeautifulSoup(self.pynexposeHttps.vulnerability_listing(),'lxml')
        for vulnerability in bsoupVulnerabilityListing.findAll('vulnerabilitysummary'):
            attrs = dict(vulnerability.attrs)
            print "Id: " + attrs['id']
            print "Severity: " + attrs['severity']
            print "Title: " + attrs['title']
            bsoupVulnerabilityDetails = BeautifulSoup(self.pynexposeHttps.vulnerability_details(attrs['id']),'lxml')
            for vulnerability_description in bsoupVulnerabilityDetails.findAll('description'):
                print "Description: " + vulnerability_description.text
                print "\n"