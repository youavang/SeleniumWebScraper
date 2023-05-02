import requests
import csv
import concurrent.futures

proxylist = []
with open('proxylist.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        proxylist.append(row[0])

print(len(proxylist))

def extract(proxy):
    try:
        req = requests.get('https://httpbin.org/ip', proxies = {'http': proxy, 'https': proxy}, timeout = 3)
        print(req.json(), ' -working')
    except:
        pass
    return proxy

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(extract, proxylist)   