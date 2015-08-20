#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import time

if __name__ == '__main__':

    while True:
        sessionCount = requests.get('http://localhost:8080/session-rate').content
        print sessionCount
        time.sleep(1)

