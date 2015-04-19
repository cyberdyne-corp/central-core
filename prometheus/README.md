Prometheus connector

# Descritpion

This component exposes a HTTP API on top of a running Prometheus instance.

The `prometheusparser.py` actualy scrap the web interface of a Prometheus and then returned a structured JSON representation.

The `prometheusapi.py` exposes the JSON as REST endpoints.

# Running

This requires python (at least 3.2) and some dependencies

```
pip install requests beautifulsoup4 bottle
```

## Start the component

```
python prometheusapi.py
```

The component exposes a `/info` endpoint.

## Query the component

Using httpie:

```
http :8080/info
```

```json
{
    "build": {
        "branch": "master", 
        "date": "20150227-14:21:56", 
        "go_version": "1.4.2", 
        "revision": "ae832c9", 
        "user": "root", 
        "version": "0.11.1"
    }, 
    "runtime": {
        "Uptime": "2015-04-19 11:09:04.432726642 +0000 UTC"
    }, 
    "targets": {
        "prometheus": [
            {
                "Base Labels": "{job=\"prometheus\"}", 
                "Endpoint": "http://haproxyexporter:9101/metrics", 
                "Error": "", 
                "Last Scrape": "3.857129706s ago", 
                "State": "ALIVE"
            }, 
            {
                "Base Labels": "{job=\"prometheus\"}", 
                "Endpoint": "http://pushgateway:9091/metrics", 
                "Error": "", 
                "Last Scrape": "536.37794ms ago", 
                "State": "ALIVE"
            }
        ]
    }
}

```


# TO DO

* ease the bootstrap of a dev workstation (setup.py, ...)
* augment the API coverage

