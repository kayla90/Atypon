__author__ = 'renshiming'
import json
f = open('/Users/renshiming/Desktop/capstone/log_split.json')
lines = f.readlines()
f.close()
print(len(lines))
dict = {}
for line in lines:
    try:
        d = json.loads(line)
        if 'ip' in d:
            if d["ip"] in dict:
                dict[d["ip"]] = dict[d["ip"]] + 1
            else:
                dict[d["ip"]] = 1
    except:
        continue

import operator
sorted_x = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)

i = 0
for ip in sorted_x:
    print str(ip[0]) + " " + str(ip[1])
    i = i + 1
    if i > 100:
        break