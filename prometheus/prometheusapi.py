#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import run, get, template
from prometheusstatusparser import PrometheusStatusParser
from query import PrometheusQuery

prometheus = PrometheusStatusParser('http://localhost:9090')
pq = PrometheusQuery('http://localhost:9090')


@get('/info')
def list():
    return prometheus.info()


@get('/sessions')
def sessionCount():
    return pq.session_count()


@get('/session-rate')
def sessionRate():
    return pq.session_rate()


@get('/health')
def health():
    return 'TODO global health'


@get('/health/<service>')
def health(service):
    return template('TODO health for service {{service}}', service=service)


if __name__ == '__main__':
    run(host='localhost', port=8080)

