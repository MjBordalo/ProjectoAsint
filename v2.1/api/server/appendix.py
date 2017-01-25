def rooms2dict(rooms):
	dic={} 
	for room in rooms:
		tmp=room.id.split('/')
		for i in range(4):
			exp1='dic'+''.join(["[tmp[%d]]"%(j) for j in range(i)])
			exp2=exp1+"[tmp[%d]]"%(i)
			if tmp[i] not in eval(exp1): 
				if i==3: exp2=exp1+"=tmp[%d]"%(i) 
				else: exp2=exp1+"[tmp[%d]]"%(i)+"={}"
				exec(exp2)
	return dic

# ### SAMPLE TEST MODULE ###
# def main():
# 	rooms=["Alameda/Torre Norte/0/EA2","Alameda/Torre Norte/0/EA1","Alameda/Torre Sul/-1/GA1","TagusPark/Torre Norte/0/TA1"]
# 	print [rooms2dict(rooms)]

# if __name__ == "__main__":
# 	main()