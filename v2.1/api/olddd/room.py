class Room:
	def __init__(self,id):
		self.id=id
		self.stud=[]
	def __str__(self):
		rom=self.id.split('/')
		return	"\n----- ROOM: \n" + \
			 	"\t --- Campus: " + rom[0] + '\n' + \
				"\t --- Building: " + rom[1] + '\n' + \
			 	"\t --- Floor: " + rom[2] + '\n' + \
			 	"\t --- Name: " + rom[3] + '\n' + \
			 	"----- List of Students: " + \
		     	", ".join(self.stud) + "\n" 
	def __eq__(self,other):
		return self.id==other.id
	def add(self,stud_id):
		self.stud.append(stud_id)
		a= ''.join(self.stud)
	def remove(self,stud_id):
		if stud_id in self.stud:
			self.stud.remove(stud_id)

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