#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


class PrometheusStatusParser():

    def __init__(self, url):
        self.url = url


    def get_runtime_info(self, soup):
        table = soup.find('h2', text='Runtime Information').find_next_sibling('table')
        return self.parse_lines_with_header(table)


    def get_build_info(self, soup):
        table = soup.find('h2', text='Build Information').find_next_sibling('table')
        return self.parse_lines_with_header(table)

    def get_startup_flags(self, soup):
        table = soup.find('h2', text='Startup Flags').find_next_sibling('table')
        return self.parse_lines_with_header(table)


    def get_targets(self, soup):
        targets = {}

        table = soup.find('h2', text='Targets').find_next_sibling('table')

        heads = table.find('thead')

        header = heads.find('tr')
        target = header.get_text()
        fields = header.find_next_sibling('tr').find_all('th')

        body = table.find('tbody')
        lines = body.find_all('tr')

        line_infos = []
        targets[target] = line_infos

        for line in lines:
            info = {}
            line_infos.append(info)
            values = line.find_all('td')

            for name, value in zip(fields, values):
                _name = name.get_text(strip=True)
                _value = value.get_text(strip=True)
                info[_name] = _value

        return targets



    def parse_lines_with_header(self, table):
        info = {}
        lines = table.find_all('tr')
        for line in lines:
            key = line.find('th').get_text()
            val = line.find('td').get_text()
            info[key] = val
        return info



    def info(self):

        content = requests.get(self.url).content
        soup = BeautifulSoup(content)

        info = {}
        info['runtime'] = self.get_runtime_info(soup)
        info['build'] = self.get_build_info(soup)
        info['startup'] = self.get_startup_flags(soup)
        info['targets'] = self.get_targets(soup)

        return info


