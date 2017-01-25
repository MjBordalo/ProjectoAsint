
from google.appengine.ext import ndb
from room import Room
class Student(ndb.Model):
	uname = ndb.StringProperty()
	id=ndb.StringProperty()
	room=ndb.StringProperty()

def list_students():
	aux = Student.query()
	output=[]
	for i in aux:
		output.append(i.uname)
	return output

def delete_students():
	aux = Student.query()
	ite=0
	for i in aux:
		i.key.delete()
		ite=ite+1
	return ite

parent_key_student=ndb.Key("Entity","student_root")
parent_key_room=ndb.Key("Entity","room_root")


def create_student(name1,id1,room1="-1"):
	student=Student(parent=parent_key_student,uname=name1,id=id1,room=room1)
	student.put()

def check_in(student,room_id):
	student.room=room_id
	student.put()


	room=Room.query(ancestor=parent_key_room).filter(Room.id==room_id).get()
	room.stud.append(student.id)
	room.put()
def check_out(student):
	room=Room.query(ancestor=parent_key_room).filter(Room.id==student.room).get()
	room.stud.remove(student.id)
	room.put()

	student.room="-1"
	student.put()


# ### SAMPLE TEST MODULE ###
# def main():
# 	s1=Student("miferrei","1")
# 	s1.check_in("Alameda/Torre Norte/0/EA2")
# 	print s1
# 	s1.check_out()
# 	print s1

# if __name__ == "__main__":
# 	main()
