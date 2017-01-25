### Import Libraries ###
## External Libraries ##
import json
import urllib2
import sys

### URL ###
server="fenix.tecnico.ulisboa.pt"
port=8080

def getCampus():
	URI='api/fenix/v1/spaces'
	URL='http://%s/%s'%(server,URI)
	response=urllib2.urlopen(URL).read()
	dataIn=json.loads(response)

	output=[]
	for i in dataIn:
		output.append(i['name'])

	return output

if __name__=="__main__":
	main()
