import fenixedu

class User:
	def __init__(self,name,id,fenix_user):
		self.name=name
		self.id=id
		self.fenix_user=fenix_user
class Users:
	def __init__(self,filename):
		self.id=0
		self.config=fenixedu.FenixEduConfiguration.fromConfigFile(filename)
		self.users=[]
	def add_user(self,name):
		#admin will be the first user! with name=admin and id=0
		self.users.append(User(name,self.id,fenixedu.FenixEduClient(self.config)))
		self.id=self.id+1
	def find_user(self,name):
		for i,value in enumerate(self.users):
			if(value.name==name):
				return value
		return "No client with that name exists!"

def main():
	filename='fenixedutest.ini'
	clients=Users(filename)
	clients.add_user('admin')

	admin=clients.find_user('admin')

	spaces=admin.fenix_user.get_spaces()

	for i,value in enumerate(spaces):
		print(value['name'])

if __name__ == "__main__":
	main()
