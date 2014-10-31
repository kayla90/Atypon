__author__ = 'renshiming'
import json
f = open('/Users/renshiming/Desktop/capstone/log_split.json')
lines = f.readlines()
f.close()
print(len(lines))

dict = {}
set1 = set()
for line in lines:
    try:
        d = json.loads(line)
        if "sessionid" in d:
            if "success" in d:
                if int(d["success"]) == 0:
                    if 'identity' not in d:
                        set1.add(d['sessionid'])
                    else:
                        d2 = json.loads(d['identity'])
                        if 'referrer' not in d2:
                            set1.add(d['sessionid'])

    except:
        continue

for session in set1:
    print session

