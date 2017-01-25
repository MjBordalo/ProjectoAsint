import sys
import random
import hashlib
from room import Room
from student import Student

# def rooms2dict(rooms):
# 	dic={}
# 	for room in rooms:
# 		tmp=room.id.split('/')
# 		for i in range(4):
# 			exp1='dic'+''.join(["[tmp[%d]]"%(j) for j in range(i)])
# 			exp2=exp1+"[tmp[%d]]"%(i)
# 			if tmp[i] not in eval(exp1):
# 				if i==3: exp2=exp1+"=tmp[%d]"%(i)
# 				else: exp2=exp1+"[tmp[%d]]"%(i)+"={}"
# 				exec(exp2)
# 	return dic

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
		tmp=room.id.split('/')
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

### Storage of Server Classes ###
class Storage:
	def __init__(self):
		self.studs=[]
		self.avab_rooms=[]
	def __str__(self):
		return "---------- List of Students ----------\n" + '\n' + \
			   "\n".join([str(room) for room in self.studs]) + '\n' + \
			   "---------- List of Rooms ----------\n" + '\n' + \
			   "\n".join([str(room) for room in self.avab_rooms])
	def add_avab_room(self,uname_id,rom_id):
		if Room(rom_id) not in self.avab_rooms and \
		   Student("",uname_id)==Student("","0") and \
		   Student("admin",0) in self.studs:
			self.avab_rooms.append(Room(rom_id))
			return True
		else:
			return False
	def add_stud(self,uname):
		if Student(uname,"") not in self.studs:
			if uname=="admin":
				stud_id="0"
			else:
				md5 = hashlib.md5()
				tmp = random.randint(0, sys.maxint)
				md5.update(str(tmp)); stud_id=str(int(md5.hexdigest(),16))
			self.studs.append(Student(uname,stud_id))
			return stud_id
		else:
			return False

	def delete_avab_room(self,uname_id,rom_id):
		if Room(rom_id) in self.avab_rooms and \
		   Student("",uname_id)==Student("","0") and \
		   Student("admin",0) in self.studs:
			index=self.avab_rooms.index(Room(rom_id))
			for stud_id in self.avab_rooms[index].stud:
				self.check_out_stud(stud_id)
			self.avab_rooms.remove(Room(rom_id))
			return True
		else:
			return False

	def check_in_stud(self,stud_id,rom_id):
		if Room(rom_id) in self.avab_rooms and \
		   Student("",stud_id)!=Student("",0) and \
		   Student("",stud_id) in self.studs:
			index=self.studs.index(Student("",stud_id))
			if self.studs[index].room==None:
				self.studs[index].check_in(rom_id)
				index=self.avab_rooms.index(Room(rom_id))
				self.avab_rooms[index].add(stud_id)
				return True
			else:
				return False
		else:
			return False
	def check_out_stud(self,stud_id):
		if Student("",stud_id)!=Student("",0) and \
		   Student("",stud_id) in self.studs:
			index=self.studs.index(Student("",stud_id))
			if self.studs[index].room==None:
				return False
			else:
				rom_id=self.studs[index].room
				self.studs[index].check_out()
				index=self.avab_rooms.index(Room(rom_id))
				self.avab_rooms[index].remove(stud_id)
				return True
		else:
			return False

	def getStudState(self,stud_id):
		if Student("",stud_id) in self.studs:
			index=self.studs.index(Student("",stud_id))
			return {'Username': self.studs[index].uname, 'Room': self.studs[index].room}
		else:
			return False

	def retrieveAvabCampus(self,stud_id):
		if Student("",stud_id) in self.studs:
			return campus2lst(self.avab_rooms)
		else:
			return False
	def retrieveAvabBuilding(self,stud_id,campus):
		if Student("",stud_id) in self.studs:
			return building2lst(self.avab_rooms,campus)
		else:
			return False
	def retrieveAvabFloor(self,stud_id,campus,building):
		if Student("",stud_id) in self.studs:
			return floor2lst(self.avab_rooms,campus,building)
		else:
			return False
	def retrieveAvabName(self,stud_id,campus,building,floor):
		if Student("",stud_id) in self.studs:
			return name2lst(self.avab_rooms,campus,building,floor)
		else:
			return False
	def retrieveStudents(self,stud_id,rom_id):
		if Room(rom_id) in self.avab_rooms and \
		   	Student("",stud_id) in self.studs:
			return sorted([item.uname for item in self.studs if item.room==rom_id])
		else:
			return False

	# def showAvabRooms(self,stud_id):
	# 	if Student("",stud_id) in self.studs:
	# 		return rooms2dict(self.avab_rooms)
	# 	else:
	# 		return False

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
