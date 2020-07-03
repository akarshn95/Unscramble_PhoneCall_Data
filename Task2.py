"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

caller_dict={}

# create an empty dictionary with all unique phone numbers
for call in calls:
    caller_dict[call[0]]=0
    caller_dict[call[1]]=0

for call in calls:
    caller_dict[call[0]]+=int(call[3])
    caller_dict[call[1]]+=int(call[3])

caller=max(caller_dict,key=lambda k:caller_dict[k])
highest=caller_dict[caller]
        
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(caller,highest))
