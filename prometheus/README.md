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
    "startup": {
        "alertmanager.http-deadline": "10s", 
        "alertmanager.notification-queue-capacity": "100", 
        "alertmanager.url": "", 
        "alsologtostderr": "false", 
        "config.file": "/config/prometheus.conf", 
        "log_backtrace_at": ":0", 
        "log_dir": "", 
        "logtostderr": "true", 
        "query.staleness-delta": "5m0s", 
        "query.timeout": "2m0s", 
        "stderrthreshold": "2", 
        "storage.incoming-samples-queue-capacity": "65536", 
        "storage.local.checkpoint-dirty-series-limit": "5000", 
        "storage.local.checkpoint-interval": "5m0s", 
        "storage.local.dirty": "false", 
        "storage.local.index-cache-size.fingerprint-to-metric": "10485760", 
        "storage.local.index-cache-size.fingerprint-to-timerange": "5242880", 
        "storage.local.index-cache-size.label-name-to-label-values": "10485760", 
        "storage.local.index-cache-size.label-pair-to-fingerprints": "20971520", 
        "storage.local.memory-chunks": "1048576", 
        "storage.local.path": "/tmp/metrics", 
        "storage.local.persistence-queue-capacity": "32768", 
        "storage.local.retention": "360h0m0s", 
        "storage.remote.timeout": "30s", 
        "storage.remote.url": "", 
        "v": "0", 
        "version": "false", 
        "vmodule": "", 
        "web.console.libraries": "/go/src/github.com/prometheus/prometheus/console_libraries", 
        "web.console.templates": "/go/src/github.com/prometheus/prometheus/consoles", 
        "web.enable-remote-shutdown": "false", 
        "web.listen-address": ":9090", 
        "web.telemetry-path": "/metrics", 
        "web.use-local-assets": "false", 
        "web.user-assets": ""
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

