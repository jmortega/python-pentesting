#!/usr/bin/python

import urllib2
import random
from lxml import etree
import requests
from bs4 import BeautifulSoup

class NeXposeServer():
    def __init__(self, server, port, username, password):
        self.server = server
        self.port = port
        self.username = username
        self.password = password
        self.baseurl = 'https://%s:%s' % (self.server, self.port)
        self.apipath = '/api/1.1/xml'
        self.token = ''

        # Force urllib2 to not use a proxy
        hand = urllib2.ProxyHandler({})
        opener = urllib2.build_opener(hand)
        urllib2.install_opener(opener)

        self.login()

    def asset_group_config(self, groupid):
        response = self.call("SiteConfig", {"group-id" : groupid})
        return etree.tostring(response)

    def asset_group_delete(self, groupid):
        response = self.call("AssetGroupDelete", {"group-id" : groupid})
        return etree.tostring(response)

    def asset_group_listing(self):
        response = self.call("AssetGroupListing")
        return etree.tostring(response)

    def asset_group_save(self, groupid):
        response = self.call("AssetGroupSave", {"group-id" : groupid})
        return etree.tostring(response)

    # TODO
    def console_command(self, command):
        response = self.call("ConsoleCommand", {"command" : command})
        return etree.tostring(response)

    def device_delete(self, deviceid):
        response = self.call("DeviceDelete", {"device-id" : deviceid})
        return etree.tostring(response)

    def download_report(self, reporturl):
        req = urllib2.Request(self.baseurl + reporturl)
        req.add_header('Cookie', 'nexposeCCSessionID=%s' % self.token)
        response = urllib2.urlopen(req)
        resxml = etree.XML(response.read())
        return resxml

    def engine_activity(self, engineid):
        response = self.call("EngineActivity", {"engine-id" : engineid})
        return etree.tostring(response)

    def engine_listing(self):
        response = self.call("EngineListing")
        return etree.tostring(response)

    def login(self):
        response = self.call("Login", {'user-id' : self.username, 'password' : self.password})
        self.token = response.attrib['session-id']
	print response

    def logout(self):
        response = self.call("Logout")
        return response.attrib['success']

    # TODO
    def report_adhoc_generate(self, templateid):
        response = self.call("ReportConfig", {'template-id' : templateid})
        return etree.tostring(response)

    def report_config(self, reportcfgid):
        response = self.call("ReportConfig", {'reportcfg-id' : reportcfgid})
        return etree.tostring(response)

    # TODO: report_delete should be able to delete both
    # actual reports as well as report configurations.
    def report_delete(self, reportid):
        response = self.call("ReportConfig", {'report-id' : reportid})
        return etree.tostring(response)

    def report_generate(self, reportid):
        response = self.call("ReportConfig", {'report-id' : reportid})
        return etree.tostring(response)

    def report_listing(self):
        response = self.call("ReportListing")
        return etree.tostring(response)

    # TODO
    def report_save(self, reportcfgid):
        response = self.call("ReportSave", {'reportcfg-id' : reportcfgid})
        return etree.tostring(response)

    def report_template_listing(self, templateid):
        response = self.call("ReportTemplateConfig", {'template-id' : templateid})
        return etree.tostring(response)

    # TODO
    def report_template_save(self, templateid):
        response = self.call("ReportTemplateSave", {'template-id' : templateid})
        return etree.tostring(response)

    def report_template_listing(self):
        response = self.call("ReportTemplateListing")
        return etree.tostring(response)

    def report_history(self, reportcfgid):
        response = self.call("ReportHistory", {'reportcfg-id' : reportcfgid})
        return etree.tostring(response)

    def restart(self):
        response = self.call("Restart")
        return etree.tostring(response)

    def scan_activity(self):
        response = self.call("ScanActivity")
        return etree.tostring(response)

    def scan_pause(self, scanid):
        response = self.call("ScanPause", {'scan-id' : scanid})
        return etree.tostring(response)

    def scan_resume(self, scanid):
        response = self.call("ScanResume", {'scan-id' : scanid})
        return etree.tostring(response)

    def scan_statistics(self, scanid):
        response = self.call("ScanStatistics", {'scan-id' : scanid})
        return etree.tostring(response)

    def scan_status(self, scanid):
        response = self.call("ScanStatus", {'scan-id' : scanid})
        return etree.tostring(response)

    def scan_stop(self, scanid):
        response = self.call("ScanStop", {'scan-id' : scanid})
        return etree.tostring(response)

    # TODO
    def send_log(self, keyid):
        response = self.call("SendLog", {"key-id" : keyid})
        return etree.tostring(response)

    def site_config(self, siteid):
        response = self.call("SiteConfig", {"site-id" : siteid})
        return etree.tostring(response)

    def site_delete(self, siteid):
        response = self.call("SiteDelete", {"site-id" : siteid})
        return etree.tostring(response)

    def site_device_listing(self, siteid):
        response = self.call("SiteDeviceListing", {"site-id" : siteid})
        return etree.tostring(response)

    # TODO
    def site_devices_scan(self, siteid):
        response = self.call("SiteDevicesScan", {"site-id" : siteid})
        return etree.tostring(response)

    def site_listing(self):
        response = self.call("SiteListing")
        return etree.tostring(response)

    # TODO
    def site_save(self):
        response = self.call("SiteSave")
        return etree.tostring(response)

    def site_scan(self, siteid):
        response = self.call("SiteScan", {"site-id" : siteid})
        return etree.tostring(response)

    def site_scan_history(self, siteid):
        response = self.call("SiteScanHistory", {"site-id" : siteid})
        return etree.tostring(response)

    def system_update(self):
        response = self.call("SystemUpdate")
        return etree.tostring(response)

    def system_information(self):
        response = self.call("SystemInformation")
        return etree.tostring(response)

    def user_authenticator_listing(self):
        response = self.call("UserAuthenticatorListing")
        return etree.tostring(response)

    def user_config(self, userid):
        response = self.call("UserConfig", {"id" : userid})
        return etree.tostring(response)

    def user_delete(self, userid):
        response = self.call("UserDelete", {"id" : userid})
        return etree.tostring(response)

    def user_listing(self):
        response = self.call("UserListing")
        return etree.tostring(response)

    # TODO
    def user_save(self, userid):
        response = self.call("UserSave", {"id" : userid})
        return etree.tostring(response)

    def vulnerability_details(self, vulnid):
        response = self.call("VulnerabilityDetails", {"vuln-id" : vulnid})
        return etree.tostring(response)

    def vulnerability_listing(self):
        response = self.call("VulnerabilityListing")
        return etree.tostring(response)
        
    def call(self, func, params={}):
        xml = etree.Element(func + "Request")

        if(self.token != ''):
            xml.set('session-id', self.token)
            xml.set('sync-id', str(random.randint(1,65535)))

        for param,value in params.iteritems():
            xml.set(param, str(value))
		

	header = {'Content-Type': 'text/xml'}
        response = requests.post(url=self.baseurl + self.apipath, data=etree.tostring(xml),verify=False,headers=header)
        resxml = etree.XML(response.text)

        return resxml
