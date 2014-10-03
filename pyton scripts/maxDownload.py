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
for session in dict:
    if  dict[session] > 100:
        try:
            print str(session) + " " + str(username[session]) + " " + str(dict[session])
            i = i + 1
        except:
            print "keyerror for dictionary"
    if i > 100:
        break

