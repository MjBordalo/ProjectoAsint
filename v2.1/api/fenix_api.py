### Import Libraries ###
## External Libraries ##
import json
import urllib2
import sys
import datetime

#Construct today str
today = datetime.datetime.now()
today_str=str(today.day)+"/"+str(today.month)+"/"+str(today.year)
### URL ###
server="fenix.tecnico.ulisboa.pt"

def getBuildings(campus_id):
	buildings_name=[]
	buildings_id=[]

	URI='api/fenix/v1/spaces'
	URL='http://%s/%s/%s?day=%s'%(server,URI,campus_id,today_str)
	response=urllib2.urlopen(URL).read()
	dataIn=json.loads(response)

	for j in dataIn['containedSpaces']:
		if(j['type']=="BUILDING"):
			buildings_name.append(j['name'])
			buildings_id.append(j['id'])
	return buildings_name,buildings_id


def getCampus():
	URI='api/fenix/v1/spaces'
	URL='http://%s/%s'%(server,URI)
	response=urllib2.urlopen(URL).read()
	dataIn=json.loads(response)

	output_names=[]
	output_ids=[]
	for i in dataIn:
		output_ids.append(i['id'])
		output_names.append(i['name'])


	print(output_names)
	print(output_ids)
	return output_names,output_ids

def main():
	[a,b]=getBuildings(2448131363667)

if __name__=="__main__":
	main()
