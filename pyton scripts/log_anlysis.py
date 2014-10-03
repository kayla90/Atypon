__author__ = 'renshiming'
import json
f = open('/Users/renshiming/Desktop/capstone/log_split.json')
lines = f.readlines()
f.close()
print(lines[2])
print(len(lines))
import time
import datetime


#for line in lines:
#    d = json.loads(line)
#    if "identity" in d:
#        # dd = json.loads(d["identity"])
#        if "username" in d["identity"]:
#            print d["identity"]["username"]
d = json.loads(lines[0])
print(d["tstamp"])
current = time.mktime(datetime.datetime.strptime(d["tstamp"], "%Y-%m-%d %H:%M:%S").timetuple())
print current
print(
    datetime.datetime.fromtimestamp(
        int(current)
    ).strftime('%Y-%m-%d %H:%M:%S')
)
