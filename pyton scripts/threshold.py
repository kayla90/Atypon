__author__ = 'renshiming'
import json
f = open('/Users/renshiming/Desktop/capstone/log_split.json')
lines = f.readlines()
f.close()
print(len(lines))

dict = {}

username = {}
for line in lines:
    try:
        d = json.loads(line)
        if "sessionid" in d:
            if "success" in d:
                if int(d["success"]) == 0:
                    if d["sessionid"] in dict:
                        dict[d["sessionid"]] = dict[d["sessionid"]] + 1
                    else:
                        dict[d["sessionid"]] = 1
                        if "identity" in d:
                            username[d["sessionid"]] = d["identity"]
                        else:
                            username[d["sessionid"]] = "NOIDENTITY"

    except:
        continue

i = 0
count = 0
for session in dict:
    count = count + int(dict[session])

count = count/len(dict)

print count