#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import string
import re


class ParserResults:

    def __init__(self, results, domain):
        self.results = results
        self.word = domain
        self.temp = []

    def genericClean(self):
        self.results = re.sub('<em>', '', self.results)
        self.results = re.sub('<b>', '', self.results)
        self.results = re.sub('</b>', '', self.results)
        self.results = re.sub('</em>', '', self.results)
        self.results = re.sub('%2f', ' ', self.results)
        self.results = re.sub('%3a', ' ', self.results)
        self.results = re.sub('<strong>', '', self.results)
        self.results = re.sub('</strong>', '', self.results)

        for e in ('>', ':', '=', '<', '/', '\\', ';', '&', '%3A', '%3D', '%3C'):
            self.results = string.replace(self.results, e, ' ')

    def urlClean(self):
        self.results = re.sub('<em>', '', self.results)
        self.results = re.sub('</em>', '', self.results)
        self.results = re.sub('%2f', ' ', self.results)
        self.results = re.sub('%3a', ' ', self.results)

        for e in ('<', '>', ':', '=', ';', '&', '%3A', '%3D', '%3C'):
            self.results = string.replace(self.results, e, ' ')

    def emails(self):
        self.genericClean()
        reg_emails = re.compile(
            '[a-zA-Z0-9.-_]*' +
            '@' +
            '(?:[a-zA-Z0-9.-]*\.)?' +
            self.word)
        self.temp = reg_emails.findall(self.results)
        emails = self.unique()
        return emails

    def fileurls(self, file):
        urls = []
        reg_urls = re.compile('<a href="(.*?)"')
        self.temp = reg_urls.findall(self.results)
        allurls = self.unique()
        for x in allurls:
            if x.count('webcache') or x.count('google.com') or x.count('search?hl'):
                pass
            else:
                urls.append(x)
        return urls

    def hostnames(self):
        self.genericClean()
        reg_hosts = re.compile('[a-zA-Z0-9.-]*\.' + self.word)
        self.temp = reg_hosts.findall(self.results)
        hostnames = self.unique()
        return hostnames

    def set(self):
        reg_sets = re.compile('>[a-zA-Z0-9]*</a></font>')
        self.temp = reg_sets.findall(self.results)
        sets = []
        for x in self.temp:
            y = string.replace(x, '>', '')
            y = string.replace(y, '</a</font', '')
            sets.append(y)
        return sets

    def hostnames_all(self):
        reg_hosts = re.compile('<cite>(.*?)</cite>')
        temp = reg_hosts.findall(self.results)
        for x in temp:
            if x.count(':'):
                res = x.split(':')[1].split('/')[2]
            else:
                res = x.split("/")[0]
            self.temp.append(res)
        hostnames = self.unique()
        return hostnames

    def unique(self):
        self.new = []
        for x in self.temp:
            if x not in self.new:
                self.new.append(x)
        return self.new
