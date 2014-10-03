__author__ = 'renshiming'
import json
f = open('/Users/renshiming/Desktop/capstone/log_split.json')
lines = f.readlines()
f.close()
print(len(lines))

smalldict = {}
bigdict = {}
import time
import datetime

# time.mktime(datetime.datetime.strptime(s, "%d/%m/%Y").timetuple())
#count = 1
for line in lines:
    #print count
    #if count > 10:
    #    break
    try:
        d = json.loads(line)
        if "tstamp" in d:
            current = time.mktime(datetime.datetime.strptime(d["tstamp"], "%Y-%m-%d %H:%M:%S").timetuple())
            #print current
            #count = count + 1
            if d["tstamp"] in bigdict:
                bigdict[d["tstamp"]] = max(bigdict[d["tstamp"]], current)
            else:
                bigdict[d["tstamp"]] = current
            if d["tstamp"] in smalldict:
                smalldict[d["tstamp"]] = min(smalldict[d["tstamp"]], current)
            else:
                smalldict[d["tstamp"]] = current
        #count = count + 1
        #print bigdict[d["tstamp"]]
        #print smalldict[d["tstamp"]]
    except:
        continue

for t in bigdict:
    if bigdict[t] - smalldict[t] > 240 * 60:
        print t
