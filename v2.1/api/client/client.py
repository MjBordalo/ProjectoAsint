### Import Libraries ###
## External Libraries ##
import json 
import urllib2
import sys

### URL ###
server="localhost"
port=8080

## Method :: POST ||  Description :: Rom R is Added to Available Rooms ##
def addRoom(uname_id,campus,building,floor,name):
	print "---- OPERATION: Add Available Room ---- "
	URI='roistapi/uname/%s/room/%s' % (uname_id,'/'.join([campus,building,floor,name]))
	URL='http://%s:%d/%s'%(server,port,URI)
	dataOut={}
	request=urllib2.Request(URL) 
	request.add_header('Content-Type','application/json') 
	response=urllib2.urlopen(request,json.dumps(dataOut))
	dataIn=json.load(response)
	if dataIn["Success"] is True:
		print "---- RESULT: Successful ---- "
	else: 
		print "---- RESULT: Unuccessful ---- "

## Method :: POST ||  Description :: User U Authenticates in Server ##
def authenUser(uname):
	print "---- OPERATION: Authenticate User ---- "
	URI='roistapi/start'
	URL='http://%s:%d/%s'%(server,port,URI)
	dataOut={'uname':uname}
	request=urllib2.Request(URL) 
	request.add_header('Content-Type','application/json') 
	response=urllib2.urlopen(request,json.dumps(dataOut))
	dataIn=json.load(response)
	if dataIn["Success"] is True:
		print "---- RESULT: Successful ---- "
		print "---- YOUR IDENTIFIER: %s " % (dataIn["Identifier"])
	else: 
		print "---- RESULT: Unuccessful ---- "

## Method :: POST ||  Description :: Student S Checks In from Room R ##
def checkIn(uname_id,campus,building,floor,name):
	print "---- OPERATION: Check-In User ---- "
	URI='roistapi/uname/%s/room/%s' % (uname_id,'/'.join([campus,building,floor,name]))
	URL='http://%s:%d/%s'%(server,port,URI)
	dataOut={}
	request=urllib2.Request(URL) 
	request.add_header('Content-Type','application/json') 
	response=urllib2.urlopen(request,json.dumps(dataOut))
	dataIn=json.load(response)
	if dataIn["Success"] is True:
		print "---- RESULT: Successful ---- "
	else: 
		print "---- RESULT: Unuccessful ---- "

## Method :: DELETE ||  Description :: Student S Checks Out from Current Room ##
def checkOut(uname_id):
	print "---- OPERATION: Check-Out User ---- "
	URI='roistapi/uname/%s' % (uname_id)
	URL='http://%s:%d/%s'%(server,port,URI)
	request=urllib2.Request(URL) 
	request.get_method = lambda: 'DELETE'
	response=urllib2.urlopen(request)
	dataIn=json.load(response)
	if dataIn["Success"] is True:
		print "---- RESULT: Successful ---- "
	else: 
		print "---- RESULT: Unuccessful ---- "

## Method :: DELETE ||  Description :: Rom R is Deleted From Available Rooms ##
## and All Students in R are Checked Out ##
def deleteRoom(uname_id,campus,building,floor,name):
	print "---- OPERATION: Delete Available Room ---- "
	URI='roistapi/uname/%s/room/%s' % (uname_id,'/'.join([campus,building,floor,name]))
	URL='http://%s:%d/%s'%(server,port,URI)
	request=urllib2.Request(URL) 
	request.get_method = lambda: 'DELETE'
	response=urllib2.urlopen(request)
	dataIn=json.load(response)
	if dataIn["Success"] is True:
		print "---- RESULT: Successful ---- "
	else: 
		print "---- RESULT: Unuccessful ---- "

## Method :: GET ||  Description :: Retrieve All Available Rooms ##
def showAvabSpaces(uname_id,campus=None,building=None,floor=None):
	print "---- OPERATION: Show Available Spaces ---- "
	if campus is None:
		loc="Campus";URI='roistapi/uname/%s/room' % (uname_id)
	elif building is None: 
		loc="Building";URI='roistapi/uname/%s/room/%s' % (uname_id,campus)
	elif floor is None:
		loc="Floor";URI='roistapi/uname/%s/room/%s/%s' % (uname_id,campus,building)
	else:
		loc="Name";URI='roistapi/uname/%s/room/%s/%s/%s' % (uname_id,campus,building,floor)
	print "---- OPERATION: Show All Available %s ---- " % (loc)
	URL='http://%s:%d/%s'%(server,port,URI)
	response=urllib2.urlopen(URL).read() 
	dataIn=json.loads(response)
	if dataIn["Success"] is True:
		print "---- RESULT: Successful ---- "
		print "---- ALL AVAILABLE %s: ----" % (loc)
		print dataIn["Rooms"]
	else: 
		print "---- RESULT: Unuccessful ---- "

## Method :: GET ||  Description :: Retrieve All Available Rooms ##
def showStudents(uname_id,campus,building,floor,room):
	print "---- OPERATION: Show Check-In Students ---- "
	URI='roistapi/uname/%s/room/%s/%s/%s/%s' % (uname_id,campus,building,floor,room)
	URL='http://%s:%d/%s'%(server,port,URI)
	response=urllib2.urlopen(URL).read() 
	dataIn=json.loads(response)
	if dataIn["Success"] is True:
		print "---- RESULT: Successful ---- "
		print "---- STUDENTS CHECKED-IN AT %s %s %s %s: ----" % (campus,building,floor,room)
		print dataIn["Students"]
	else: 
		print "---- RESULT: Unuccessful ---- "

def main():
	print "---------- Started Client Application ---------- "
	oper=sys.argv[1]
	if oper=="Authenticate" and len(sys.argv)==3:
		authenUser(sys.argv[2])
	elif oper=="Add_Available_Room" and len(sys.argv)==7:
		addRoom(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6])
	elif oper=="Check_In" and len(sys.argv)==7:
		checkIn(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6])
	elif oper=="Check_Out" and len(sys.argv)==3:
		checkOut(sys.argv[2])
	elif oper=="Delete_Available_Room" and len(sys.argv)==7:
		deleteRoom(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6])
	elif oper=="Show_Available_Rooms":
		if len(sys.argv)==3: showAvabSpaces(sys.argv[2])
		elif len(sys.argv)==4: showAvabSpaces(sys.argv[2],sys.argv[3])
		elif len(sys.argv)==5: showAvabSpaces(sys.argv[2],sys.argv[3],sys.argv[4])
		elif len(sys.argv)==6: showAvabSpaces(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])
		else: print "---- Invalid Operation ----"
	elif oper=="Show_Students" and len(sys.argv)==7:
		showStudents(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6])
	else:
		print "---- Invalid Operation ----"

if __name__ == "__main__":
	main()