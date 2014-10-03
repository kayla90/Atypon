__author__ = 'renshiming'
class IPRecord(object):
    ipfrom = None
    ipto = None
    download_counts = 0
import json
f = open('/Users/renshiming/Desktop/capstone/log_split.json')
lines = f.readlines()
f.close()
print(len(lines))

ip = {}
ip_downloads = {}
import time
import datetime

for line in lines:
    try:
        d = json.loads(line)
        
