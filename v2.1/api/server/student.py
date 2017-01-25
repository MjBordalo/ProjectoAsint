class Student:
	def __init__(self,uname,id):
		self.uname=uname
		self.id=id
		self.room=None 
	def __str__(self):
		if self.room is not None: tmp=self.room
		else: tmp="Empty"
		return	"----- STUDENT: \n" + \
				"\t --- Username: " + self.uname + '\n' + \
				"\t --- Identifier: " + self.id + '\n' + \
				"\t --- Room: " + tmp + '\n'
	def __eq__(self,other):
		return self.id==other.id or self.uname==other.uname
	def check_in(self,room_id):
		self.room=room_id
	def check_out(self):
		self.room=None

# ### SAMPLE TEST MODULE ###
# def main():
# 	s1=Student("miferrei","1")
# 	s1.check_in("Alameda/Torre Norte/0/EA2")
# 	print s1
# 	s1.check_out()
# 	print s1

# if __name__ == "__main__":
# 	main()