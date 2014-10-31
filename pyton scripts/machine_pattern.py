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
        if 'sessionid' in d:
            if 'content' in dict:
                content = json.loads(d['content'])
                if 'articleid' in content:
                    if d['sessionid'] in dict:
                        arr = dict[d['sessionid']]
                        arr.append(content['articleid'])
                    else:
                        arr = []
                        arr.append(content['articleid'])
                        dict[d['sessionid']] = arr
    except:
        continue

for session in dict:
    arr = dict[session]
    l = len(arr)
    arr.sort(arr)
    difference = int(arr[-1]) - int(arr[0])
    if difference <= l:
        print session
