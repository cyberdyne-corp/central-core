#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import datetime
import json

class PrometheusQuery():

    def __init__(self, url, endpoint='/api/v1'):
        self.q = url + endpoint + '/query'
        self.range = url + endpoint + '/query_range'


    def now(self):
        return datetime.datetime.utcnow().isoformat() + 'Z'


    def at(self, offset):
        previous = datetime.datetime.utcnow() - datetime.timedelta(seconds=offset)
        return previous.isoformat() + 'Z'

    def query_range(self, query, offset=5, step=1):
        start = self.at(offset)
        end = self.now()
        return requests.get(self.range + '?query=' + query + '&start=' + start + '&end=' + end + '&step=' + str(step)).content


    def query(self, query):
        return requests.get(self.q + '?query=' + query + '&time=' + self.now()).content


    def extract(self, result, raw=False):
        if (not raw):
            data = json.loads(result)
            return data['data']['result'][0]['value'][1]

        return result


    def session_count(self, raw=False):
        data = self.query('haproxy_frontend_current_sessions { frontend="http-front" }')
        return self.extract(data, raw)



    def session_rate(self, raw=True):
        data = self.query_range('haproxy_frontend_current_session_rate { frontend="http-front" }')
        return self.extract(data, raw)



