# command to run parse.py: cat literatum.access-2014-03-01.lion103.log | python parse.py
import sys

line = sys.stdin.readline() # Read data set line by line 

#file = open('ip_timestamp.csv','wb')
file = open('timestamp_count.csv','wb')
dict_ip = {} 
dict_time = {}

while line:


	ip_start = line.index('\"')
	ip_end = line.index('\" ',ip_start)
	ip = line[ip_start+1:ip_end]

	if ip in dict_ip:
		dict_ip[ip] = dict_ip[ip] + 1
	else:
		dict_ip[ip] = 1

	#print 'ip: ', line[ip_start+1:ip_end]

	time_start = line.index('[')
	time_end = line.index(']',time_start)
	time = line[time_start + 1:time_end]
	if time in dict_time:
		dict_time[time] = dict_time[time] + 1
	else:
		dict_time[time] = 1

	#print 'time: ', line[time_start + 1:time_end]

	#file.write(ip + ',' + time + '\n')

	line = sys.stdin.readline()

#file.close()
#print dict_ip.items()
for a, b in sorted(dict_ip.iteritems(), key=lambda item: item[1], reverse=True)[:10]:

    print a, b

for a, b in sorted(dict_time.iteritems(), key=lambda item: item[1], reverse=True)[:10]:

    print a, b

for a, b in sorted(dict_time.iteritems(), key=lambda item: item[1], reverse=True):
	print a, b

	file.write(str(a) + ',' + str(b) + '\n')
file.close()
