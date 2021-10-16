# import requests as req
#
# data = req.get("https://proxylist.geonode.com/api/proxy-list?limit=50&page=1&sort_by=lastChecked&sort_type=desc").json()
#
# for i in range(len(data["data"])):
#
#     did = data["data"][i]["_id"]
#     ip = data["data"][i]["ip"]
#
#     print(did, "-", ip)

from .proxies import Proxylist


# class Request:
#     def __init__(self):
#         pass
#
#     def get_dict(self):
#
