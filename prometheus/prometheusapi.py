#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import run, get
from prometheusparser import PrometheusParser

prometheus = PrometheusParser('http://localhost:9090')

@get('/info')
def list():
    return prometheus.info()


if __name__ == '__main__':
    run(host='localhost', port=8080)

