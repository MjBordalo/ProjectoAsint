### Import Libraries ###
## External Libraries ##
from bottle import Bottle, run, template, request, response, redirect, static_file, HTTPError, TEMPLATE_PATH
import json
import os
from google.appengine.ext.webapp.util import run_wsgi_app
## My Libraries ##
from storage import Storage
from appendix import *
import connect_fenix

##### APPLICATION CLASS #####
fenix_client=connect_fenix.connect_fenix()
app=Bottle()
st=Storage()

##### SET TEMPLATE PATH #####
#TEMPLATE_PATH.insert(0,os.path.dirname(os.getcwd())+'/browser/views')
##### Set Debug #####
debug=True

############### REST API METHODS ###############
## IF USER is STUDENT:
	## Method :: POST ||  Description :: Student S Checks In from Room R ##
## IF USER is ADMIN:
	## Method :: POST ||  Description :: Rom R is Added to Available Rooms ##
@app.route('/roistapi/uname/<uname_id>/room/<campus>/<building>/<floor>/<name>',method="post")
def addRoom(uname_id,campus,building,floor,name):
	print("id "+str(uname_id))
	room_id='/'.join([campus,building,floor,name])
	if uname_id=="0":
		print "A"
		res=st.add_avab_room(uname_id,room_id)
	else:
		res=st.check_in_stud(uname_id,room_id)
	if debug: print st
	response.content_type='application/json'
	if res is True:
		return {'Success':True}
	else:
		return {'Success':False}

## Method :: POST ||  Description :: Authenticate User U ##
@app.route('/roistapi/start',method="post")
def authenUser():
	uname=request.json.get('uname')
	stud_id=st.add_stud(uname)

	if debug: print st
	response.content_type='application/json'
	if stud_id is False:
		return {'Success':False,'Identifier':None}
	else:
		return {'Success':True,'Identifier':stud_id}

## Method :: DELETE ||  Description :: Student S Checks Out from Current Room ##
@app.route('/roistapi/uname/<uname_id>',method="delete")
def checkOut(uname_id):
	res=st.check_out_stud(uname_id)
	if debug: print st
	if res is True:
		return {'Success':True}
	else:
		return {'Success':False}

## Method :: DELETE ||  Description :: Rom R is Deleted From Available Rooms ##
## and All Students in R are Checked Out ##
@app.route('/roistapi/uname/<uname_id>/room/<campus>/<building>/<floor>/<name>',method="delete")
def deleteRoom(uname_id,campus,building,floor,name):
	room_id='/'.join([campus,building,floor,name])
	res=st.delete_avab_room(uname_id,room_id)
	if debug: print st
	if res is True:
		return {'Success':True}
	else:
		return {'Success':False}

## Method :: GET ||  Description :: Retrieve All Campus With Available Rooms ##
@app.route('/roistapi/uname/<uname_id>/room',method="get")
def retrieveAvabCampus(uname_id):
	res=st.retrieveAvabCampus(uname_id)
	if res is not False:
		return {'Success':True,'Rooms':res}
	else:
		return {'Success':False,'Rooms':None}

## Method :: GET ||  Description :: Retrieve All Buildings B From Campus
## C With Available Rooms ##
@app.route('/roistapi/uname/<uname_id>/room/<campus>',method="get")
def retrieveAvabBuilding(uname_id,campus):
	res=st.retrieveAvabBuilding(uname_id,campus)
	if res is not False:
		return {'Success':True,'Rooms':res}
	else:
		return {'Success':False,'Rooms':None}

## Method :: GET ||  Description :: Retrieve All Floors C From Building B
## and Campus C With Available Rooms ##
@app.route('/roistapi/uname/<uname_id>/room/<campus>/<building>',method="get")
def retrieveAvabFloor(uname_id,campus,building):
	res=st.retrieveAvabFloor(uname_id,campus,building)
	if res is not False:
		return {'Success':True,'Rooms':res}
	else:
		return {'Success':False,'Rooms':None}

## Method :: GET ||  Description :: Retrieve All Names of Rooms R From Floors F
## , Building B and Campus C With Available Rooms ##
@app.route('/roistapi/uname/<uname_id>/room/<campus>/<building>/<floor>',method="get")
def retrieveAvabName(uname_id,campus,building,floor):
	res=st.retrieveAvabName(uname_id,campus,building,floor)
	if res is not False:
		return {'Success':True,'Rooms':res}
	else:
		return {'Success':False,'Rooms':None}

## Method :: GET ||  Description :: Retrieve All Students Check-In in Room R, Floor F
## , Building B and Campus C With Available Rooms ##
@app.route('/roistapi/uname/<uname_id>/room/<campus>/<building>/<floor>/<room>',method="get")
def retrieveStudents(uname_id,campus,building,floor,room):
	room_id='/'.join([campus,building,floor,room])
	res=st.retrieveStudents(uname_id,room_id)
	if res is not False:
		return {'Success':True,'Students':res}
	else:
		return {'Success':False,'Students':None}

# ## Method :: GET ||  Description :: Retrieve All Available Rooms ##
# @app.route('/roistapi/uname/<uname_id>',method="get")
# def showAvabRooms(uname_id):
# 	res=st.showAvabRooms(uname_id)
# 	if res is not False:
# 		return {'Success':True,'Rooms':res}
# 	else:
# 		return {'Success':False,'Rooms':None}

# ## Method :: GET ||  Description :: Retrieve all Rooms in IST ##
# @app.route('uname/<uname_id>/room/<id>',method="get")
# def retrieveRoomsIST(uname_id,room_id):
# 	############ INSERT CALL TO FENIX API ############
# 	if uname_id == 0:
# 		return get_all_rooms_ist()



## DOMINGOS: RETRIEVE ALL BUILDINGS FROM FENIX API
@app.route('/roistapi/fenix/buildings/<campus_id>',method="get")
def retrieveStudents(campus_id):
	buildings_name,buildings_id=connect_fenix.get_buildings(fenix_client,campus_id)
	if buildings_name is not False:
		return {'Success':True,'buildings_name':buildings_name,'buildings_id':buildings_id}
	else:
		return {'Success':False}


## DOMINGOS: RETRIEVE ALL FLOOORS FROM FENIX API
@app.route('/roistapi/fenix/floors/<building_id>',method="get")
def retrieveStudents(building_id):
	floors_name,floors_id=connect_fenix.get_floors(fenix_client,building_id)
	if floors_name is not False:
		return {'Success':True,'floors_name':floors_name,'floors_id':floors_id}
	else:
		return {'Success':False}



## DOMINGOS: RETRIEVE ALL ROOMS FROM FENIX API
@app.route('/roistapi/fenix/rooms/<floor_id>',method="get")
def retrieveStudents(floor_id):
	rooms_names,rooms_id=connect_fenix.get_rooms(fenix_client,floor_id)
	if rooms_names is not False:
		return {'Success':True,'rooms_names':rooms_names,'rooms_id':rooms_id}
	else:
		return {'Success':False}




############### BROWSER INTERFACE CALLS ###############
##### START APPLICATION #####
@app.route('/roistapi/start')
def start():
	return template('browser/views/start_wp.tpl')

##### STUDENT INTERFACE #####
@app.route('/roistapi/uname/<uname_id>',method="get")
def start(uname_id):
	res=st.getStudState(uname_id)
	if res is not False:
		if(uname_id=="0"):
			campus_name,campus_id=connect_fenix.get_campus(fenix_client)
			return template('browser/views/admin_wp.tpl',name=res,id=uname_id,campus_names=campus_name,campus_id=campus_id)
		else:
			return template('browser/views/student_wp.tpl',res)
	else:
		return HTTPError(400, "Username is not logged in")

############### AUXILIARY FUNCTIONS ###############
##### UPLOAD #####
@app.route('/roistapi/static/<dir>/<file>')
def upload(dir, file):
	root=os.path.dirname(os.getcwd())+'/browser/static/' + dir
	return static_file(file, root=root)

#run(app, host='localhost',port=8080,debug=True)'''
run_wsgi_app(app)
