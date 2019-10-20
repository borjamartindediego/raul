# -*- coding: utf-8 -*-
import json, requests, sys, os
import datetime
from datetime import timedelta 
from datetime import datetime
def sort_by_date(d):
	return d.get ('startTime',None)

today=datetime.now().strftime("%Y-%m-%d")
delta = timedelta(days=1)
date = datetime.now() + delta
today1=date.strftime("%Y-%m-%d")
#print today

# Replace with the correct URL
url=("https://www.olympicchannel.com/en/api/v1/live/video/") + today1 + ("/epglist")
#print ("API URL: %s"%url)
#print url

# It is a good practice not to hardcode the credentials. So ask the user to enter credentials at runtime
myResponse = requests.get(url)
#print (myResponse.status_code)

# For successful API call, response code will be 200 (OK)
if(myResponse.ok):

    # Loading the response data into a dict variable
    # json.loads takes in only binary or string variables so using content to fetch binary content
    # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
    jData = json.loads(myResponse.content)
    with open('epg.json','w+') as f:
        json.dump(jData,f)
else:
  # If response code is not ok (200), print the resulting http error code with description
    myResponse.raise_for_status()

i=1
OCChannel="OC1"
ndate= datetime.now()
startdate=datetime.now().strftime("%Y-%m-%dT06:00:00")
et="2112-06-14T22:30:00"
fich=open("epg.txt", "w+")
print ("\n\n\t List of OC1 Items for today's EPG\n")
fich.write("\n\n\t List of OC1 Items for today's EPG\n")

#delta = timedelta(days=1)
#deltainfi= timedelta(days=1000)
newtime=ndate+delta
sameday=datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
enddate=newtime.strftime("%Y-%m-%dT06:00:00")
#print '\033[1;31mGray like Ghost\033[1;m'
print ("API URL: %s\n"%url)
fich.write ("API URL: ")
fich.write (url)
fich.write ("\n")
fich.write ("\n")
#print ("Start date: %s"% sameday)
#print ("Until date: %s\n"% enddate)

with open ('epg.json') as json_file:
	print (("{: <10} ".format("    Item")) + ("{: <6} ".format("ChID")) + ("{: <90} ".format("  Event Title"))+("{: <20} ".format("  Start Time"))+("{: <20} ".format("  End Time")))
	print ("------------------------------------------------------------------------------------------------------------------------------------------------------")
	fich.write("{: <10} ".format("    Item") + "{: <6} ".format("ChID") + "{: <90} ".format("  Event Title") + "{: <20} ".format("  Start Time") + "{: <20} ".format("  End Time"))
	fich.write("\n")
	fich.write("------------------------------------------------------------------------------------------------------------------------------------------------------\n")
	#print("\n")
	data=json.load(json_file)
	for p in data['modules']:
		for q in sorted (p['content'],key=sort_by_date):
			try:
				if  q['channelId'] == OCChannel:
					if (q['startTime'])>= startdate  and  (q['startTime'])<= enddate:
						st=q['startTime']
						#st=q['startTime'][:-3]
						#print ("ST= %s"% st + " - " + "ET= %s"% et)  
                        			if st > et:
                            				tt = datetime.strptime(st,"%Y-%m-%dT%H:%M:%S") - datetime.strptime(et,"%Y-%m-%dT%H:%M:%S")
                            				print ("\t\t\t**************************")
                                                        print ("\t\t\t* GAP Difference " + ("%s"% tt) + " *")
                                                        print ("\t\t\t**************************")
			     				print(("{: <10} ".format("    %s" %i)) + ("{: <6} ".format(q['channelId'])) + ("{: <90} ".format(q['title'].encode("utf-8")))+("{: <20} ".format(q['startTime']))+("{: <20} ".format(q['endTime'])))
							fich.write("\t\t\t****** GAP Difference ")
							fich.write(str(tt))
							fich.write(" ******")
							fich.write("\n")
							fich.write("{: <10} ".format("    %s" %i) + "{: <6} ".format(q['channelId']) + "{: <90} ".format(q['title'].encode("utf-8"))+"{: <20} ".format(q['startTime'])+"{: <20} ".format(q['endTime']))
							fich.write("\n")
							#fich.write(
							#tt = datetime.strptime(st,"%Y-%m-%dT%H:%M:%S") - datetime.strptime(et,"%Y-%m-%dT%H:%M:%S")
							#print ("  Difference: %s"% tt)
						else:
							print(("{: <10} ".format("    %s" %i)) + ("{: <6} ".format(q['channelId'])) + ("{: <90} ".format(q['title'].encode("utf-8")))+("{: <20} ".format(q['startTime']))+("{: <20} ".format(q['endTime'])))
							fich.write("{: <10} ".format("    %s" %i) + "{: <6} ".format(q['channelId']) + "{: <90} ".format(q['title'].encode("utf-8")) + "{: <20} ".format(q['startTime']) + "{: <20} ".format(q['endTime']))
							fich.write("\n")
						i=i+1
						#st=q['startTime'][:-3]
						#et=q['endTime'][:-3]
						et=q['endTime']
						#print st
						#print et
			except KeyError:
				print (" ")
items=i-1
print ("Total Items: %s" %items)
print ("------------------------------------------------------------------------------------------------------------------------------------------------------")
fich.write  ("\n")
fich.write ("Total Items: ")
fich.write (str(items))
fich.write("\n")
fich.write ("------------------------------------------------------------------------------------------------------------------------------------------------------")
fich.write ("\n")
print ("\n")
fich.close()
#os.system("cat epg.txt|./slacktee.sh -q")

