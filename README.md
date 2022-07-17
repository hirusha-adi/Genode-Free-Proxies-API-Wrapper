# Genode-Free-Proxies-API-Wrapper

Python3 - Genode Free Proxies API Wrapper

API wrapper for
[https://geonode.com/free-proxy-list](https://geonode.com/free-proxy-list)

Scrap proxies easily with a simple knwoledge in python3 (all you need to know is the usage of `for` loops to work this api wrapper). This will scrap the Genode Free Proxies API and return the results. This is an wrapper for the Genode Free Proxies API

# Usage

```python
import geonode
prox = geonode.Proxylist()
proxies = prox.get_proxies_only()
for proxy in proxies:
    print(proxy)
```
