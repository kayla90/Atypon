'''
Created on Oct 23, 2014

@author: Abby

Pull ip and success codes from JSON and write to csv
'''

import json 
import csv
import io

# with open('C:\\Users\\Abby\\Documents\\Fall2014\\Capstone\\Data\\success.csv','wb') as csvfile:
with open('success.csv','wb') as csvfile:
    datout = csv.writer(csvfile, delimiter=',')
    
    #with open('C:\\Users\\Abby\\Documents\\Fall2014\\Capstone\\Data\\tandf_action-events-enriched_2014-04.json') as f:
    with open('tandf_action-events-enriched_2014-04.json') as f:
        for line in f:
            j = json.loads(line)
            row = [j['ip'],j['success']]
            datout.writerow(row)
csvfile.close()
f.close()
