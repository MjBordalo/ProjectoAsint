from fenixedu.configuration import FenixEduConfiguration
from fenixedu.__init__ import FenixEduClient
import datetime

#Construct today str
today = datetime.datetime.now()
today_str=str(today.day)+"/"+str(today.month)+"/"+str(today.year)

def connect_fenix():
	filename='fenixedutest.ini'
	config=FenixEduConfiguration.fromConfigFile(filename)
	api_client=FenixEduClient(config)
	return api_client

def get_campus(user_fenix):
	campus_name=[]
	campus_id=[]
	campus_aux=user_fenix.get_spaces()
	for i in campus_aux:
		campus_name.append(i['name'])
		campus_id.append(int(i['id']))
	return campus_name,campus_id


def get_buildings(user_fenix,campus_id):
	buildings_name=[]
	buildings_id=[]
	buildings_aux=user_fenix.get_space(campus_id,today_str)
	if(buildings_aux== None):
		return False,False
	else:
		for j in buildings_aux['containedSpaces']:
			if(j['type']=="BUILDING"):
				name=j['name']
				buildings_name.append(name.encode("utf-8"))
				buildings_id.append(int(j['id']))

		return buildings_name,buildings_id

def get_floors(user_fenix,building_id):
	floors_name=[]
	floors_id=[]
	floors_aux=user_fenix.get_space(building_id,today_str)

	if(floors_aux== None):
		return False,False
	else:
		for j in floors_aux['containedSpaces']:
			if(j['type']=="FLOOR"):
				floors_name.append(j['name'])
				floors_id.append(int(j['id']))

		return floors_name,floors_id

def get_rooms(user_fenix,floor_id):
	print(floor_id)
	rooms_name=[]
	rooms_id=[]
	rooms_aux=user_fenix.get_space(floor_id,today_str)

	if(rooms_aux==None):
		return False,False
	else:
		for j in rooms_aux['containedSpaces']:
			if(j['type']=="ROOM"):
				rooms_name.append(j['name'])
				rooms_id.append(int(j['id']))
		return rooms_name,rooms_id

def get_options():
	user_fenix=connect_fenix()
	[campus_names,campus_id]=get_campus(user_fenix)
	for i in range(len(campus_id)):
		print("-----------------------------------------")
		[buildings_name,buildings_id]=get_buildings(user_fenix,campus_id[i])
		print("Campus "+campus_names[i]+" with "+str(len(buildings_id))+" buildings")

		for j in range(len(buildings_name)):
			print(".........................")
			print("Buildings "+buildings_name[j])
			[floors_name,floors_id]=get_floors(user_fenix,buildings_id[j])

			for w in range(len(floors_name)):
				print("+++++++++++++++++++++++++++++++++++++++++")
				print("Floors "+floors_name[w])
				[rooms_name,rooms_id]=get_rooms(user_fenix,floors_id[w])

				for z in range(len(rooms_name)):
					print("Rooms "+rooms_name[z])




def main():

	[a,b]=get_floors(connect_fenix(),2448131361091)
	print(a)
	print(b)

if __name__ == "__main__":
	main()
