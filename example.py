import geonode
prox = geonode.Proxylist()

# data_json = prox.get_dicts()
# print(data_json)

data_json = prox.get_proxies_only()
for i in data_json:
    print(i)
