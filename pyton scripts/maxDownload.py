__author__ = 'renshiming'
import json
f = open('/Users/renshiming/Desktop/capstone/log_split.json')
lines = f.readlines()
f.close()
print(len(lines))

dict = {}
#for line in lines:
#    d = json.loads(line)
#    if "identity" in d:
#        # dd = json.loads(d["identity"])
#        if "username" in d["identity"]:
#            print d["identity"]["username"]

for line in lines:
    try:
        d = json.loads(line)
        if "sessionid" in d:
            if d["sessionid"] in dict:
                dict[d["sessionid"]] = dict[d["sessionid"]] + 1
            else:
                dict[d["sessionid"]] = 1
    except:
        continue

i = 0
for session in dict:
    if  dict[session] > 100:
        print str(session) + " " + str(dict[session])
        i = i + 1
    if i > 100:
        break

