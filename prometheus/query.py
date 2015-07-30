#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import datetime
import json

class PrometheusQuery():

    def __init__(self, url, endpoint='/api/v1'):
        self.url = url
        self.endpoint = endpoint


    def query(self, query):
        now = datetime.datetime.utcnow().isoformat()
        return requests.get(self.url + self.endpoint + '/query?query=' + query + '&time=' + now + 'Z').content

    def extract(self, result, raw=False):
        if (not raw):
            data = json.loads(result)
            return data['data']['result'][0]['value'][1]

        return result


    def session_count(self, raw=False):
        data = self.query('haproxy_frontend_current_sessions { frontend="http-front" }')
        return self.extract(data, raw)



    def session_rate(self, raw=False):
        data = self.query('haproxy_frontend_current_session_rate { frontend="http-front" }')
        return self.extract(data, raw)



