# -*- coding: utf-8 -*-
import sys
import random
import hashlib
from google.appengine.ext import ndb


from room import Room, add_room, room_on_off, remove_room, add_student, remove_student, delete_rooms
from student import Student, create_student, delete_students,check_in ,check_out

parent_key_student=ndb.Key("Entity","student_root")
parent_key_room=ndb.Key("Entity","room_root")

def get_registered_rooms():
	output=[]
	rooms=Room.query(ancestor=parent_key_room).filter().fetch()
	if(rooms==None):
		return output
	else:
		for aux in rooms:
			output.append(aux.id)
		return output

def delete_all():
	delete_students()
	delete_rooms()


def campus2lst(rooms):
	lst=[]
	for room in rooms:
		tmp=room.id.split('/')[0]
		if tmp not in lst: lst.append(tmp)
	return sorted(lst)

def building2lst(rooms,campus):
	lst=[]
	for room in rooms:
		tmp=room.id.split('/')
		if tmp[0] == campus and \
		   tmp[1] not in lst:
			lst.append(tmp[1])
	return sorted(lst)

def floor2lst(rooms,campus,building):
	lst=[]
	for room in rooms:
		#tmp=unicodedata.normalize('NFKD', room.id).encode('ascii','ignore')
		tmp=room.id
		tmp=tmp.split('/')
		if tmp[0] == campus and \
		   tmp[1] == building and \
		   tmp[2] not in lst:
			lst.append(tmp[2])
	return sorted(lst)

def name2lst(rooms,campus,building,floor):
	lst=[]
	for room in rooms:
		tmp=room.id.split('/')
		if tmp[0] == campus and \
		   tmp[1] == building and \
		   tmp[2] == floor and \
		   tmp[3] not in lst:
			lst.append(tmp[3])
	return sorted(lst)


def add_avab_room(uname_id,room_id):
	#Is uname_id the id of the admin?
	if(uname_id !="0"):
		return False
	else:
		#Is admin already registered?
		aux1=Student.query(ancestor=parent_key_student).filter(Student.uname=="admin",Student.id=="0").get()
		if(aux1==None):
			return False
		else:
			#Does this room already exists?
			aux2=Room.query(ancestor=parent_key_room).filter(Room.id==room_id).get()
			if(aux2==None):
				add_room(room_id)
				#room_on_off(room_id,True)
				return True
			else:
				return False
			'''#Is room already available?
				aux3=Room.query(ancestor=parent_key_room).filter(Room.id==room_id,Room.available==True).get()
				if(aux3==None):
					room_on_off(room_id,True)
					return True
				else:'''


def add_stud(uname):
	#Does the student already exists in dB?
	check=Student.query(ancestor=parent_key_student).filter(Student.uname==uname).get()
	if(check==None):
		#Admin case!
		if uname=="admin":
			stud_id="0"
		else:
		#Student case! Generate a id by a hash function
			md5 = hashlib.md5()
			tmp = random.randint(0, sys.maxint)
			md5.update(str(tmp)); stud_id=str(int(md5.hexdigest(),16))

		create_student(uname,stud_id)
		return stud_id
	else:
		return False


def delete_avab_room(uname_id,room_id):
	#Is uname_id the id of the admin?
	if(uname_id !="0"):
		return False
	else:
		#Is admin already registered?
		aux1=Student.query(ancestor=parent_key_student).filter(Student.uname=="admin",Student.id=="0").get()
		if(aux1==None):
			return False
		else:
			#Does this room exists?
			aux2=Room.query(ancestor=parent_key_room).filter(Room.id==room_id).get()
			if(aux2==None):
				return False
			else:
			#Delete room
				remove_room(room_id)
				return True


def check_in_stud(stud_id,room_id):
	#Is uname_id the id of the admin?
	if(stud_id =="0"):
		return False
	else:
		#Does this room exists?
		aux1=Room.query(ancestor=parent_key_room).filter(Room.id==room_id).get()
		if(aux1==None):
			return False
		else:
			#Is student already registered and not in this room?
			aux2=Student.query(ancestor=parent_key_student).filter(Student.id==stud_id,Student.room!=room_id).get()
			if(aux2==None):
				return False
			else:
				check_in(aux2,room_id)
				return True

def check_out_stud(stud_id):
	#Is uname_id the id of the admin?
	if(stud_id =="0"):
		return False
	else:
		#Is student already registered?
		aux1=Student.query(ancestor=parent_key_student).filter(Student.id==stud_id).get()
		if(aux1==None):
			return False
		else:
			#Does this room exists?
			aux2=Room.query(ancestor=parent_key_room).filter(Room.id==aux1.room).get()
			if(aux2==None):
				return False
			else:
				check_out(aux1)
				return True

def teste(unameid):
	aux=Student(uname="name",id=unameid,room="None")
	aux.put()

	student=Student.query(ancestor=parent_key_student).filter(Student.id==unameid).get()
	return student.room


def getStudState(stud_id):
	student=Student.query(ancestor=parent_key_student).filter(Student.id==stud_id).get()
	if(student==None):
		return False
	else:
		return {'Username': student.uname, 'Room': student.room}

def retrieveAvabCampus(stud_id):
	#CHECK IF STUDENT EXIST IN DATABASE
	student=Student.query(ancestor=parent_key_student).filter(Student.id==stud_id).get()
	if(student==None):
		return False
	else:
		rooms=Room.query(ancestor=parent_key_room).fetch()
		rooms_list=[]
		for aux in rooms:
			rooms_list.append(aux)
		return campus2lst(rooms_list)
def retrieveAvabBuilding(stud_id,campus):
	#CHECK IF STUDENT EXIST IN DATABASE
	student=Student.query(ancestor=parent_key_student).filter(Student.id==stud_id).get()
	if(student==None):
		return False
	else:
		rooms=Room.query(ancestor=parent_key_room).fetch()
		rooms_list=[]
		for aux in rooms:
			if(campus in aux.id):
				rooms_list.append(aux)
		return  building2lst(rooms,campus)



def retrieveAvabFloor(stud_id,campus,building):
	student=Student.query(ancestor=parent_key_student).filter(Student.id==stud_id).get()
	if(student==None):
		return False
	else:
		rooms=Room.query(ancestor=parent_key_room).fetch()
		rooms_list=[]
		for aux in rooms:
			#return [str(type(building)),str(type(aux.id))]
			if(building in aux.id and campus in aux.id):
				rooms_list.append(aux)
		return  floor2lst(rooms_list,campus,building)

def retrieveAvabName(stud_id,campus,building,floor):
	student=Student.query(ancestor=parent_key_student).filter(Student.id==stud_id).get()
	if(student==None):
		return False
	else:
		rooms=Room.query(ancestor=parent_key_room).fetch()
		rooms_list=[]
		for aux in rooms:
			#return [str(type(building)),str(type(aux.id))]
			if(floor in aux.id and building in aux.id and campus in aux.id):
				rooms_list.append(aux)
		return name2lst(rooms_list,campus,building,floor)

def retrieveStudents(stud_id,room_id):
	#Is the student already registered?
	aux2=Student.query(ancestor=parent_key_student).filter(Student.id==stud_id).get()
	if(aux2==None):
		return False
	else:
		#Does the room already exists?
		students_room=Room.query(ancestor=parent_key_room).filter(Room.id==room_id).get()
		if(students_room==None):
			return False
		else:
			if(len(students_room.stud)==0):
				return []
			else:
				output=[]
				for ite in students_room.stud:
					student_name=Student.query(ancestor=parent_key_student).filter(Student.id==ite).get()
					output.append(student_name.uname)
				return sorted(output)

''''
### SAMPLE TEST MODULE ###
def main():
	st=Storage()
	st.add_avab_room("Alameda/Torre Norte/0/EA2")
	#st.add_avab_room("Alameda/Torre Norte/0/EA1")
	#st.add_avab_room("TagusPark/Torre Norte/0/TA1")
	#id=st.add_stud("miferrei")
	#st.check_in_stud(id,"TagusPark/Torre Norte/0/TA1")
	# print st
	#st.delete_avab_room("TagusPark/Torre Norte/0/TA1")
	# print st

if __name__ == "__main__":
	main()
'''
