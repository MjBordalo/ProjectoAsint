from google.appengine.ext import ndb
parent_key_room=ndb.Key("Entity","room_root")
class Room(ndb.Model):
	id=ndb.StringProperty()
	stud=ndb.StringProperty(repeated=True)

def delete_rooms():
	aux = Room.query(ancestor=parent_key_room)
	ite=0
	for i in aux:
		i.key.delete()
		ite=ite+1
	return ite

def counter(room_id):
	room=Room.query(Room.id==room_id)
	for aux in room:
		return len(aux.stud)
	return 0


def room_on_off(room_id,flag):
	room=Room.query(ancestor=parent_key_room).filter(Room.id==room_id).get()
	room.available=flag
	room.put()


def add_room(id1,list_students=[]):
	new=Room(parent=parent_key_room,id=id1,stud=list_students)
	new.put()

def compare_rooms(room1_id,room2_id):
	return room1_id==room2_id

def add_student(room_id,student_id):
	room=Room.query(ancestor=parent_key_room).filter(Room.id==room_id)
	for aux in room:
		aux.stud.append(student_id)
		aux.put()

def remove_student(room_id,stud_id):
	room=Room.query(ancestor=parent_key_room).filter(Room.id==room_id)
	for aux in room:
		for x in aux.stud:
			x.remove(stud_id)
			aux.put()

def remove_room(room_id):
	room=Room.query(ancestor=parent_key_room).filter(Room.id==room_id).get()
	room.key.delete()


# ### SAMPLE TEST MODULE ###
# def main():
# 	r1=Room("Alameda/Torre Norte/0/EA2")
# 	r1.add("2")
# 	r1.add("4")
# 	r1.add("5")
# 	r1.add("7")
# 	print r1
# 	r1.remove("2")
# 	r1.remove("4")
# 	r1.remove("5")
# 	r1.remove("8")
# 	print r1

# if __name__ == "__main__":
# 	main()
